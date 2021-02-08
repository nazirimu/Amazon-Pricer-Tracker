import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

# PRODUCT INFORMATION
URL = "https://www.amazon.ca/Instant-Pot-Duo-Evo-Plus/dp/B07W55DDFB/ref=sr_1_1?qid=1597662463"
target_price = 200.0
product = "Instant Pot"
# ^ ABOVE INFORMATION CAN BE SWITCHED IF YOU WOULD LIKE TO TARGET A DIFFERENT PRODUCT


# BROWSER INFORMATION FOR WEB SCRAPPING
header = {
    "User-Agent" : "ENTER YOUR OWN. TO FIND GO TO http://myhttpheader.com/",
    "Accept-Language" : "en-US,en;q=0.9"
}
# EMAIL INFO FOR EMAIL
MY_EMAIL = "nshaz9932@gmail.com"
MY_PASSWORD = "ENTER YOUR OWN PASSWORD AND YOUR OWN EMAIL ABOVE"

# USING THE RESPONSE MODULE TO GET THE WEBPAGE
response = requests.get(URL, headers=header)
amazon_wbpage = response.text

# Using Beautiful Soup to parse the amazon webpage
# # NOTE FOR AMAZON FOR COUNTRIES OTHER THAN CANADA, LXML PARSER MIGHT BE NEEDED
soup = BeautifulSoup(amazon_wbpage, 'html.parser')

# Using the soup to find the price of the product
price_tag = soup.find(id="priceblock_ourprice").getText()
price_without_currency = price_tag.split("$")[1]
price_as_float = float(price_without_currency)
print(price_as_float)

# CHECKS THE PRICE OF THE PRODUCT VS TARGET PRICE
if price_as_float <= target_price:

    email_script = f"The price of {product} is below ${target_price}, visit: {URL}"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,to_addrs=MY_EMAIL, msg=f"Subject: Amazon Tracker Price Alert!\n\n{email_script}")

else:
    print("Price is over the limit!")
