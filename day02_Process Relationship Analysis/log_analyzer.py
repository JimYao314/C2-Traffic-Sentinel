import os
import pandas as pd
from lxml import etree  # 你清單中已有的強大解析庫

# --- [1. 導入 python-evtx] ---
try:
    import Evtx.Evtx as evtx_parser

    print("[+] 成功啟動 python-evtx 穩定版引擎！")
except ImportError:
    print("[-] 報錯：環境中找不到 python-evtx。")
    import sys

    sys.exit(1)


def parse_evtx_to_list(evtx_path):
    event_list = []
    print(f"[*] 正在分析證物: {evtx_path}")

    # 定義 Windows 事件日誌的 XML 命名空間 (Namespace)
    ns = {'ns': 'http://schemas.microsoft.com/win/2004/08/events/event'}

    try:
        with evtx_parser.Evtx(evtx_path) as log:
            for i, record in enumerate(log.records()):
                if i >= 1000: break  # 掃描 1000 筆紀錄

                # 取得原始 XML 字串
                xml_str = record.xml()
                # 使用 lxml 解析 XML
                root = etree.fromstring(xml_str.encode('utf-8'))

                # 提取 EventID (路徑: System -> EventID)
                event_id_element = root.xpath('//ns:EventID', namespaces=ns)
                event_id = int(event_id_element[0].text) if event_id_element else 0

                # 提取 時間 (路徑: System -> TimeCreated -> SystemTime)
                time_element = root.xpath('//ns:TimeCreated', namespaces=ns)
                timestamp = time_element[0].get('SystemTime') if time_element else "Unknown"

                # 提取完整數據 (用於後續關鍵字搜尋)
                event_list.append({
                    "EventID": event_id,
                    "Time": timestamp,
                    "RawXML": xml_str  # 保存原始數據
                })
        return event_list
    except Exception as e:
        print(f"[-] 解析過程發生錯誤: {e}")
        return []


if __name__ == "__main__":
    # 自動定位同資料夾下的 Security.evtx
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    EVTX_FILE = os.path.join(BASE_DIR, "Security.evtx")

    # 1. 執行解析
    raw_data = parse_evtx_to_list(EVTX_FILE)

    if raw_data:
        df = pd.DataFrame(raw_data)

        # 2. 獵捕：篩選 4688 (新程序建立)
        process_events = df[df['EventID'] == 4624]

        print("\n" + "=" * 60)
        print(f"【 獵捕報告：發現 {len(process_events)} 筆登入紀錄 】")
        print("=" * 60)

        if not process_events.empty:
            # 顯示時間與 ID
            print(process_events[['Time', 'EventID']].head(10))

            # --- [額外獵捕：搜尋惡意關鍵字] ---
            threat_keywords = ["powershell", "whoami", "mimikatz", "cmd.exe"]
            print("\n[*] 正在掃描惡意關鍵字特徵...")
            for kw in threat_keywords:
                matches = process_events[process_events['RawXML'].str.contains(kw, case=False)]
                if not matches.empty:
                    print(f"[!] 發現疑似威脅使用 {kw}: {len(matches)} 筆")
        else:
            print("[INFO] 本次分析範圍內沒有 4688 紀錄。")
            print(f"[DEBUG] 擷取到的 EventID 範例: {df['EventID'].unique()[:5]}")
    else:
        print("[-] 解析失敗，請確認 Security.evtx 是否在正確路徑。")