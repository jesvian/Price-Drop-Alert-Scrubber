import requests
from bs4 import BeautifulSoup
import smtplib
import time

url = "https://www.amazon.com/Sceptre-Edge-Less-FreeSync-DisplayPort-C275B-144RN/dp/B07N6ZBCVY/ref=sxin_7_ac_d_rm?ac_md=3-2-Z2FtaW5nIG1vbml0b3JzIDE0NGh6IDFtcw%3D%3D-ac_d_rm&cv_ct_cx=gaming+monitor&dchild=1&keywords=gaming+monitor&pd_rd_i=B07N6ZBCVY&pd_rd_r=fa6c3bdf-1d91-420c-add6-2f84ea25f7ee&pd_rd_w=Jw8QD&pd_rd_wg=7b0jV&pf_rd_p=e3dc9e0c-9eab-4c3e-b43a-ba36f8522e14&pf_rd_r=6BAK4F39AATAGMJZ62MJ&psc=1&qid=1596214135&sr=1-3-12d4272d-8adb-4121-8624-135149aa9081"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"}

def check_price():
        # return all data from website
    page = requests.get(url, headers = headers)

    # parse so can pull out individual pieces of info
    soup = BeautifulSoup(page.content, "html.parser")

    # Find title/product I want (only name/text of product)
    title = soup.find(id="productTitle").get_text()

    # Find price of product
    product_price = soup.find(id="priceblock_ourprice").get_text()

    # Extracts first 3 digits of price (not cents or $ sign) & converts to float
    converted_price = float(product_price[1:4])

    if(converted_price < 198.0):
        send_email()

    print(converted_price)

    # strips whitespace
    print(title.strip())

    if(converted_price < 198.0):
        send_email()

def send_email():
    # Set up gmail server 
    server  = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login("villarroeljesvian@gmail.com", "taitgqdyidjauatd")

    # Actually email being sent to me
    subject = "Price fell down!"
    body = "Check the amazon link: https://www.amazon.com/Sceptre-Edge-Less-FreeSync-DisplayPort-C275B-144RN/dp/B07N6ZBCVY/ref=sxin_7_ac_d_rm?ac_md=3-2-Z2FtaW5nIG1vbml0b3JzIDE0NGh6IDFtcw%3D%3D-ac_d_rm&cv_ct_cx=gaming+monitor&dchild=1&keywords=gaming+monitor&pd_rd_i=B07N6ZBCVY&pd_rd_r=fa6c3bdf-1d91-420c-add6-2f84ea25f7ee&pd_rd_w=Jw8QD&pd_rd_wg=7b0jV&pf_rd_p=e3dc9e0c-9eab-4c3e-b43a-ba36f8522e14&pf_rd_r=6BAK4F39AATAGMJZ62MJ&psc=1&qid=1596214135&sr=1-3-12d4272d-8adb-4121-8624-135149aa9081"

    message = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        # email being sent from
        "villarroeljesvian@gmail.com",
        "jesvianadolfo@yahoo.com",
        message
    )
    print("HEY EMAIL HAS BEEN SENT!")

    server.quit()

# loop to continue running checking price/sending emails once a day
while(True):
    check_price()
    # 86,400 secs = 1 day
    time.sleep(43,200)