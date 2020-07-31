import requests
from bs4 import BeautifulSoup
import smtplib
import time

url = "https://finance.yahoo.com/quote/AAPL?p=AAPL"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"}

def stock_price_check():
    # return all data from website
    page = requests.get(url, headers = headers)

    # parse so can pull out individual pieces of info
    soup = BeautifulSoup(page.content, "html.parser")

    # Get stock name
    stock_name = soup.find("h1", {"class" : "D(ib) Fz(18px)"}).get_text()

    # Get stock price
    stock_price = soup.find("span", {"class": "Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)"}).get_text()

    # Convert price to only first 4 numbers and float
    converted_price = float(stock_price[0:3])

    if converted_price < 430:
        send_email()
    
    print(stock_name.strip())
    print(f"Stock price: {converted_price}")



def send_email():
# Set up gmail server 
    server  = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login("villarroeljesvian@gmail.com", "taitgqdyidjauatd")

    subject = "Stock Price Fell!"
    body = "Your stock price fell!: https://finance.yahoo.com/quote/AAPL?p=AAPL"

    msg = f"{subject}\n\n{body}"

    server.sendmail(
        # email being sent from
        "villarroeljesvian@gmail.com",

        # email being sent to
        "jesvianadolfo@yahoo.com",

        # message
        msg
    )
    print("MESSAGE HAS BEEN SENT!")

    server.quit()

# loop to continue running checking price/sending emails once a day
while(True):
    stock_price_check()
    # checks every 60 seconds
    time.sleep(60)



