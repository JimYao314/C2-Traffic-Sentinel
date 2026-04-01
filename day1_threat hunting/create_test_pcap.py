# 虛擬的威脅 → 合成流量 (Synthetic Traffic) or 「模擬樣本」
from scapy.all import IP, TCP, wrpcap
import time


def generate_fake_c2_traffic():
    packets = []
    # 模擬 2024 年常見的 C2：每 2 秒回報一次，非常穩定的規律
    target_ip = "1.2.3.4"
    print(f"[*] 正在生成模擬 C2 流量到 {target_ip}...")

    start_time = time.time()
    for i in range(15):  # 產生 15 個封包
        # 建立一個前往 443 埠口 (HTTPS) 的模擬封包
        pkt = IP(dst=target_ip) / TCP(dport=443, flags="S")
        # 設定每個封包的時間間隔，剛好是 2 秒
        pkt.time = start_time + (i * 2.0)
        packets.append(pkt)

    wrpcap("evidence.pcap", packets)  # 存成檔案
    print("[+] 成功產出測試檔: evidence.pcap")


if __name__ == "__main__":
    generate_fake_c2_traffic()