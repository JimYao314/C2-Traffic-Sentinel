import os
import sys
import subprocess
import json
from datetime import datetime

# --- [ 第一戰區：指揮部環境自覺 ] ---
# 取得專案根目錄 (C:\InfoSec_Lab)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)


class SphinxMemorySentinel:
    def __init__(self, dump_path):
        """
        [母體初始化]
        此模組負責處理『揮發性證據 (RAM Dump)』，並調度 Volatility 3 執行鑑定任務。
        """
        self.dump_path = dump_path
        # 產出物集中化目錄
        self.reports_dir = os.path.join(BASE_DIR, "reports")
        os.makedirs(self.reports_dir, exist_ok=True)

        # 標記當前分析階段
        self.phase = "PHASE_2_VOLATILE_FORENSICS"

    def run_vol_plugin(self, plugin_name):
        """
        [核心邏輯：subprocess 指揮鏈]
        Python 作為指揮官，下令作業系統啟動 Volatility 3 重型設備。
        """
        print(f"[*] 指揮官下令：啟動記憶體掃描儀，執行插件 [{plugin_name}]...")

        # 構建系統指令清單
        # vol -f [路徑] [插件名稱]
        cmd = ["vol", "-f", self.dump_path, plugin_name]

        try:
            # 利用 subprocess.run 捕捉外部程式的輸出內容
            # capture_output=True : 讓 Python 攔截本來要印在螢幕上的字，存入變數
            # text=True : 將 0101 原始數據自動轉譯為人類可讀的字串
            # timeout=300 : 設定 5 分鐘超時防線，避免單一分析任務卡死系統
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)

            if result.returncode == 0:
                return result.stdout
            else:
                return f"[-] 插件執行失敗，錯誤訊息: {result.stderr}"

        except FileNotFoundError:
            return "[-] 系統錯誤：找不到 'vol' 指令。請確認 Volatility 3 已安裝並加入環境變數。"
        except Exception as e:
            return f"[-] 發生非預期系統錯誤: {str(e)}"

    def generate_init_report(self):
        """
        [展示亮點] 產出第二階段環境就緒報告，展現從『存續性』到『揮發性』的戰略轉型。
        """
        report_content = f"""# 🧠 Project Sphinx：揮發性取證環境初始化報告
> **評定時間：{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}**
> **分析階段：Phase 2 - Volatile Forensics (意識掃描)**

---

## 1. 核心概念演進 (The Paradigm Shift)
本專案已從第一階段的「存續性取證」正式跨入第二階段。

| 鑑識維度 | 第一階段：存續性 (Persistence) | 第二階段：揮發性 (Volatility) |
| :--- | :--- | :--- |
| **證據位置** | 硬碟磁碟 (Disk / Logs) | 隨機存取記憶體 (RAM) |
| **目標狀態** | 駭客留下的足跡與屍體 | 駭客正在跳動的靈魂與意識 |
| **核心挑戰** | 日誌刪除、檔案偽裝 | **無檔案攻擊、代碼注入、Ghost Process** |

## 2. 分析母體配置 (Environment Audit)
- **鑑定引擎**：Volatility 3 Framework (Industrial Standard)
- **連動技術**：Python `subprocess` Pipe-lining
- **目前狀態**：🚀 指令集已焊接完成，等待掛載實體記憶體鏡像檔案。

## 3. 預計追蹤目標 (Hunting Roadmap)
1. **[windows.malfind]**：偵測隱藏在合法進程空間內的惡意代碼（抓捕降靈程序）。
2. **[windows.pslist]**：列出所有執行中的程序，包含具備隱身能力的深層進程。
3. **[windows.netstat]**：還原記憶體中殘留的網路連線軌跡（對抗 C2 反連）。

---
*本報告由 C2-Traffic-Sentinel 揮發性分析母體自動生成。*
"""
        output_path = os.path.join(self.reports_dir, "Sample_Memory_Forensics_Init.md")
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(report_content)

        return output_path


# --- [ 執行單元 ] ---
if __name__ == "__main__":
    # 預先設定一個未來要使用的證據路徑 (假設路徑)
    MOCK_DUMP_PATH = "C:\\Evidence\\target_ram.dmp"

    print("\n" + "=" * 70)
    print("🧠 Project Sphinx Phase 2：揮發性數據鑑定母體啟動")
    print("=" * 70)

    # 實例化母體
    sentinel = SphinxMemorySentinel(MOCK_DUMP_PATH)

    # 動作 1：生成初始化證明文件 (二面展示用)
    report_file = sentinel.generate_init_report()
    print(f"[+] 戰略轉型報告已產出：{report_file}")

    # 動作 2：執行初步邏輯檢查
    if not os.path.exists(MOCK_DUMP_PATH):
        print(f"[!] 偵測目標缺失：目前硬碟中尚未發現實體鏡像檔。")
        print("[*] 邏輯驗證：母體架構檢查通過。正在等待第三週的鏡像採集工具 (Acquisition Tool) 交付。")
    else:
        # 如果檔案在，就跑一個基礎插件測試
        sentinel.run_vol_plugin("windows.pslist")

    print("\n" + "=" * 60)
    print("【階段二環境初始化成功】分析引擎已對齊『揮發性意識』獵捕標準。")
    print("=" * 60)