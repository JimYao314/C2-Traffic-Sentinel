import os
import sys
import json
from datetime import datetime

# --- [ 第一戰區：指揮部環境初始化 ] ---
# 取得專案根目錄 (C:\InfoSec_Lab)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)


class SphinxDecisionBrain:
    def __init__(self):
        """
        [法典定義] 定義不同維度證據的加權分數。
        """
        self.rules = {
            "critical_vt": 50,  # 全球通緝(10家以上報警)
            "suspicious_vt": 20,  # 雲端疑似(1-9家報警)
            "recursive_obfuscation": 30,  # 發現多層嵌套對抗行為
            "malicious_intent": 25,  # 發現惡意下載/執行指令
        }
        # 開火門檻：總分超過 65 則觸發立即處置
        self.threshold = 65

    def evaluate_threat(self, fusion_json_path):
        """
        核心邏輯：執行啟發式計分，並完整紀錄審計追蹤 (Audit Trail)
        """
        if not os.path.exists(fusion_json_path):
            print(f"[-] 錯誤：找不到數據源 {fusion_json_path}")
            return None

        # 1. 讀取 Day 12 產出的融合情資
        with open(fusion_json_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        current_score = 0
        audit_trail = []

        print(f"\n[開始判定] 目標指令：{data.get('final_payload', 'Unknown')}")
        print("-" * 50)

        # --- 維度 1：全球情資審核 (來自 Day 11) ---
        vt_stats = data.get('cloud_intelligence', {})
        if isinstance(vt_stats, dict):
            malicious_count = vt_stats.get('malicious', 0)
            if malicious_count >= 10:
                points = self.rules["critical_vt"]
                current_score += points
                msg = f"[+ {points}分] 強特徵：全球智庫高度共識惡意 (報警引擎: {malicious_count}) | 累計: {current_score}"
                audit_trail.append(msg)
                print(msg)
            elif malicious_count > 0:
                points = self.rules["suspicious_vt"]
                current_score += points
                msg = f"[+ {points}分] 弱特徵：全球智庫低度疑似 (報警引擎: {malicious_count}) | 累計: {current_score}"
                audit_trail.append(msg)
                print(msg)

        # --- 維度 2：混淆深度審核 (來自 Day 08) ---
        layers = data.get('summary', {}).get('layers_unwrapped', 0)
        if layers >= 2:
            points = self.rules["recursive_obfuscation"]
            current_score += points
            msg = f"[+ {points}分] 對抗特徵：偵測到 {layers} 層遞迴混淆意圖 | 累計: {current_score}"
            audit_trail.append(msg)
            print(msg)

        # --- 維度 3：行為意圖審核 (來自 Day 04/05) ---
        intent = data.get('final_payload', "").lower()
        if any(k in intent for k in ["downloadstring", "iex", "invoke-webrequest"]):
            points = self.rules["malicious_intent"]
            current_score += points
            msg = f"[+ {points}分] 行為特徵：發現遠端載荷下載與執行特徵 | 累計: {current_score}"
            audit_trail.append(msg)
            print(msg)

        # --- 最終裁決 ---
        is_malicious = current_score >= self.threshold
        result = {
            "target": data.get('final_payload', 'Unknown'),
            "total_score": current_score,
            "is_malicious": is_malicious,
            "audit_trail": audit_trail,
            "verdict": "🛑 CRITICAL" if is_malicious else "✅ MONITOR"
        }
        return result

    def generate_audit_md(self, result, output_filename="Sample_Decision_Audit.md"):
        """
        [輸出模組] 將運算過程產出為正式的 Markdown 審計報告
        """
        REPORTS_DIR = os.path.join(BASE_DIR, "reports")
        os.makedirs(REPORTS_DIR, exist_ok=True)

        # 建立 Markdown 內容
        audit_content = f"""# ⚖️ Project Sphinx：威脅決策審計報告
> **報告編號：AUDIT-{datetime.now().strftime("%Y%m%d-%H%M%S")}**
> **評定時間：{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}**

---

## 1. 判決結論 (Final Verdict)
| 鑑定項目 | 數值 / 結果 | 說明 |
| :--- | :--- | :--- |
| **最終威脅評分** | **{result['total_score']} / 100** | 綜合權重計算之最終得分 |
| **系統判定結論** | {result['verdict']} | 基於門檻值 (65) 的分類結果 |
| **建議處置動作** | `{"IMMEDIATE_QUARANTINE" if result['is_malicious'] else "CONTINUOUS_MONITOR"}` | 指導應變團隊之下一步動作 |

---

## 2. 運算過程明細 (Calculation Audit Trail)
系統根據「啟發式計分矩陣」自動執行以下鑑定流程：

"""
        for step in result['audit_trail']:
            audit_content += f"- {step}\n"

        audit_content += f"""
---

## 3. 決策邏輯基準 (Policy Baseline)
- **判定門檻 (Threshold)**：65 分。
- **設計思維**：本系統不依賴單一情資。若雲端情資命中但本地無顯性惡意行為，系統將維持 `MONITOR` 狀態以避免誤報（False Positive）。唯有「聲譽證據」與「行為證據」達成疊加效應時，方會觸發處置程序。

---
*本報告由 C2-Traffic-Sentinel 決策大腦自動生成，紀錄具備取證審核效力。*
"""
        output_path = os.path.join(REPORTS_DIR, output_filename)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(audit_content)

        return output_path


# --- [ 執行單元 ] ---
if __name__ == "__main__":
    # 數據源：Day 12 整合產出的 JSON
    JSON_PATH = os.path.join(BASE_DIR, "reports", "Sample_Enriched_Threat_Data.json")

    # 1. 啟動計分大腦
    brain = SphinxDecisionBrain()
    print("🧠 Project Sphinx：正在運行啟發式計分管線...")

    # 2. 執行鑑定
    assessment = brain.evaluate_threat(JSON_PATH)

    if assessment:
        # 3. 產出審計報告
        saved_file = brain.generate_audit_md(assessment)

        print("-" * 50)
        print(f"✅ 【里程碑六達成】決策引擎執行完畢！")
        print(f"[*] 最終分數：{assessment['total_score']}")
        print(f"[*] 判定結論：{assessment['verdict']}")
        print(f"[*] 審計報告：{saved_file}")
        print("-" * 50)