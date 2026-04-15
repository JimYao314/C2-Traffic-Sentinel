import os
import base64
import re
import pandas as pd
from lxml import etree
import Evtx.Evtx as evtx_parser


# --- [ 零件 A：解碼專家 ] ---
class PowerDeobfuscator:
    @staticmethod
    def decode_logic(cmd_line: str):
        pattern = r"-(?:e|enc|encodedcommand)\s+([A-Za-z0-9+/=]+)"
        match = re.search(pattern, cmd_line, re.IGNORECASE)
        if match:
            try:
                b64_str = match.group(1)
                return base64.b64decode(b64_str).decode("utf-16-le")
            except:
                return "「解碼失敗」"
        return None


# --- [ 零件 B：整合引擎 ] ---
class SphinxIntegratedHunter:
    def __init__(self, evtx_file):
        self.evtx_file = evtx_file
        self.ns = {'ns': 'http://schemas.microsoft.com/win/2004/08/events/event'}
        self.alerts = []

    def start_hunting(self):
        print(f"[*] Project Sphinx 啟動中...")
        print(f"[*] 正在掃描日誌: {os.path.basename(self.evtx_file)}")

        # 1. 先檢查檔案在不在
        if not os.path.exists(self.evtx_file):
            print(f"[-] 錯誤：找不到日誌檔案 {self.evtx_file}")
            return

        count = 0
        try:
            # 2. 開啟日誌
            with evtx_parser.Evtx(self.evtx_file) as log:
                for record in log.records():
                    count += 1

                    # 顯示進度
                    if count % 1000 == 0:
                        print(f"[*] 已掃描 {count} 筆紀錄...")

                    # 快速測試：只掃描前 5000 筆 (可自行調整)
                    if count > 5000:
                        print("[!] 達到快速測試上限，停止掃描。")
                        break

                    # 3. 解析 XML
                    root = etree.fromstring(record.xml().encode('utf-8'))
                    event_id = int(root.xpath('//ns:EventID', namespaces=self.ns)[0].text)

                    # 4. 偵測程序建立 (4688)
                    if event_id == 4688:
                        cmd_elements = root.xpath("//ns:Data[@Name='CommandLine']", namespaces=self.ns)
                        if cmd_elements and cmd_elements[0].text:
                            raw_cmd = cmd_elements[0].text

                            # 5. Call 解碼小組
                            decoded_cmd = PowerDeobfuscator.decode_logic(raw_cmd)

                            if decoded_cmd:
                                timestamp = root.xpath('//ns:TimeCreated', namespaces=self.ns)[0].get('SystemTime')
                                self.alerts.append({
                                    "時間": timestamp,
                                    "還原內容": decoded_cmd,
                                    "風險": "🔥 高風險指令"
                                })

            # 6. 掃描結束後印出報告
            self._generate_report()

        except Exception as e:
            print(f"[-] 分析過程中發生錯誤: {e}")

    def _generate_report(self):
        print("\n" + "=" * 60)
        print("【 Project Sphinx：Day 5 自動化獵捕報告 】")
        print("=" * 60)
        if self.alerts:
            df = pd.DataFrame(self.alerts)
            print(df.to_string(index=False))
        else:
            print("[OK] 掃描筆數內未發現加密指令。")


# --- [ 指揮中心 ] ---
if __name__ == "__main__":
    # 使用正確的路徑：去上一層，再進去 day2 資料夾找檔案
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    EVTX_TARGET = os.path.join(BASE_DIR, "day2_Process Relationship Analysis", "Security.evtx")

    hunter = SphinxIntegratedHunter(EVTX_TARGET)
    hunter.start_hunting()