import os
import sys
import json
import base64
from datetime import datetime

# --- [ 重構點 1：建立指揮鏈通道 ] ---
# 取得專案根目錄 C:\InfoSec_Lab
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)

# 真正發生「呼叫」的地方：從 day4 的資料夾，導入 SphinxDeobfuscator 工具
# 語法邏輯：from [資料夾名稱].[檔案名稱] ...
try:
    from day04_Deobfuscation_Analysis.deobfuscator import SphinxDeobfuscator

    print("[+] 成功串聯 Day 4 解碼模組！")
except ImportError:
    print("[-] 錯誤：找不到 Day 4 模組。請確認該資料夾內有 __init__.py")
    sys.exit(1)


class RecursiveDeobfuscator:
    def __init__(self):
        # --- [ 重構點 2：實例化 Day 4 的零件 ] ---
        # 我們直接把 Day 4 寫好的那套工具「拿過來用」
        self.day4_engine = SphinxDeobfuscator()
        self.history = []

    def deep_scan(self, raw_data):
        """核心遞迴引擎：透過循環呼叫 Day 4 零件，直到拆完為止"""
        current_layer_text = raw_data
        layer_count = 0

        while True:
            # --- [ 重構點 3：不再自己解碼，而是下令給 Day 4 ] ---
            # 呼叫 Day 4 模組中我們寫好的分析函數
            result = self.day4_engine.analyze_command(current_layer_text)

            # 如果 Day 4 告訴我們「這是一層加密指令」
            if result.is_obfuscated:
                layer_count += 1
                self.history.append({
                    "layer": layer_count,
                    "content": result.decoded_cmd,
                    "risk": result.risk_level
                })
                # 把解開的東西，當成下一圈的輸入，看看裡面還有沒有娃娃
                current_layer_text = result.decoded_cmd
            else:
                # Day 4 回報：「報長官，這是明文了，拆不動了。」
                break

        return current_layer_text

    def export_json_report(self, original_cmd, final_result):
        """將分析過程序列化為標準 JSON"""
        report = {
            "status": "Success",
            "timestamp": datetime.now().isoformat(),
            "summary": {
                "layers_unwrapped": len(self.history),
                "is_multi_stage": len(self.history) > 1
            },
            "extraction_steps": self.history,
            "final_payload": final_result
        }
        # indent=4 讓 JSON 看起來整齊漂亮，ensure_ascii=False 支援中文
        return json.dumps(report, indent=4, ensure_ascii=False)


# --- [ 執行與演練 ] ---
if __name__ == "__main__":
    # 模擬一個「雙層俄羅斯娃娃」：
    # 內層：whoami
    # 外層：加密後的 (powershell -enc [whoami])
    inner_cmd = "whoami"
    # 這裡我們手動構造一個雙層加密字串
    layer2_b64 = base64.b64encode(inner_cmd.encode('utf-16-le')).decode()
    layer1_cmd = f"powershell.exe -enc {base64.b64encode(f'powershell -enc {layer2_b64}'.encode('utf-16-le')).decode()}"

    print(f"[*] 收到多層混淆指令：\n{layer1_cmd}\n")

    # 啟動 Day 8 指揮中心
    hunter = RecursiveDeobfuscator()
    final_intent = hunter.deep_scan(layer1_cmd)

    # 產出報告
    print("=" * 65)
    print("【 Project Sphinx：Day 8 遞迴解碼 JSON 報告 】")
    print("=" * 65)
    print(hunter.export_json_report(layer1_cmd, final_intent))