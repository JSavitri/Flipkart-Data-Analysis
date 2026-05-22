from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import pandas as pd
import time

service = Service(ChromeDriverManager().install())

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(service=service, options=options)

driver.get("https://www.flipkart.com/search?q=laptops")

time.sleep(5)

# close popup
try:
    driver.find_element(By.XPATH, "//button[contains(text(),'✕')]").click()
except:
    pass

time.sleep(3)

products = []

# ✅ ONLY REAL PRODUCT CARDS
cards = driver.find_elements(By.XPATH, "//div[contains(@data-id,'CPU') or contains(@data-id,'COM')]")

for c in cards:
    try:
        lines = c.text.split("\n")

        name = ""
        price = ""
        rating = ""

        for l in lines:
            if "₹" in l:
                price = l
            elif l.replace(".", "", 1).isdigit():
                rating = l
            else:
                if len(l) > 10:
                    name = l

        if name and price:
            products.append([name, price, rating])

    except:
        pass

driver.quit()

df = pd.DataFrame(products, columns=["Name", "Price", "Rating"])

print("Final scraped rows:", len(df))

df.to_csv("data/flipkart_data.csv", index=False)
print("CSV saved ✔")