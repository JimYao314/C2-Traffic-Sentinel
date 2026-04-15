# 🛡️ C2-Traffic-Sentinel (Project Sphinx)
> **整合型 C2 威脅偵測哨兵：從網路流量到端點行為的全方位自動化獵捕平台**

![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)
![Security Focus](https://img.shields.io/badge/Focus-Threat%20Hunting%20%7C%20Incident%20Response-red)
![Progress](https://img.shields.io/badge/Progress-Day%2010%20%2F%2030-green)

**Project Sphinx** 是一個為期 30 天的整合性數位鑑識與事件應變 (DFIR) 平台建構計畫。本專案旨在透過 Python 3.10+ 自動化處理海量資安日誌與網路流量，實現從「原始數據解析」到「自動化報告產出」的完整 Pipeline。

---

## 🚀 技術棧 (Tech Stack)
- **核心語言**: Python 3.10+ (具備物件導向 Class 呼叫鏈、遞迴分析與 **Generator 串流技術**)
- **數據分析**: Scapy (Network), python-evtx (Binary Logs), pefile & yara-python (Malware)
- **效能優化**: **Streaming Processing (Yield/Generators)**, Memory-efficient Parsing
- **數據處理**: Pandas (Correlation), JSON Serialization
- **報告引擎**: Markdown Templating (Reporting-as-Code), MITRE ATT&CK Mapping

---

## 📊 產出範例 (Sample Output)
- [📈 數位取證鑑定報告樣本](./reports/Sample_Forensic_Report.md)
- [🔍 JSON 結構化威脅情報樣本](./reports/Sample_Threat_Data.json)

---

## 📅 30 天獵捕日誌 (The Hunting Log)

| 天數 | 主題 | 核心產出 | 關鍵技術點 |
| :--- | :--- | :--- | :--- |
| **Day 1** | 網路哨兵基礎 | `create_test_pcap.py` | Scapy 封包構造、標準差心跳偵測 (Beaconing) |
| **Day 2** | 端點日誌解析 | `evtx_process_hunter.py` | EVTX 二進位解碼、XPath XML 數據提取 |
| **Day 3** | 持久化行為獵捕 | `sysmon_hunter.py` | Sysmon Event ID 13 解析、環境取證標準化 |
| **Day 4** | 惡意指令去混淆 | `deobfuscator.py` | Regex 參數捕捉、Base64 / UTF-16LE 解碼引擎 |
| **Day 5** | 模組化大整合 | `integrated_hunter.py` | **里程碑 I：** 跨模組呼叫、自動化掃描即還原 |
| **Day 6** | 靜態惡意程式分析 | `file_analyzer.py` | SHA256 指紋採集、PE 結構解剖、YARA 基因掃描 |
| **Day 7** | 自動化關聯獵捕 | `auto_correlation_hunter.py` | **里程碑 II：** 事件驅動自動化管線、Ghost Process 偵測 |
| **Day 8** | 深度數據挖掘 | `advanced_deobfuscator.py` | 遞迴解碼邏輯 (Recursion)、JSON 報告序列化 |
| **Day 9** | 自動化報告撰寫 | `markdown_reporter.py` | Reporting-as-Code、MITRE 映射、處置建議自動生成 |
| **Day 10** | 大數據效能優化 | `streaming_orchestrator.py` | **里程碑 III：** Generator 串流解析、記憶體恆定化優化 |

---

### 🗓️ 開發實況紀錄 (Dev Log)
- [x] **Day 01-04**: 完成基礎分析零件，包含網路心跳統計、日誌解碼與 PowerShell 去混淆引擎。
- [x] **Day 05**: 達成 $\color{#E1AD01}{\text{首個整合里程碑}}$。實現「掃描即還原」自動化工作流，具備處理大規模二進位證據能力。
- [x] **Day 06**: 實作靜態鑑定模組。不執行檔案即可透過 Hashing、PE 結構與 YARA 規則識別惡意基因。
- [x] **Day 07**: 達成 $\color{#E1AD01}{\text{第二個整合里程碑}}$。實作「日誌觸發鑑定」自動化管線，解決 Ghost Process 反鑑識對抗。
- [x] **Day 08**: 實作進階數據挖掘模組。透過遞迴 (Recursive) 邏輯拆解多層嵌套混淆，並導入 JSON 數據標準化。
- [x] **Day 09**: 實作自動化報告引擎。開發 **Reporting-as-Code** 模組，實現鑑定建議書的自動化生產。
- [x] **Day 10**: 達成 $\color{#E1AD01}{\text{第三個整合里程碑}}$。針對大規模企業日誌（33,000+ 筆）實作 **Streaming Analysis (串流分析)** 架構；利用 Python `yield` 生成器技術將空間複雜度優化至 $O(1)$，實現即時攔截與記憶體無感監控。
- [ ] **Day 11**: (預計) 強化分析深度：實作時間窗分析 (Time-window Analysis) 與異常登入行為建模。

---

## 🧩 核心模組架構 (Architecture)

### 1. Detection Engines (偵測引擎)
- **Streaming Pipeline**: 利用 `yield` 技術，實現邊讀取、邊分析、邊報警的高效能管線，能處理數 GB 級別的原始 EVTX 日誌而不佔用額外記憶體。
- **Recursive Deobfuscator**: 具備遞迴拆解能力，自動破譯多層嵌套的 Base64 加密指令。

### 2. Analysis & Orchestration (分析與編排)
- **Malware Analyst**: 整合 YARA 引擎與 PE 解析，識別檔案惡意潛力與加殼特徵。
- **Decision Engine**: 實作啟發式權重計分（Heuristic Scoring），自動關聯「事件日誌」與「磁碟實體」。

### 3. Reporting Engine (報告引擎)
- **Reporting-as-Code**: 自動生成具備 Executive Summary、MITRE ATT&CK 映射與處置建議的專業鑑定報告。

---

## 🛠️ 安裝與快速啟動 (Setup & Quick Start)
```bash
# 1. 克隆專案並進入實驗室
git clone https://github.com/JimYao0314/C2-Traffic-Sentinel.git
cd C2-Traffic-Sentinel

# 2. 啟動虛擬環境與一鍵還原分析環境
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt

# 3. 執行串流獵捕測試 (Day 10 產出)
python day10_Big_Data_Optimization/streaming_orchestrator.py