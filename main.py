import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


chrome_driver_path = "C:/Users/gb/Documents/chromedriver.exe"
driver_service = Service(executable_path=chrome_driver_path)


class ScrapeEngine:

    def __init__(self):

        self.driver = webdriver.Chrome(service=driver_service)
        self.driver.maximize_window()
        self.site = input("Enter the accurate url for the jumia page: \n")
        self.driver.get(self.site)

        self.spec = []
        self.price = []
        self.product_link = []

    def get_details(self):
        time.sleep(2)
        specs = self.driver.find_elements(by=By.CSS_SELECTOR, value=".name")
        for spec in specs:
            self.spec.append(spec.text)

        prices = self.driver.find_elements(by=By.CSS_SELECTOR, value=".prc")
        for price in prices:
            self.price.append(price.text)

        product_link = self.driver.find_elements(by=By.CSS_SELECTOR, value=".core")
        for links in product_link:
            self.product_link.append(links.get_attribute("href"))
        time.sleep(3)

    def click_button(self):
        nxt_button = self.driver.find_element(by=By.XPATH, value='//*[@id="jm"]/main/div[2]/div[3]/section/div[2]/a[6]')
        # nxt_button.click()
        self.driver.execute_script("arguments[0].click();", nxt_button)
        time.sleep(2)


start_time = time.perf_counter()
scrape = ScrapeEngine()
pages = int(input("How many pages do you want to do scrape? "))
while pages > 0:
    scrape.get_details()
    scrape.click_button()
    pages -= 1

a = []
for i in range(len(scrape.spec)):
    a.append((scrape.spec[i], scrape.price[i].replace("₦", "").replace(",", ""), scrape.product_link[i]))


df = pd.DataFrame(a, columns=["Spec", "Price", "product link"])

new_csv = df.to_csv("prices.csv", index=False)
scrape.driver.quit()
end_time = time.perf_counter()

time_taken = round(((end_time - start_time) / 60), 2)
print("Completed in", time_taken, "minutes")
