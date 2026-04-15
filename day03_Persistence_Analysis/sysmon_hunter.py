import os
from lxml import etree
import pandas as pd


class SysmonPersistenceHunter:
    def __init__(self, xml_path):
        self.xml_path = xml_path
        self.ns = {'ns': 'http://schemas.microsoft.com/win/2004/08/events/event'}

    def hunt(self):
        findings = []
        print(f"[*] 正在掃描 Sysmon 證據檔案...")

        try:
            # 解析我們剛才產出的 XML
            tree = etree.parse(self.xml_path)
            root = tree.getroot()

            # 尋找 EventID 13 (註冊表數值設定)
            event_id = int(root.xpath("//ns:EventID", namespaces=self.ns)[0].text)

            if event_id == 13:
                # 提取關鍵欄位
                image = root.xpath("//ns:Data[@Name='Image']", namespaces=self.ns)[0].text
                target = root.xpath("//ns:Data[@Name='TargetObject']", namespaces=self.ns)[0].text
                time = root.xpath("//ns:TimeCreated", namespaces=self.ns)[0].get('SystemTime')

                # 判斷邏輯：是否修改了自動啟動路徑 (Run Key)
                if "currentversion\\run" in target.lower():
                    findings.append({
                        "Time": time,
                        "Verdict": "🔥 CRITICAL: PERSISTENCE DETECTED",
                        "Attacker_Tool": image,
                        "Infected_Registry": target
                    })
            return findings
        except Exception as e:
            print(f"[-] 偵測過程發生錯誤: {e}")
            return []


if __name__ == "__main__":
    # 指向剛才產生的模擬檔
    TEST_FILE = os.path.join(os.path.dirname(__file__), "sysmon_test_data.xml")

    hunter = SysmonPersistenceHunter(TEST_FILE)
    results = hunter.hunt()

    if results:
        print("\n" + "=" * 70)
        print("【 Project Sphinx：Day 3 獵捕報告 】")
        print("=" * 70)
        df = pd.DataFrame(results)
        print(df.to_string(index=False))
        print("\n[!] 建議行動：立即檢查該註冊表鍵值，並隔離發起該動作的端點主機。")
    else:
        print("\n[OK] 未發現異常。")