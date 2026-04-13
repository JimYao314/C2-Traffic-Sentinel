# 🛡️ C2-Traffic-Sentinel (Project Sphinx)
> **整合型 C2 威脅偵測哨兵：從網路流量到端點行為的全方位自動化獵捕平台**

![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)
![Security Focus](https://img.shields.io/badge/Focus-Threat%20Hunting%20%7C%20Incident%20Response-red)
![Progress](https://img.shields.io/badge/Progress-Day%208%20%2F%2030-green)

**Project Sphinx** 是一個為期 30 天的整合性數位鑑識與事件應變 (DFIR) 平台建構計畫。本專案旨在透過 Python 3.10+ 自動化處理海量資安日誌與網路流量，實現從「原始數據解析」到「自動化威脅連動分析」的完整 Pipeline。

---

## 🚀 技術棧 (Tech Stack)
- **核心語言**: Python 3.10+ (具備物件導向 Class 呼叫鏈與遞迴分析邏輯)
- **網路分析**: Scapy (Packet crafting & parsing)
- **主機鑑識**: python-evtx, lxml (XPath), Sysmon Integration, shlex (Path surgery)
- **檔案解剖**: pefile (PE Structure), yara-python (Genetic Pattern Matching)
- **數據處理**: Pandas (Correlation & statistics), **JSON Serialization (Standardized Reporting)**

---

## 📅 30 天獵捕日誌 (The Hunting Log)

| 天數 | 主題 | 核心產出 | 關鍵技術點 |
| :--- | :--- | :--- | :--- |
| **Day 1** | 網路哨兵基礎 | `create_test_pcap.py`, `main.py` | Scapy 封包構造、標準差心跳偵測 (Beaconing) |
| **Day 2** | 端點日誌解析 | `evtx_process_hunter.py` | EVTX 二進位解碼、XPath XML 數據提取、4624 行為建模 |
| **Day 3** | 持久化行為獵捕 | `sysmon_hunter.py` | Sysmon Event ID 13 解析、環境取證標準化 (C:\InfoSec_Lab) |
| **Day 4** | 惡意指令去混淆 | `deobfuscator.py` | Regex 參數捕捉、Base64 / UTF-16LE 自動解碼引擎 |
| **Day 5** | 模組化大整合 | `integrated_hunter.py` | **首個里程碑：** 跨模組呼叫架構、自動化解碼連動、效能採樣優化 |
| **Day 6** | 靜態惡意程式分析 | `file_analyzer.py` | SHA256 指紋採集、PE 結構解剖 (TimeDateStamp)、YARA 基因掃描 |
| **Day 7** | 自動化關聯獵捕 | `auto_correlation_hunter.py` | **第二個里程碑：** 事件驅動自動化管線、啟發式權重評分、Ghost Process 偵測 |
| **Day 8** | 深度數據挖掘 | `advanced_deobfuscator.py` | **遞迴解碼引擎 (Recursion)**、多層嵌套拆解、JSON 報告序列化 |

---

### 🗓️ 開發實況紀錄 (Dev Log)
- [x] **Day 01**: 完成 Scapy 封包解析引擎，實作心跳行為 (Beaconing) 統計分析。
- [x] **Day 02**: 完成 EVTX 日誌解析模組，實作 4624 登入事件自動化過濾。
- [x] **Day 03**: 成功實作 Sysmon 持久化監控模組。解決路徑衝突，完成取證環境標準化遷移。
- [x] **Day 04**: 實作 PowerShell 去混淆引擎。克服 UTF-16LE 解碼陷阱，產出純淨 `requirements.txt`。
- [x] **Day 05**: 達成 $\color{#E1AD01}{\text{首個整合里程碑}}$。實現「掃描即還原」自動化工作流，具備處理大規模二進位證據能力。
- [x] **Day 06**: 實作靜態鑑定模組。不執行檔案即可透過 Hashing、PE 結構分析與 YARA 規則識別惡意基因，實現多維度檔案特徵獵捕。
- [x] **Day 07**: 達成 $\color{#E1AD01}{\text{第二個整合里程碑}}$。實作「日誌觸發鑑定」自動化管線，解決 Ghost Process 反鑑識對抗；引入啟發式權重評分引擎。
- [x] **Day 08**: 實作進階數據挖掘模組。透過遞迴 (Recursive) 邏輯自動拆解多層嵌套混淆指令，成功破解「俄羅斯娃娃」式攻擊特徵；導入 JSON 序列化技術，將碎片化的分析過程轉化為標準化、可對接 SIEM 的結構化取證報告。
- [ ] **Day 09**: (預計) 自動化報告撰寫：實作分析結果向 Markdown 格式的自動轉化，生成具備專業質感的資安鑑定建議書。

---

## 🧩 核心模組架構 (Architecture)

### 1. Network Sentinel (網路監控模組)
- **亮點**: 利用標準差 (StdDev) 算法排除人為隨機流量，精準定位自動化木馬回傳心跳。

### 2. Endpoint Hunter & Deobfuscator (端點獵捕與解碼模組)
- **亮點**: 透過 XPath 實現秒級 XML 數據提取，並具備 **「遞迴拆解」** 能力，不論駭客進行幾層 Base64 嵌套加密，皆能自動還原原始意圖。

### 3. Malware Analyst & Orchestrator (自動化鑑定指揮官)
- **實作內容**: 跨模組邏輯連動與數據序列化。
- **亮點**: 整合 **啟發式權重計分** 並將所有鑑定結果 **JSON 化**。這確保了分析數據可以被外部系統（如 SIEM 或自動化郵件警報）無縫調用。

---

## 🛠️ 安裝與快速啟動 (Setup & Quick Start)
```bash
# 1. 克隆專案並進入實驗室
git clone https://github.com/JimYao0314/C2-Traffic-Sentinel.git
cd C2-Traffic-Sentinel

# 2. 建立並啟動虛擬環境 (Windows)
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# 3. 一鍵還原分析環境
pip install -r requirements.txt

# 4. 執行多層嵌套解碼測試 (Day 8 產出)
python day8_Advanced_Data_Mining/advanced_deobfuscator.py