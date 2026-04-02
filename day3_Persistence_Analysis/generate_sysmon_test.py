import os


def create_fake_sysmon_log():
    # 修正後的 XML，確保標籤完全閉合
    fake_xml = """<Event xmlns='http://schemas.microsoft.com/win/2004/08/events/event'>
    <System>
        <Provider Name='Microsoft-Windows-Sysmon' Guid='{5770385F-C22A-43E0-BF4C-06F5698FFBD9}'/>
        <EventID>13</EventID>
        <TimeCreated SystemTime='2026-04-02T09:30:00.123456Z'/>
    </System>
    <EventData>
        <Data Name='Image'>C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe</Data>
        <Data Name='TargetObject'>HKLM\\Software\\Microsoft\\Windows\\CurrentVersion\\Run\\MalwareUpdate</Data>
        <Data Name='Details'>C:\\Users\\Public\\malware.ps1</Data>
    </EventData>
</Event>"""

    # 獲取目前路徑，確保檔案存在正確位置
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(BASE_DIR, "sysmon_test_data.xml")

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(fake_xml)
    print(f"[+] 模擬攻擊數據已修正並產出：{file_path}")


if __name__ == "__main__":
    create_fake_sysmon_log()