# 🛡️ C2-Traffic-Sentinel (Project Sphinx)
> **整合型 C2 威脅偵測哨兵：從網路流量到端點行為的全方位自動化獵捕與應變平台**

![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)
![Security Focus](https://img.shields.io/badge/Focus-Threat%20Hunting%20%7C%20Incident%20Response-red)
![Progress](https://img.shields.io/badge/Progress-Day%2011%20%2F%2030-green)

**Project Sphinx** 是一個為期 30 天的整合性數位鑑識與事件應變 (DFIR) 平台建構計畫。本專案旨在透過 Python 3.10+ 自動化處理海量資安日誌與網路流量，實作從「原始數據解析」到「自動化實時攔截」的完整防禦管線。

---

## 🚀 專案三階段戰略 (The 3-Phase Strategy)

### 🧩 第一階段：建立「偵測大腦」 (Day 01 - Day 14) - [進行中]
- **目標**：完成網路、日誌、檔案與雲端情資的模組化整合。
- **核心成果**：實作「自動決策中樞」，達成多維度威脅權重計分與全球情資連動。

### 🔍 第二階段：深挖「隱蔽藏身處」 (Day 15 - Day 21)
- **目標**：攻克「記憶體鑑識 (Memory Forensics)」與動態行為監控。
- **核心成果**：定位 Ghost Processes 在 RAM 中的實體，識破無檔案攻擊 (Fileless Attacks)。

### ⚔️ 第三階段：啟動「執法權限」 (Day 22 - Day 30)
- **目標**：開發 **The Enforcer (執法者模組)**。
- **核心成果**：實現自動化隔離 (Firewall Block)、程序斬首 (Process Kill) 與惡意痕跡清理。

---

## 🚀 技術棧 (Tech Stack)
- **核心語言**: Python 3.10+ (具備物件導向 Class 呼叫鏈、遞迴分析與 **Generator 串流技術**)
- **數據分析**: Scapy (Network), python-evtx (Logs), pefile & yara-python (Malware), **Requests (API)**
- **效能優化**: **Streaming Pipeline (Yield/Generators)**, Memory-efficient Parsing ($O(1)$ Space)
- **數據處理**: Pandas (Correlation), JSON Serialization, Performance Benchmarking
- **報告引擎**: Markdown Templating (Reporting-as-Code), MITRE ATT&CK Mapping

---

## 📊 產出範例 (Sample Output)
- [📈 數位取證鑑定報告樣本](./reports/Sample_Forensic_Report.md)
- [🔍 JSON 結構化威脅情報樣本](./reports/Sample_Threat_Data.json)
- [⚡ 大數據掃描效能基準報告 (33,142 筆實測)](./reports/PERFORMANCE_LOG.md)

---

## 📅 30 天獵捕日誌 (The Hunting Log)

| 天數 | 主題 | 核心產出 | 關鍵技術點 |
| :--- | :--- | :--- | :--- |
| **Day 01-04** | 偵測零件開發 | `main.py`, `deobfuscator.py` | Scapy 流量分析、Base64/UTF-16LE 解碼 |
| **Day 05** | 里程碑 I | `integrated_hunter.py` | **首個整合里程碑：** 掃描即還原自動化 |
| **Day 07** | 里程碑 II | `auto_correlation_hunter.py` | **第二個整合里程碑：** 事件驅動管線、Ghost Process 偵測 |
| **Day 10** | 里程碑 III | `streaming_orchestrator.py` | **第三個整合里程碑：** $O(1)$ 記憶體串流引擎、204 EPS 實測 |
| **Day 11** | 里程碑 IV | `vt_intel_radar.py` | **第四個整合里程碑：** 全球威脅情資 VirusTotal API 連動 |
| **Day 14** | 里程碑 V | (Expected) | **第五個整合里程碑：** 自動決策指揮中樞正式落成 |
| **Day 21** | 里程碑 VI | (Expected) | **第六個整合里程碑：** 記憶體遺失證據捕獲系統 |
| **Day 30** | 終極里程碑 | (Final Delivery) | **The Enforcer 執法者模組啟動：** 達成自動化攔截應變 |

---

### 🗓️ 開發實況紀錄 (Dev Log)

#### **第一階段：偵測大腦與自動化管線**
- [x] **Day 01-04**: 完成基礎分析零件，實作心跳行為統計與 PowerShell 去混淆。
- [x] **Day 05**: 達成 $\color{#E1AD01}{\text{首個整合里程碑}}$。實現日誌掃描與指令還原的自動化連動。
- [x] **Day 06**: 實作靜態鑑定模組。不執行檔案即可透過 Hashing、PE 結構與 YARA 規則識別惡意基因。
- [x] **Day 07**: 達成 $\color{#E1AD01}{\text{第二個整合里程碑}}$。解決 Ghost Process 反鑑識對抗，建立閃電取證管線。
- [x] **Day 08**: 實作進階數據挖掘模組。透過遞迴 (Recursive) 邏輯拆解多層嵌套混淆，並導入 JSON 數據標準化。
- [x] **Day 09**: 實作自動化報告引擎。開發 **Reporting-as-Code** 模組，將 JSON 鑑定數據自動轉化為專業 Markdown 報告。
- [x] **Day 10**: 達成 $\color{#E1AD01}{\text{第三個整合里程碑}}$。針對 33,142 筆真實日誌實作 **Streaming Analysis**；利用 `yield` 技術將空間複雜度優化至 $O(1)$。
- [x] **Day 11**: 達成 $\color{#E1AD01}{\text{第四個整合里程碑}}$。成功對接 **VirusTotal API v3**，實作全球 70+ 安全引擎連動鑑定，並引入本地快取 (Caching) 與頻率限制 (Rate-limiting) 處理。
- [ ] **Day 12**: (開發中) 情報融合：將雲端 API 結果自動導入 Markdown 鑑定報告。

#### **第二階段：深挖藏身處 (預計)**
- [ ] **Day 15-21**: 引入 Volatility 引擎，實作記憶體掃描與動態行為追蹤模組。

#### **第三階段：執法者啟動 (預計)**
- [ ] **Day 22-30**: 開發自動化應變組件，實作隔離、終止、清理三位一體的執行緒。

---

## 🧩 核心模組架構 (Architecture)

### 1. High-Performance Detection Engine (高效能偵測引擎)
- **Streaming Pipeline**: 利用 `yield` 生成器技術，實現邊讀取、邊分析、邊報警的數據流。
- **Recursive Deobfuscator**: 自動破解多層嵌套 Base64 指令，還原隱蔽的攻擊意圖。

### 2. Forensic Analysis & Orchestration (取證分析與編排)
- **Malware Analyst**: 整合 **YARA 基因掃描**、**PE 深度解剖** 與 **VirusTotal 全球情資**。
- **Decision Engine**: 實作啟發式權重計分（Heuristic Scoring），自動關聯「事件日誌」與「磁碟實體」。

### 3. Reporting Engine (報告引擎)
- **Reporting-as-Code**: 自動化產出具備 MITRE ATT&CK 映射與 Actionable Intelligence (處置建議) 的專業鑑定書。

---

## 🛠️ 安裝與快速啟動 (Setup & Quick Start)
```bash
# 1. 克隆專案
git clone https://github.com/JimYao0314/C2-Traffic-Sentinel.git
cd C2-Traffic-Sentinel

# 2. 啟動虛擬環境 (Windows)
.\.venv\Scripts\Activate.ps1

# 3. 安裝工業級依賴環境
pip install -r requirements.txt

# 4. 執行全球情資連動測試 (請先於代碼中配置 API Key)
python day11_Threat_Intel_Integration/vt_intel_radar.py