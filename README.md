# 🛡️ Project Sphinx: 30-Day DFIR Engineering Challenge

![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)
![Security Focus](https://img.shields.io/badge/Focus-Threat%20Hunting%20%7C%20Incident%20Response-red)
![Progress](https://img.shields.io/badge/Progress-Day%202%20%2F%2030-green)

**Project Sphinx** 是一個為期 30 天的整合性數位鑑識與事件應變 (DFIR) 平台建構計畫。本專案旨在透過 Python 3.10+ 自動化處理海量資安日誌與網路流量，實現從「原始數據解析」到「自動化威脅獵捕」的完整 Pipeline。

---

## 🚀 技術棧 (Tech Stack)
- **語言**: Python 3.10+ (match-case, asyncio, type hinting)
- **網路分析**: Scapy (Packet crafting & parsing)
- **主機鑑識**: python-evtx, lxml, xml-standard
- **數據處理**: Pandas (Big data analysis & correlation)
- **框架對齊**: MITRE ATT&CK Framework

---

## 📅 30 天獵捕日誌 (The Hunting Log)

| 天數 | 主題 | 核心產出 | 關鍵技術點 |
| :--- | :--- | :--- | :--- |
| **Day 1** | 網路哨兵基礎 | `create_test_pcap.py`, `main.py` | Scapy 封包構造、標準差心跳偵測 (Beaconing) |
| **Day 2** | 端點日誌解析 | `evtx_process_hunter.py` | EVTX 二進位解碼、XPath XML 數據提取、4624 行為建模 |
| **Day 3** | 持久化行為獵捕 | `sysmon_hunter.py`, `requirements.txt` | Sysmon Event ID 13 解析、XPath 數據提取、環境取證標準化 |
| **Day 4** | 惡意指令去混淆 | (待更新) | Base64 自動解碼、PowerShell 混淆行為偵測 |

---

### 🗓️ 開發實況紀錄 (Dev Log)
- [x] **Day 01**: 完成 Scapy 封包解析引擎，實作 `main.py` 與 `create_test_pcap.py`。
- [x] **Day 02**: 完成 EVTX 日誌解析模組，解決 `python-evtx` 依賴問題，成功過濾 4624 登入事件。
- [x] **Day 03**: 成功實作 Sysmon 持久化監控模組。解決 OneDrive 路徑衝突並完成 `C:\InfoSec_Lab` 取證環境標準化遷移，產出專案 `requirements.txt` 以確保環境可移植性。
- [ ] **Day 04**: (開發中) 預計導入 PowerShell 惡意指令自動去混淆 (Deobfuscation) 與行為標籤化。。

---

## 🧩 核心模組架構 (Modules)

### 1. Network Sentinel (網路監控模組)
- **功能**: 自動識別 C2 通訊特徵。
- **亮點**: 實作統計學偵測模型，有效排除人為隨機流量，精準定位自動化木馬回傳。

### 2. Endpoint Hunter (端點獵捕模組)
- **功能**: Windows Event Logs 自動化分析。
- **亮點**: 透過 XPath 實現秒級過濾萬筆 XML 日誌，並針對 LOLBins (如 PowerShell, Certutil) 進行關鍵字特徵獵捕。

---

## 🛠️ 安裝與環境 (Setup)
```bash
# 克隆專案
git clone https://github.com/JimYao0314/C2-Traffic-Sentinel.git

# 建立虛擬環境 (DFIR 隔離環境)
python -m venv .venv
source .venv/bin/activate  # Windows: .\.venv\Scripts\Activate.ps1

# 安裝依賴
pip install scapy pandas python-evtx lxml
