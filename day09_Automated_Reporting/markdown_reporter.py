import os
import json
from datetime import datetime


class SphinxReporter:
    def __init__(self):
        # 這是報告的骨架 (模板)
        self.report_template = """# 🛡️ Project Sphinx：全維度取證鑑定報告
> **報告編號：{report_id}**
> **生成時間：{timestamp}**

---

## 1. 威脅综觀 (Executive Summary)
- **鑑定目標**：`{target_file}`
- **威脅判定**：{verdict}
- **混淆層級**：發現 {layer_count} 層加密嵌套
- **最後意圖**：`{final_intent}`

## 2. 全球威脅情資 (Global Intelligence)
{intel_section}

## 3. 深度分析細節 (Technical Analysis)
系統已自動執行遞迴拆解，以下為證據鏈還原路徑：

{extraction_table}

## 4. MITRE ATT&CK 映射
| 技法編號 | 技法名稱 | 描述 |
| :--- | :--- | :--- |
| T1059.001 | PowerShell | 執行隱蔽腳本 |
| T1027 | Obfuscated Files | 透過多層編碼規避偵測 |

## 5. 處置建議 (Recommendations)
1. **立即隔離**：建議暫時切斷目標主機的網路連線。
2. **深度掃描**：對磁碟執行全盤 YARA 掃描，確認有無持久化後門。

---
*本報告由 C2-Traffic-Sentinel 自動化引擎生成*
"""

    def generate_table(self, steps):
        """將步驟轉為 Markdown 表格"""
        table = "| 層級 | 還原內容 (明文) | 風險評估 |\n| :--- | :--- | :--- |"
        for step in steps:
            content = (step['content'][:70] + "..") if len(step['content']) > 70 else step['content']
            table += f"\n| {step['layer']} | `{content}` | {step.get('risk', 'High')} |"
        return table

    def _format_intel(self, vt_data):
        """處理雲端情報顯示邏輯"""
        if not vt_data or vt_data.get('status') == 'unknown':
            return "> *提示：此檔案尚未在全球威脅智庫中有紀錄。*"

        return f"""
| 鑑定維度 | 數據結果 |
| :--- | :--- |
| **國際引擎判定 (Malicious)** | {vt_data.get('malicious', 0)} / 75 |
| **可疑指標 (Suspicious)** | {vt_data.get('suspicious', 0)} |
| **全球報告連結** | [點此查看詳細鑑定]({vt_data.get('link', '#')}) |
"""

    def create_report(self, json_data, filename=None):
        """將數據填入模板並存檔"""
        data = json.loads(json_data)

        # 1. 準備所有的填空資料 (確保這裡的 key 跟模板完全對齊)
        # 這些變數必須跟 self.report_template 裡的大括號名稱一模一樣
        report_vars = {
            "report_id": datetime.now().strftime("%Y%m%d-%H%M%S"),
            "timestamp": data.get('timestamp', datetime.now().isoformat()),
            "target_file": os.path.basename(data['extraction_steps'][0]['content'].split()[0]) if data.get(
                'extraction_steps') else "Unknown",
            "verdict": "🛑 CRITICAL" if data.get('summary', {}).get('is_multi_stage') else "⚠️ SUSPICIOUS",
            "layer_count": data.get('summary', {}).get('layers_unwrapped', 0),
            "final_intent": data.get('final_payload', 'None'),
            "intel_section": self._format_intel(data.get('cloud_intelligence')),  # 處理雲端情報
            "extraction_table": self.generate_table(data.get('extraction_steps', []))
        }

        # 2. 執行填空
        report_content = self.report_template.format(**report_vars)

        # 3. 處理路徑
        ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        REPORTS_DIR = os.path.join(ROOT_DIR, "reports")
        os.makedirs(REPORTS_DIR, exist_ok=True)

        if filename is None:
            filename = f"Forensic_Report_{datetime.now().strftime('%H%M%S')}.md"

        output_path = os.path.join(REPORTS_DIR, filename)

        # 4. 寫入檔案
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(report_content)

        return output_path