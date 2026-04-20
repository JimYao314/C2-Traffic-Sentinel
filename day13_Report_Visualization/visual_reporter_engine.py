import os
import sys
import json
import shutil
from datetime import datetime

# --- [ 第一戰區：指揮部導航 ] ---
# 取得專案根目錄 (C:\InfoSec_Lab)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)


class SphinxVisualReporter:
    def __init__(self):
        # 設定報告產出的總目錄
        self.reports_dir = os.path.join(BASE_DIR, "reports")
        os.makedirs(self.reports_dir, exist_ok=True)

        # 設定 Day 13 專屬的歷史檔案室
        self.day13_records = os.path.join(os.path.dirname(os.path.abspath(__file__)), "records")
        os.makedirs(self.day13_records, exist_ok=True)

    def _get_status_color(self, score):
        """[視覺邏輯] 根據威脅數值返回 HTML 顏色標籤"""
        if score >= 10: return "red", "🛑 CRITICAL (極高風險)"
        if 1 <= score < 10: return "orange", "⚠️ SUSPICIOUS (中度疑似)"
        return "green", "✅ CLEAN (環境安全)"

    def _build_collapsible_section(self, steps):
        """[排版邏輯] 實作 HTML 摺疊語法，隱藏繁瑣的解碼路徑"""
        if not steps: return "> *此指令無混淆特徵。*"

        html = f"<details>\n<summary><b>🔍 點擊展開深度還原路徑 (共 {len(steps)} 層拆解)</b></summary>\n\n"
        html += "| 層級 | 還原內容片段 | 風險評估 |\n| :--- | :--- | :--- |\n"
        for s in steps:
            # 截斷過長的內容，保持表格整齊
            content = (s['content'][:60] + "...") if len(s['content']) > 60 else s['content']
            html += f"| {s['layer']} | `{content}` | {s.get('risk', 'High')} |\n"
        html += "\n</details>"
        return html

    def render(self, input_json_path):
        """
        核心渲染引擎：讀取融合情資 JSON 並產出高級 Markdown 報告
        """
        if not os.path.exists(input_json_path):
            print(f"[-] 錯誤：找不到數據源 {input_json_path}")
            return None

        # 1. 讀取數據
        with open(input_json_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        # 2. 數據清洗與變量提取
        vt_stats = data.get('cloud_intelligence', {})
        malicious = vt_stats.get('malicious', 0) if isinstance(vt_stats, dict) else 0
        color, label = self._get_status_color(malicious)

        # 3. 準備處置建議 (Decision Logic)
        advice = "建議立即執行 Enforcer 隔離程序並封鎖相關 IP。" if malicious > 5 else "目前威脅程度尚低，建議持續監控異常行為。"

        # --- [ 4. 構建高級 Markdown 內容 ] ---
        report_md = f"""# 🛡️ Project Sphinx：高級取證鑑定報告 (v2.0)
> **系統自動生成於：{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}**
> **數據版本：Intelligence Fusion v1.2**

---

## 1. 核心判定 (Core Verdict)
### <font color='{color}'>{label}</font>

| 關鍵指標 | 數據結果 | 說明 |
| :--- | :--- | :--- |
| **國際引擎警報** | **{malicious} / 75** | 來自全球威脅智庫 VirusTotal |
| **自動解碼層級** | {data['summary']['layers_unwrapped']} 層 | 遞迴解碼引擎分析深度 |
| **最終意圖識別** | `{data['final_payload']}` | 去混淆後還原的原始指令 |

---

## 2. 深度取證細節 (Technical Evidence)
### 🕵️ 攻擊鏈還原
{self._build_collapsible_section(data.get('extraction_steps', []))}

### 🌐 雲端情資關聯
- **通緝令詳細連結**：[點此檢閱 VirusTotal 完整分析紀錄]({vt_stats.get('link', '#') if isinstance(vt_stats, dict) else '#'})
- **情資狀態**：{"✅ 已確認威脅" if malicious > 0 else "ℹ️ 全球查無已知惡意特徵"}

---

## 3. 應變處置建議 (Actionable Intelligence)
1. **緊急動作**：{advice}
2. **防禦加固**：針對 `{data['final_payload']}` 涉及的 API 調用進行系統級審核。
3. **證據留存**：本報告已同步存檔至本地歷史案卷庫，具備法理存證價值。

---
<p align="right">分析師簽章：<b>Sphinx Automated Engine</b></p>
"""
        # --- [ 5. 執行雙重存檔機制 ] ---

        # A. 產出『展示版』(會被複寫，供 GitHub README 連結使用)
        display_file = "Sample_Enriched_Forensic_Report.md"
        display_path = os.path.join(self.reports_dir, display_file)
        with open(display_path, "w", encoding="utf-8") as f:
            f.write(report_md)

        # B. 產出『歷史存檔版』(存入 day13/records，永久保留)
        archive_name = f"V2_Archive_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
        archive_path = os.path.join(self.day13_records, archive_name)
        shutil.copy2(display_path, archive_path)  # 利用 shutil 進行精確拷貝

        return display_path, archive_path


if __name__ == "__main__":
    # 指向昨天產出的融合數據 JSON
    JSON_SOURCE = os.path.join(BASE_DIR, "reports", "Sample_Enriched_Threat_Data.json")

    print("\n" + "=" * 60)
    print("🚀 Day 13：啟動高級視覺化報告引擎 (V2.0)")
    print("=" * 60)

    engine = SphinxVisualReporter()
    paths = engine.render(JSON_SOURCE)

    if paths:
        print(f"\n[+] 報告任務執行成功！")
        print(f"[*] 展示文件已更新 : {paths[0]}")
        print(f"[*] 歷史案卷已封存 : {paths[1]}")