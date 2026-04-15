import base64
import re
from dataclasses import dataclass
from typing import Optional


# --- [ 建立數據傳輸標準 ] ---
@dataclass
class DeobfuscationResult:
    is_obfuscated: bool
    decoded_cmd: Optional[str] = None
    risk_level: str = "Low"


# --- [ 將函式升級為『類別』 ] ---
class SphinxDeobfuscator:
    def __init__(self):
        # 將原本的 Regex 咒語變成專家的『專長屬性』
        self.pattern = re.compile(r"-(?:e|enc|encodedcommand)\s+([A-Za-z0-9+/=]+)", re.IGNORECASE)

    def analyze_command(self, raw_cmd: str) -> DeobfuscationResult:
        """
        專業負責：分析單一指令，判斷有無混淆並解碼
        """
        match = self.pattern.search(raw_cmd)

        if match:
            try:
                b64_str = match.group(1)
                # 執行 Base64 與 UTF-16LE 解碼
                decoded = base64.b64decode(b64_str).decode("utf-16-le")

                # 判定風險
                risk = "🔥 CRITICAL" if "downloadstring" in decoded.lower() else "High"

                return DeobfuscationResult(is_obfuscated=True, decoded_cmd=decoded, risk_level=risk)
            except:
                return DeobfuscationResult(is_obfuscated=True, decoded_cmd="[解碼失敗]", risk_level="Error")

        return DeobfuscationResult(is_obfuscated=False)


# 為了不破壞你之前的測試，保留執行區塊
if __name__ == "__main__":
    test_cmd = "powershell.exe -enc dwBoAG8AYQBtAGkA"
    expert = SphinxDeobfuscator()
    res = expert.analyze_command(test_cmd)
    print(f"解碼結果: {res.decoded_cmd}")