import os
import json
from datetime import datetime


class SphinxReporter:
    def __init__(self):
        self.report_template = """# 🛡️ Project Sphinx：數位取證鑑定報告
> **報告編號：{report_id}**
> **生成時間：{timestamp}**

---

## 1. 威脅综觀 (Executive Summary)
- **鑑定目標**：{target_file}
- **威脅判定**：{verdict}
- **混淆層級**：發現 {layer_count} 層加密嵌套
    - **最後意圖**：`{final_intent}`

## 2. 深度分析細節 (Technical Analysis)
系統已自動執行遞迴拆解，以下為證據鏈還原路徑：

{extraction_table}

## 3. MITRE ATT&CK 框架映射
| 技法編號 | 技法名稱 | 描述 |
| :--- | :--- | :--- |
| T1059.001 | PowerShell | 攻擊者利用 PowerShell 執行惡意代碼。 |
| T1027 | Obfuscated Files | 透過 Base64 進行多層混淆以規避偵測。 |

## 4. 處置建議 (Recommendations)
1. **立即隔離**：建議暫時切斷主機 {target_file} 的網路連線。
2. **記憶體採樣**：由於涉及混淆指令，建議進行動態記憶體傾印 (Memory Dump) 以追蹤注入行為。
3. **路徑清理**：刪除相關持久化註冊表鍵值。

---
*本報告由 C2-Traffic-Sentinel 自動化引擎生成，具備法律證據初步參考價值。*
"""

    def generate_table(self, steps):
        """將 JSON 裡的 steps 清單轉化為 Markdown 表格"""
        table = "| 層級 | 還原內容 (明文) | 風險評估 |\n| :--- | :--- | :--- |"
        for step in steps:
            # 簡化顯示，避免內容過長
            content = step['content'][:80] + "..." if len(step['content']) > 80 else step['content']
            table += f"\n| {step['layer']} | `{content}` | {step['risk']} |"
        return table

    def create_report(self, json_data):
        """核心邏輯：將 JSON 轉化為 MD 檔案"""
        data = json.loads(json_data)

        # 準備填充資料
        report_content = self.report_template.format(
            report_id=datetime.now().strftime("%Y%m%d-%H%M%S"),
            timestamp=data['timestamp'],
            target_file=os.path.basename(data['extraction_steps'][0]['content'].split()[0]),  # 嘗試猜測檔案名
            verdict="🛑 CRITICAL" if data['summary']['is_multi_stage'] else "⚠️ SUSPICIOUS",
            layer_count=data['summary']['layers_unwrapped'],
            final_intent=data['final_payload'],
            extraction_table=self.generate_table(data['extraction_steps'])
        )

        # 寫入檔案
        filename = f"Forensic_Report_{datetime.now().strftime('%H%M%S')}.md"
        output_path = os.path.join(os.path.dirname(__file__), filename)

        with open(output_path, "w", encoding="utf-8") as f:
            f.write(report_content)

        return output_path


if __name__ == "__main__":
    # --- [ 零件連動：獲取 Day 8 的結果 ] ---
    import sys

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.append(BASE_DIR)

    try:
        from day8_Advanced_Data_Mining.advanced_deobfuscator import RecursiveDeobfuscator

        # 1. 模擬獲取數據 (Call Day 8)
        mock_cmd = "powershell -enc JABhAD0AJwB3AGgAbwBhAG0AaQAnADsAcABvAHcAZQByAHMAaABlAGwAbAAuAGUAeABlACAALQBlAG4AYwAgAGQAdwBCAG8AQQBHADgAQQBZAFEAQgB0AEEARwBrAEEA"
        engine = RecursiveDeobfuscator()
        final_intent = engine.deep_scan(mock_cmd)
        json_res = engine.export_json_report(mock_cmd, final_intent)

        # 2. 執行報告生成 (Call Day 9)
        reporter = SphinxReporter()
        report_path = reporter.create_report(json_res)

        print(f"[+] 報告生成成功！檔案位於：\n{report_path}")
        print("[*] 請使用 Markdown 編輯器 (或 PyCharm 預覽) 查看報告效果。")

    except ImportError:
        print("[-] 請確保 day8 的 __init__.py 與資料夾名稱正確。")