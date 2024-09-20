# 先導入後面會用到的套件
import requests  # 請求工具
from bs4 import BeautifulSoup  # 解析工具
import time  # 用來暫停程式
from urllib.parse import quote_plus  # 如果 message 包含特殊字符（如空格、符號等），需要使用 urllib.parse.quote_plus()

# 要爬的股票
stock = ["1101", "2330"]

for i in range(len(stock)):  # 迴圈依序爬股價
    
    # 現在處理的股票
    stockid = stock[i]

    # 網址塞入股票編號
    url = "https://tw.stock.yahoo.com/quote/" + stockid + ".TW"

    # 發送請求
    r = requests.get(url)

    # 確認請求是否成功
    if r.status_code == 200:
        # 解析回應的 HTML
        soup = BeautifulSoup(r.text, 'html.parser')

        # 定位股價，添加錯誤處理避免元素找不到
        try:
            price = soup.find(
                'span', class_=["Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c) C($c-trend-down)",
                                "Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c)",
                                "Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c) C($c-trend-up)"]).getText()
        except AttributeError:
            print(f"無法找到股票 {stockid} 的股價。")
            continue  # 繼續處理下一隻股票

        # 回報的訊息 (可自訂)
        message = f"股票 {stockid} 即時股價為 {price}"

        # 用 telegram bot 回報股價
        # bot token
        token = "7702909345:AAH2mn5uangiAbAmnJJKcCY9ZNb6GzRjwsg"

        # 使用者 id
        chat_id = "@vkxuan"

        # bot 送訊息，記得對 message 進行 URL 編碼
        telegram_url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={quote_plus(message)}"

        # 發送請求並檢查回應
        response = requests.get(telegram_url)

        if response.status_code == 200:
            print(f"已成功發送股票 {stockid} 的訊息。")
        else:
            print(f"發送訊息失敗，狀態碼：{response.status_code}, 訊息：{response.text}")
    else:
        print(f"無法取得股票 {stockid} 的資料，狀態碼：{r.status_code}")

    # 每次都停 3 秒
    time.sleep(3)
