import os
import sys
import shlex
import time
from datetime import datetime

# --- [ 第一戰區：指揮部導航 ] ---
# 自動定位專案總部 (C:\InfoSec_Lab)，確保能 Call 到 Day 6
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)

# 導入 Day 6 的專家（注意：請確保 day6 資料夾內有 __init__.py 檔案）
try:
    from day6_Static_Malware_Analysis.file_analyzer import (
        get_file_fingerprint,
        analyze_pe_structure,
        run_yara_genetic_scan
    )

    print("[+] 成功連線總部：Day 6 專家小組已進入戰備狀態。")
except ImportError:
    print("[-] 錯誤：無法找到 Day 6 模組。請確認 day6 資料夾內有名為 __init__.py 的空白檔案。")
    sys.exit(1)


# --- [ 第二、三、四戰區整合：指揮官類別 ] ---
class SphinxOrchestrator:
    def __init__(self):
        # 設定警報門檻 (分數達到此值則發信/報警)
        self.alert_threshold = 15

    def _extract_clean_path(self, raw_cmd):
        """第二戰區：外科手術級的路徑拆解"""
        try:
            parts = shlex.split(raw_cmd)
            if parts:
                path = parts[0]
                # 權限與存在檢查 (Logic Correction)
                if os.path.isfile(path) and os.access(path, os.R_OK):
                    return path
        except:
            return None
        return None

    def _evaluate_threat(self, scan_results):
        """[新增] 指揮官的決策大腦：加權評分邏輯"""
        score = 0
        reasons = []

        # 1. 判定 YARA (佔比重)
        if scan_results.get('yara_hit'):
            score += 20
            reasons.append("基因特徵匹配惡意代碼 (YARA)")

        # 2. 判定編譯時間 (佔比輕)
        # 模擬：如果編譯年份大於 2025，視為可疑
        if scan_results.get('compile_year', 0) > 2025:
            score += 10
            reasons.append("編譯時間異常 (未來戳記)")

        return score, reasons

    def run_hunt(self, cmd_line):
        """第四戰區：自動化管線總指揮"""
        target_path = self._extract_clean_path(cmd_line)

        # --- 第三戰區：幽靈判定 ---
        if not target_path:
            return {
                "verdict": "🔥 CRITICAL: GHOST PROCESS",
                "score": 100,
                "reasons": ["日誌有啟動紀錄但磁碟找不到實體檔案"],
                "target": cmd_line
            }

        # --- 啟動專家連動分析 ---
        # 這裡為了展示邏輯，我們手動獲取數據 (實戰中是由函式 return 出來)
        file_hash = get_file_fingerprint(target_path)
        analyze_pe_structure(target_path)
        # 假設 YARA 掃描發現了東西
        yara_result = run_yara_genetic_scan(target_path)

        # 決策引擎計分
        # (這裡暫用模擬數據，之後我們會重構 Day 6 讓它直接 return 數據)
        mock_results = {"yara_hit": False, "compile_year": 2026}
        score, reasons = self._evaluate_threat(mock_results)

        return {
            "verdict": "ANALYSIS_COMPLETE",
            "score": score,
            "reasons": reasons,
            "hash": file_hash,
            "target": target_path
        }


# --- [ 執行單元：貼身警衛模式 ] ---
if __name__ == "__main__":
    commander = SphinxOrchestrator()

    # 模擬三種日誌場景
    scenarios = [
        f'"{sys.executable}" --safe',  # 場景 1：合法 Python 執行
        'C:\\Temp\\unknown_malware.exe -p 443'  # 場景 2：幽靈程序 (路徑不存在)
    ]

    print("\n" + "=" * 70)
    print("🛡️  Project Sphinx Day 7：自動化連動引擎啟動")
    print("=" * 70)

    for i, mock_cmd in enumerate(scenarios):
        print(f"\n[*] [事件 #{i + 1}] 偵測到日誌異動，正在同步鑑定...")
        report = commander.run_hunt(mock_cmd)

        # 決策執行：根據分數決定是否觸發「緊急應變」
        if report["score"] >= 15 or "GHOST" in report["verdict"]:
            print(f"🚨 [!!! 威脅警報 !!!]")
            print(f"    - 威脅分數: {report['score']}")
            print(f"    - 判定原因: {report['reasons']}")
            print(f"    - 處置建議: 立即隔離該端點並採集記憶體鏡像")
        else:
            print(f"✅ [鑑定結果: 安全] 檔案指紋已存入信任白名單")

        time.sleep(2)