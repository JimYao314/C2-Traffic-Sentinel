# 🛡️ C2-Traffic-Sentinel (Project Sphinx)
> **整合型 C2 威脅偵測哨兵：從網路流量到端點行為的全方位自動化獵捕、鑑定與決策應變平台**

![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)
![Security Focus](https://img.shields.io/badge/Focus-Threat%20Hunting%20%7C%20Incident%20Response-red)
![Progress](https://img.shields.io/badge/Progress-Day%2014%20%2F%2030-green)

**Project Sphinx** 是一個為期 30 天的整合性數位鑑識與事件應變 (DFIR) 平台建構計畫。專案旨在透過 Python 3.10+ 自動化處理海量資安日誌與網路流量，實作從「原始數據解析」到「自動化實時攔截」的完整防禦管線。

---

## 🚀 專案三階段戰略 (The 3-Phase Strategy)

### 🧩 第一階段：建立「偵測大腦」 (Day 01 - Day 14) - [已完工 ✅]
- **目標**：完成網路、日誌、檔案與雲端情資的模組化整合。
- **核心成果**：實作「自動決策中樞」，達成多維度威脅權重計分、全球情資連動與透明化審計報告。

### 🔍 第二階段：深挖「隱蔽藏身處」 (Day 15 - Day 21) - [即將開啟 ⏳]
- **目標**：攻克「記憶體鑑識 (Memory Forensics)」與動態行為監控。
- **核心成果**：定位 Ghost Processes 在 RAM 中的實體，識破無檔案攻擊 (Fileless Attacks)。

### ⚔️ 第三階段：啟動「執法權限」 (Day 22 - Day 30)
- **目標**：開發 **The Enforcer (執法者模組)**。
- **核心成果**：實現自動化隔離 (Firewall Block)、程序斬首 (Process Kill) 與惡意痕跡清理。

---

## 🚀 技術棧 (Tech Stack)
- **核心語言**: Python 3.10+ (Class 呼叫鏈、遞迴分析、Generator 串流、**Heuristic Scoring**)
- **分析引擎**: Scapy (Network), python-evtx (Logs), pefile & yara-python (Malware), Requests (API)
- **決策邏輯**: **加權評分權重矩陣 (Weighted Matrix)**, 決策審計追蹤 (Audit Trail)
- **報告視覺化**: HTML-in-Markdown, 產出物集中化管理 (Artifact Management)
- **數據處理**: Pandas, JSON Serialization, Performance Benchmarking

---

## 📊 產出範例 (Sample Output)
根據專案開發時序產出之核心物證：

1. [⚡ 大數據掃描效能基準報告 (33,142 筆)](./reports/PERFORMANCE_LOG.md) —— `Day 10 效能驗證`
2. [🧬 融合型情資數據樣本 (JSON)](./reports/Sample_Enriched_Threat_Data.json) —— `Day 12 數據融合`
3. [📈 全維度視覺化鑑定報告樣板 (V2.0)](./reports/Sample_Enriched_Forensic_Report.md) —— `Day 13 視覺呈現`
4. [⚖️ 威脅決策審計報告樣板 (計分過程)](./reports/Sample_Decision_Audit.md) —— `Day 14 最終決議`

---

## 📅 30 天獵捕日誌 (The Hunting Log)

| 天數 | 主題 | 核心產出 | 關鍵技術點 |
| :--- | :--- | :--- | :--- |
| **Day 01-04** | 偵測零件開發 | `main.py`, `deobfuscator.py` | Scapy 流量分析、Base64/UTF-16LE 解碼 |
| **Day 05** | 里程碑 I | `integrated_hunter.py` | **首個整合里程碑：** 掃描即還原自動化 |
| **Day 07** | 里程碑 II | `auto_correlation_hunter.py` | **第二個整合里程碑：** 事件驅動管線、Ghost Process 偵測 |
| **Day 10** | 里程碑 III | `streaming_orchestrator.py` | **第三個整合里程碑：** $O(1)$ 記憶體串流引擎、204 EPS 實測 |
| **Day 11** | 里程碑 IV | `vt_intel_radar.py` | **第四個整合里程碑：** 全球威脅情資 VirusTotal API 連動 |
| **Day 12** | 里程碑 V | `fusion_orchestrator.py` | **第五個整合里程碑：** 跨模組情報融合與數據中樞化 |
| **Day 13** | 高級視覺化 | `visual_reporter_engine.py` | V2.0 報告引擎、條件渲染標籤、自動化案卷管理 |
| **Day 14** | 里程碑 VI | `decision_engine.py` | **第六個整合里程碑：** 啟發式威脅評分矩陣指揮部落成 |

---

### 🗓️ 開發實況紀錄 (Dev Log)

#### **第一階段：偵測大腦與自動化管線 (Phase 1 Complete)**
- [x] **Day 01-04**: 完成基礎分析零件，實作心跳行為統計與 PowerShell 去混淆。
- [x] **Day 05**: 達成 $\color{#E1AD01}{\text{首個整合里程碑}}$。實現日誌掃描與指令還原的自動化連動。
- [x] **Day 06**: 實作靜態鑑定模組。不執行檔案即可透過 Hashing、PE 結構與 YARA 規則識別惡意基因。
- [x] **Day 07**: 達成 $\color{#E1AD01}{\text{第二個整合里程碑}}$。解決 Ghost Process 反鑑識對抗，建立閃電取證管線。
- [x] **Day 10**: 達成 $\color{#E1AD01}{\text{第三個整合里程碑}}$。實作串流解析引擎，通過 33,142 筆真實日誌壓力測試。
- [x] **Day 11**: 達成 $\color{#E1AD01}{\text{第四個整合里程碑}}$。成功對接 VirusTotal API，實作 Secrets 隔離管理。
- [x] **Day 12**: 達成 $\color{#E1AD01}{\text{第五個整合里程碑}}$。實作 **Intelligence Fusion** 引擎，將「本地意圖」與「雲端情資」物理合併。
- [x] **Day 13**: 實作高級視覺化報告引擎 (V2.0)。引入條件渲染技術與自動化案卷管理系統。
- [x] **Day 14**: 達成 $\color{#E1AD01}{\text{第六個整合里程碑}}$。實作 **Heuristic Scoring Matrix (啟發式計分矩陣)**，將碎片化的取證數據轉化為量化威脅指標；導入 **Decision Auditing** 機制，產出透明化的計分過程審計報告，完善自動化指揮中心之決策邏輯。

#### **第二階段：深挖藏身處 (預計)**
- [ ] **Day 15-21**: 引入 Volatility 引擎，實作記憶體掃描與動態行為追蹤模組。

#### **第三階段：執法者啟動 (預計)**
- [ ] **Day 22-30**: 開發自動化應變組件，實作隔離、終止、清理三位一體的執行緒。

---

## 🛠️ 安裝與快速啟動 (Setup & Quick Start)
```bash
# 1. 克隆專案
git clone https://github.com/JimYao0314/C2-Traffic-Sentinel.git
cd C2-Traffic-Sentinel

# 2. 配置金鑰 (OpSec 隔離)
# 於根目錄建立 .env 檔案並寫入: VT_API_KEY=your_key_here

# 3. 啟動環境與還原
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt

# 4. 執行決策引擎測試 (Day 14 產出)
python day14_Heuristic_Scoring/decision_engine.py