import urllib.request
from datetime import datetime
from zoneinfo import ZoneInfo

URL = "https://www.mvdis.gov.tw/m3-emv-mk3/agent/webAgentFactory"

print("台灣時間：", datetime.now(ZoneInfo("Asia/Taipei")))
print("開始測試監理服務網...")

request = urllib.request.Request(
    URL,
    headers={"User-Agent": "Mozilla/5.0"}
)

try:
    with urllib.request.urlopen(request, timeout=30) as response:
        html = response.read().decode("utf-8", errors="replace")
        print("HTTP 狀態：", response.status)
        print("網頁長度：", len(html))
        with open("page.html", "w", encoding="utf-8") as file:
            file.write(html)
        print("已儲存 page.html")
except Exception as error:
    print("連線失敗：", str(error))
