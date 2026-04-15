import os
import sys
import time
import json
from datetime import datetime

# --- [ 第一戰區：指揮部路徑打通 ] ---
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)

# 導入 Day 8 的進階遞迴解碼引擎
try:
    from day8_Advanced_Data_Mining.advanced_deobfuscator import RecursiveDeobfuscator
    import Evtx.Evtx as evtx_parser
    from lxml import etree

    print("[+] 成功串聯跨模組工具：進階遞迴引擎與 EVTX 解析器已就緒。")
except ImportError as e:
    print(f"[-] 導入錯誤: {e}。請確保各資料夾內有 __init__.py 且執行過 pip install。")
    sys.exit(1)


# --- [ 第二、三戰區：串流獵捕引擎類別 ] ---
class SphinxStreamingSentinel:
    def __init__(self, evtx_path):
        self.evtx_path = evtx_path
        self.ns = {'ns': 'http://schemas.microsoft.com/win/2004/08/events/event'}
        self.deobfuscator = RecursiveDeobfuscator()  # 徵調 Day 8 專家
        self.total_records_scanned = 0

    def hunt_stream(self):
        """
        核心邏輯：Generator 串流模式
        底層運作：一邊讀取二進位流，一邊吐出威脅數據，保持記憶體恆定。
        """
        if not os.path.exists(self.evtx_path):
            return

        with evtx_parser.Evtx(self.evtx_path) as log:
            for record in log.records():
                self.total_records_scanned += 1

                # 每 5000 筆印一次小進度，避免螢幕太空白
                if self.total_records_scanned % 1000 == 0:
                    print(f"[*] 系統巡邏中... 已檢查 {self.total_records_scanned} 筆日誌")

                try:
                    # 解析 XML 結構
                    root = etree.fromstring(record.xml().encode('utf-8'))
                    event_id = int(root.xpath('//ns:EventID', namespaces=self.ns)[0].text)

                    # 鎖定 4688 程序建立事件
                    if event_id == 4688:
                        cmd_elements = root.xpath("//ns:Data[@Name='CommandLine']", namespaces=self.ns)
                        if cmd_elements and cmd_elements[0].text:
                            raw_cmd = cmd_elements[0].text

                            # [連動 Day 8] 執行遞迴剝洋蔥解碼
                            final_intent = self.deobfuscator.deep_scan(raw_cmd)

                            # 如果發現了至少一層混淆特徵
                            if len(self.deobfuscator.history) > 0:
                                timestamp = root.xpath('//ns:TimeCreated', namespaces=self.ns)[0].get('SystemTime')

                                finding = {
                                    "time": timestamp,
                                    "original": raw_cmd[:60] + "...",
                                    "decoded_intent": final_intent,
                                    "layers": len(self.deobfuscator.history)
                                }
                                # 回報前清空解碼器歷史，準備處理下一條
                                self.deobfuscator.history = []

                                # [核心動作] 像水龍頭一樣滴出結果
                                yield finding
                except Exception:
                    continue


# --- [ 第四戰區：決策中心與效能統計 ] ---
if __name__ == "__main__":
    # 指定 Day 2 的原始日誌檔案
    TARGET_LOG = os.path.join(BASE_DIR, "day2_Process Relationship Analysis", "Security.evtx")

    sentinel = SphinxStreamingSentinel(TARGET_LOG)

    print("\n" + "=" * 70)
    print(f"🛡️  Project Sphinx Day 10：大數據串流分析 (Performance Monitoring)")
    print("=" * 70)

    # 開始計時
    start_time = time.time()

    threat_found = False
    # 這裡就是管線末端：接收 yield 吐出的數據
    for alert in sentinel.hunt_stream():
        threat_found = True
        print(f"\n[!] 🚨 偵測到嚴重威脅！")
        print(f"    時間: {alert['time']}")
        print(f"    解密意圖: {alert['decoded_intent']}")
        print(f"    混淆層級: {alert['layers']} 層")

        # 姚競的『即刻叫停』邏輯：實戰中發現第一個 C2 啟動就必須立刻介入
        print("\n[判定]：威脅確鑿。啟動緊急處置中斷程序...")
        break

        # 結束計時
    end_time = time.time()
    duration = end_time - start_time

    # --- 產出公信力數據報告 ---
    print("\n" + "-" * 70)
    print(f"📊 效能基準測試總結 (Benchmark Report)")
    print(f"[*] 掃描總筆數 : {sentinel.total_records_scanned} 筆")
    print(f"[*] 總運算耗時 : {duration:.4f} 秒")

    # 避免除以零的錯誤
    if duration > 0:
        print(f"[*] 平均解析速率 : {sentinel.total_records_scanned / duration:.0f} 筆/秒")

    print(f"[*] 記憶體模式 : Generator-Stream (O(1) Memory Usage)")
    print("-" * 70)

    if not threat_found:
        print("[OK] 掃描範圍內未發現惡意混淆指令。環境健康。")