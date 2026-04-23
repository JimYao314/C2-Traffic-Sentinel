# 🛡️ C2-Traffic-Sentinel (Project Sphinx)
> **整合型 C2 威脅偵測哨兵：從「存續性足跡」到「揮發性意識」的全方位自動化獵捕與應變平台**

![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)
![Security Focus](https://img.shields.io/badge/Focus-Threat%20Hunting%20%7C%20Incident%20Response-red)
![Progress](https://img.shields.io/badge/Progress-Day%2015%20%2F%2030-green)

**Project Sphinx** 是一個為期 30 天的整合性數位鑑識與事件應變 (DFIR) 平台建構計畫。專案旨在透過 Python 3.10+ 自動化處理海量資安日誌與網路流量，實作從「原始數據解析」到「自動化實時攔截」的完整防禦管線。

---

## 🚀 專案三階段戰略 (The 3-Phase Strategy)

### 🧩 第一階段：存續性取證 (Persistent Forensics) - [已完工 ✅]
- **目標**：追蹤駭客在磁碟與日誌中留下的「足跡」。
- **核心成果**：實作網路心跳偵測、EVTX/Sysmon 自動化解析、遞迴解碼引擎與啟發式權重計分大腦。

### 🔍 第二階段：揮發性取證 (Volatile Forensics) - [進行中 ⏳]
- **目標**：讀取駭客正在隨機存取記憶體 (RAM) 中跳動的「意識」。
- **核心成果**：導入 **Volatility 3** 工業級引擎，利用 `subprocess` 指揮鏈偵測無檔案攻擊 (Fileless)、進程挖空 (Hollowing) 與隱形 Ghost Processes。

### ⚔️ 第三階段：自動化應變 (Active Response)
- **目標**：開發 **The Enforcer (執法者模組)**。
- **核心成果**：實現自動化網路隔離、程序斬首與惡意痕跡清理，達成「發現即處置」的閉環防禦。

---

## 🚀 技術棧 (Tech Stack)
- **核心語言**: Python 3.10+ (Class 呼叫鏈、Generator 串流、**Subprocess 外部引擎調度**)
- **分析引擎**: Scapy (Network), python-evtx (Logs), **Volatility 3 (Memory)**, YARA & pefile
- **數據處理**: Pandas (Big data), JSON Serialization, Secrets Management (.env)
- **報告視覺化**: HTML-in-Markdown, Artifact Lifecycle Management

---

## 📊 產出範例 (Sample Output)
根據專案開發時序產出之核心物證：

1. [⚡ 大數據掃描效能基準報告 (33,142 筆)](./reports/PERFORMANCE_LOG.md) —— `Day 10 效能驗證`
2. [🧬 融合型情資數據樣本 (JSON)](./reports/Sample_Enriched_Threat_Data.json) —— `Day 12 數據融合`
3. [📈 全維度視覺化鑑定報告樣板 (V2.0)](./reports/Sample_Enriched_Forensic_Report.md) —— `Day 13 視覺呈現`
4. [⚖️ 威脅決策審計報告樣板 (計分過程)](./reports/Sample_Decision_Audit.md) —— `Day 14 最終決議`
5. [🧠 揮發性取證環境初始化報告](./reports/Sample_Memory_Forensics_Init.md) —— `Day 15 階段轉型`

---

## 📅 30 天獵捕日誌 (The Hunting Log)

| 天數 | 主題 | 核心產出 | 關鍵技術點 |
| :--- | :--- | :--- | :--- |
| **Day 01-04** | 偵測零件開發 | `main.py`, `deobfuscator.py` | Scapy 流量分析、Base64/UTF-16LE 解碼 |
| **Day 05** | 里程碑 I | `integrated_hunter.py` | 掃描即還原自動化 |
| **Day 07** | 里程碑 II | `auto_correlation_hunter.py` | 事件驅動管線、Ghost Process 偵測 |
| **Day 10** | 里程碑 III | `streaming_orchestrator.py` | $O(1)$ 記憶體串流引擎、204 EPS 實測 |
| **Day 11** | 里程碑 IV | `vt_intel_radar.py` | 全球威脅情資 VirusTotal API 連動 |
| **Day 14** | 里程碑 VI | `decision_engine.py` | 啟發式威脅評分矩陣指揮部落成 |
| **Day 15** | 揮發性取證基礎 | `memory_sentinel.py` | **Volatility 3 整合、Subprocess 指令編排、環境就緒鑑定** |

---

### 🗓️ 開發實況紀錄 (Dev Log)

#### **第一階段：偵測大腦與自動化管線 (Phase 1 Complete)**
- [x] **Day 01-14**: 完成基礎分析零件與啟發式決策中樞。成功實作從日誌解析、多層解碼到雲端情資融合的完整自動化取證管線。

#### **第二階段：深挖藏身處 (Phase 2 In-Progress)**
- [x] **Day 15**: 實作 $\color{#E1AD01}{\text{揮發性分析母體}}$。正式開啟第二階段「意識掃描」；導入 **Volatility 3** 框架，利用 Python `subprocess` 實作外部引擎的自動化調度鏈，並產出實驗室就緒報告（Lab Readiness Report），為對抗無檔案攻擊與隱形進程奠定架構基礎。
- [ ] **Day 16**: (預計) 實戰採樣：模擬製作記憶體鏡像檔案 (Memory Dump) 並實作自動化程序樹掃描。

#### **第三階段：執法者啟動 (預計)**
- [ ] **Day 22-30**: 開發自動化應變組件，實作隔離、終止、清理三位一體的執行緒。

---

## 🛠️ 安裝與快速啟動 (Setup & Quick Start)
```bash
# 1. 克隆專案
git clone https://github.com/JimYao0314/C2-Traffic-Sentinel.git
cd C2-Traffic-Sentinel

# 2. 啟動環境與還原
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt

# 3. 執行揮發性分析母體環境檢查
python day15_Memory_Forensics_Base/memory_sentinel.py