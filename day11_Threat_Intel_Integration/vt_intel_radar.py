import os
import requests
import json
import sys
from typing import Dict, Optional
from dotenv import load_dotenv

# --- [ 1. 環境安全加載層 ] ---
# 取得專案根目錄 (C:\InfoSec_Lab)，確保能找到裡面的 .env 檔案
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENV_PATH = os.path.join(BASE_DIR, ".env")

# 載入 .env 檔案中的金鑰
load_dotenv(dotenv_path=ENV_PATH)
print(f"[*] 偵錯：正在讀取的路徑是: {ENV_PATH}")
print(f"[*] 偵錯：該路徑是否存在: {os.path.exists(ENV_PATH)}")

class VirusTotalRadar:
    def __init__(self):
        """
        底層邏輯：從環境變數中安全提取 API Key。
        """
        self.api_key = os.getenv("VT_API_KEY")
        if self.api_key:
            print(f"[*] 偵錯：成功讀取金鑰，長度為 {len(self.api_key)} 字元")
        else:
            print("[!] 偵錯：os.getenv 抓不到任何東西！")
        self.base_url = "https://www.virustotal.com/api/v3/files/"
        self.headers = {
            "x-apikey": self.api_key,
            "accept": "application/json"
        }
        # 本地快取 (Cache)：同一份指紋不重複查詢，節省 API 配額
        self.cache = {}

    def query_hash(self, file_hash: str) -> Optional[Dict]:
        """
        向全球智庫查詢檔案指紋，具備快取、限速判定與權限檢查。
        """
        # A. 憑證完整性檢查
        if not self.api_key or self.api_key == "YOUR_API_KEY_HERE":
            print("[!] 錯誤：未偵測到有效的 VT_API_KEY。請檢查根目錄的 .env 檔案。")
            return None

        # B. 檢查本地快取 (OpSec & 成本考量)
        if file_hash in self.cache:
            print(f"[*] (Cache) 擊中快取：讀取本地情資 -> {file_hash[:12]}...")
            return self.cache[file_hash]

        # C. 執行跨境通訊
        url = f"{self.base_url}{file_hash}"
        print(f"[*] (Cloud) 跨境外派請求：正在向 VirusTotal 查詢指紋 -> {file_hash[:12]}...")

        try:
            # 設定 10 秒超時，防止網路阻塞導致程式死機
            response = requests.get(url, headers=self.headers, timeout=10)

            # D. 根據總部回傳的 HTTP 狀態碼進行決策
            if response.status_code == 200:
                data = response.json()
                stats = data['data']['attributes']['last_analysis_stats']

                result = {
                    "malicious": stats.get('malicious', 0),
                    "suspicious": stats.get('suspicious', 0),
                    "undetected": stats.get('undetected', 0),
                    "link": f"https://www.virustotal.com/gui/file/{file_hash}"
                }

                # 存入快取
                self.cache[file_hash] = result
                return result

            elif response.status_code == 401:
                print("[!] 警告：API Key 無效或權限遭拒（401 Unauthorized）。")
                return None
            elif response.status_code == 404:
                print("[-] 報告：全球智庫目前查無此指紋（404 Not Found）。")
                return {"malicious": 0, "status": "unknown"}
            elif response.status_code == 429:
                print("[!] 警報：達到 API 每分鐘查詢上限（429 Rate Limit）。")
                return "RATE_LIMIT"
            else:
                print(f"[?] 異常：總部回傳未知狀態碼 {response.status_code}")
                return None

        except requests.exceptions.RequestException as e:
            print(f"[-] 網路通訊故障: {e}")
            return None


# --- [ 執行與演練區 ] ---
if __name__ == "__main__":
    # 初始化雷達
    radar = VirusTotalRadar()

    # 測試樣本：EICAR 標準病毒測試碼
    test_virus = "275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f"

    print("\n" + "=" * 60)
    print("🛡️  Project Sphinx Day 11：全球威脅情資連動測試")
    print("=" * 60)

    # 執行第一次查詢 (應該會走 Cloud)
    intel = radar.query_hash(test_virus)

    if isinstance(intel, dict) and "malicious" in intel:
        print(f"\n[+] 鑑定結果：惡意引擎數 {intel['malicious']}")
        print(f"[+] 報告連結：{intel.get('link', 'N/A')}")

        # 執行第二次查詢 (測試 Cache 邏輯)
        print("\n[*] 正在測試重複查詢...")
        radar.query_hash(test_virus)

    elif intel == "RATE_LIMIT":
        print("\n[!] 請稍候一分鐘再進行測試。")