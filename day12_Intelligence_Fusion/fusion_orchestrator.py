import os
import sys
import json
import shutil
from datetime import datetime

# --- [ 第一戰區：指揮部導航與模組掛載 ] ---
# 定位專案總目錄 (C:\InfoSec_Lab)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)

# 導入各路專業組件 (請確保對應資料夾內有 __init__.py)
try:
    from day08_Advanced_Data_Mining.advanced_deobfuscator import RecursiveDeobfuscator
    from day09_Automated_Reporting.markdown_reporter import SphinxReporter
    from day11_Threat_Intel_Integration.vt_intel_radar import VirusTotalRadar

    print("[+] 總部通訊網建立完成：本地解碼、雲端雷達、報告引擎已就緒。")
except ImportError as e:
    print(f"[-] 指揮鏈斷裂：無法導入模組。錯誤詳情: {e}")
    sys.exit(1)


# --- [ 第二戰區：情報融合指揮官 ] ---
class SphinxFusionCommander:
    def __init__(self):
        self.deobfuscator = RecursiveDeobfuscator()
        self.radar = VirusTotalRadar()
        self.reporter = SphinxReporter()

    def run_full_analysis(self, raw_command, file_hash):
        """
        執行全自動獵捕流程：從日誌到鑑定書的一條龍管線
        """
        print(f"\n[*] 啟動【里程碑五】全維度連動獵捕管線...")

        # 1. 本地遞迴解碼分析 (來自 Day 08)
        print("[1/4] 本地模組：正在剝除多層混淆外殼...")
        decoded_intent = self.deobfuscator.deep_scan(raw_command)
        local_data_json = self.deobfuscator.export_json_report(raw_command, decoded_intent)
        local_data = json.loads(local_data_json)

        # 2. 雲端情資連動 (來自 Day 11)
        print("[2/4] 雲端模組：正在向全球智庫連線查詢指紋...")
        cloud_intel = self.radar.query_hash(file_hash)

        # 3. 數據中樞融合 (Intelligence Fusion)
        print("[3/4] 指揮中樞：正在進行本地與雲端數據融合...")
        local_data['cloud_intelligence'] = cloud_intel

        # 產出融合後的範例 JSON 供 GitHub 展示
        REPORTS_DIR = os.path.join(BASE_DIR, "reports")
        os.makedirs(REPORTS_DIR, exist_ok=True)
        with open(os.path.join(REPORTS_DIR, "Sample_Enriched_Threat_Data.json"), "w", encoding="utf-8") as f:
            json.dump(local_data, f, indent=4, ensure_ascii=False)

        # 4. 自動化報告產出與存檔管理 (來自 Day 09 改版)
        print("[4/4] 報告模組：產出最終鑑定鑑定書並執行分類存檔...")

        # A. 產出『展示版』：供 GitHub 連結使用 (會被複寫)
        display_name = "Sample_Enriched_Forensic_Report.md"
        display_path = self.reporter.create_report(json.dumps(local_data), filename=display_name)

        # B. 產出『歷史存檔版』：存入 day12/records (不會被複寫)
        DAY12_RECORDS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "records")
        os.makedirs(DAY12_RECORDS, exist_ok=True)

        archive_name = f"Archive_Report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
        # 直接利用 shutil 進行物理複製，這是最穩健的做法
        archive_path = os.path.join(DAY12_RECORDS, archive_name)
        shutil.copy2(display_path, archive_path)

        return display_path, archive_path


# --- [ 實戰執行單元 ] ---
if __name__ == "__main__":
    commander = SphinxFusionCommander()

    # 模擬場景：捕獲到具備 Base64 多層混淆的 EICAR 病毒測試指令
    MOCK_RAW_CMD = "powershell.exe -enc dABoAG8AYQBtAGkALwBhAGwAbAA="
    MOCK_HASH = "275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f"

    print("\n" + "=" * 70)
    print("🛡️  C2-Traffic-Sentinel | Intelligence Fusion System v1.0")
    print("=" * 70)

    # 啟動總指揮
    display_file, archive_file = commander.run_full_analysis(MOCK_RAW_CMD, MOCK_HASH)

    print("\n" + "-" * 70)
    print(f"✅ 【任務達成】全維度鑑定流程圓滿結束")
    print(f"[*] GitHub 展示路徑 : {display_file}")
    print(f"[*] 私人紀錄存檔     : {archive_file}")
    print("-" * 70)