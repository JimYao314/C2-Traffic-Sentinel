import os
import statistics
from collections import defaultdict
from dataclasses import dataclass, field
from typing import List, Dict

# 導入 Scapy 核心組件
from scapy.all import PcapReader, IP, TCP, UDP, DNS


# --- [資料結構層] ---
@dataclass
class FlowStat:
    """用來儲存特定連線（Flow）的統計數據"""
    timestamps: List[float] = field(default_factory=list)  # 紀錄每個封包出現的時間
    payload_sizes: List[int] = field(default_factory=list)  # 紀錄每個封包的大小
    dest_ports: set = field(default_factory=set)  # 紀錄連線過的目標連接埠


# --- [分析邏輯層] ---
class SphinxNetworkAnalyzer:
    def __init__(self, pcap_path: str):
        self.pcap_path = pcap_path
        # 使用字典儲存流量，Key 是 "來源IP->目標IP"
        self.flows: Dict[str, FlowStat] = defaultdict(FlowStat)
        self.suspicious_dns: List[str] = []

    def analyze(self):
        """讀取 PCAP 並解析結構"""
        print(f"[*] 啟動 Project Sphinx 分析引擎...")
        print(f"[*] 正在掃描檔案: {self.pcap_path}")

        if not os.path.exists(self.pcap_path):
            print(f"[-] 錯誤: 找不到檔案 {self.pcap_path}，請先執行 create_test_pcap.py")
            return

        # 使用 PcapReader (Streaming 模式) 以節省記憶體
        with PcapReader(self.pcap_path) as reader:
            count = 0
            for pkt in reader:
                # 只有包含 IP 層的封包才處理
                if not pkt.haslayer(IP):
                    continue

                src_ip = pkt[IP].src
                dst_ip = pkt[IP].dst
                flow_key = f"{src_ip} -> {dst_ip}"

                # 紀錄時間戳與封包大小
                self.flows[flow_key].timestamps.append(float(pkt.time))
                self.flows[flow_key].payload_sizes.append(len(pkt))

                # 使用 Python 3.10 match-case 語法進行協議分類
                match pkt:
                    case _ if pkt.haslayer(DNS) and pkt.getlayer(DNS).qr == 0:
                        # 處理 DNS 查詢
                        try:
                            query_name = pkt.getlayer(DNS).qd.qname.decode()
                            self._check_dns_anomaly(query_name)
                        except:
                            pass
                    case _ if pkt.haslayer(TCP):
                        # 紀錄 TCP 連接埠
                        self.flows[flow_key].dest_ports.add(pkt[TCP].dport)

                count += 1
            print(f"[+] 掃描完成，共處理 {count} 個封包")

    def _check_dns_anomaly(self, domain: str):
        """簡單的 DGA 異常域名偵測邏輯"""
        # 如果網域名稱第一段長度超過 20，視為可疑 (常見於 DGA 演算法)
        if len(domain.split('.')[0]) > 20:
            self.suspicious_dns.append(domain)

    def detect_beaconing(self, threshold_std: float = 0.1):
        """
        核心偵測：心跳行為 (Beaconing) 檢測
        原理：計算連線時間間隔的「標準差」。
        標準差越趨近於 0，代表連線頻率越死板、越像機器人。
        """
        print("\n" + "=" * 50)
        print("【 威脅獵捕報告：Beaconing 規律性檢測 】")
        print("=" * 50)

        found_any = False
        for flow, stat in self.flows.items():
            # 樣本數太少 (少於 5 個) 的連線不具統計意義，跳過
            if len(stat.timestamps) < 5:
                continue

            # 1. 計算所有連線的時間間隔 (Intervals)
            intervals = [
                stat.timestamps[i] - stat.timestamps[i - 1]
                for i in range(1, len(stat.timestamps))
            ]

            # 2. 計算平均值與標準差
            avg_interval = statistics.mean(intervals)
            # 如果只有一個間隔無法計算標準差，設為 999 (不規律)
            std_dev = statistics.stdev(intervals) if len(intervals) > 1 else 999

            # 3. 判斷標準差是否極低 (代表極度規律)
            if std_dev < threshold_std:
                found_any = True
                print(f"[!] 發現高度嫌疑 C2 通訊特徵:")
                print(f"    - 流量方向: {flow}")
                print(f"    - 平均心跳: {avg_interval:.2f} 秒一次")
                print(f"    - 時間抖動 (StdDev): {std_dev:.4f} (極度穩定，排除人為)")
                print(f"    - 目標連接埠: {list(stat.dest_ports)}")
                print("-" * 30)

        if not found_any:
            print("[INFO] 未發現明顯規律性心跳行為。")


# --- [執行單元] ---
if __name__ == "__main__":
    # 指定我們要分析的證據檔案
    EVIDENCE_FILE = "evidence.pcap"

    # 建立分析對象
    hunter = SphinxNetworkAnalyzer(EVIDENCE_FILE)

    # 開始分析流程
    hunter.analyze()
    hunter.detect_beaconing()