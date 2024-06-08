from selenium import webdriver
from selenium.webdriver.common.by import By
from celery import shared_task
class CoinMarketCap:
    coins: list
    driver: webdriver.Chrome

    def __init__(self, coins: list):
        self.coins = coins
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--headless')
        self.options.add_argument('--no-sandbox')
        self.options.add_argument('--disable-gpu')
        self.options.add_argument("--disable-dev-shm-usage")
        self.driver = webdriver.Chrome(options=self.options)
        self.get_market_cap()

    @shared_task
    def get_data(self, coin):

        self.driver.get(f'https://coinmarketcap.com/currencies/{coin}/')
        self.driver.implicitly_wait(10)
        data={
            "job_id": "<UUID>",
            "tasks": [
                     {"coin": coin,"output": {
                     "price": self.driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div[2]/div/div/div[2]/section/div/div[2]/span").text
                         ,"price_change":self.driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div[2]/div/div/div[2]/section/div/div[2]/div/div/p").text ,
                         "market_cap": self.driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div[2]/div/div/div[2]/div[2]/section[2]/div/div[1]/div/dl/div[1]/div[2]/div/span").text,
                         "market_cap_rank": 740,"volume": 4583151,"volume_rank": 627,"volume_change": self.driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div[2]/div/div/div[2]/div[2]/section[2]/div/div[1]/div/dl/div[3]/div/dd").text,
                         "circulating_supply": self.driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div[2]/div/div/div[2]/div[2]/section[2]/div/div[1]/div/dl/div[4]/div/dd").text,
                         "total_supply": self.driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div[2]/div/div/div[2]/div[2]/section[2]/div/div[1]/div/dl/div[5]/div/dd").text,
                         "diluted_market_cap": self.driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div[2]/div/div/div[2]/div[2]/section[2]/div/div[1]/div/dl/div[7]/div/dd").text,
                         "contracts": [{"name": "solana","address":"HLptm5e6rTgh4EKgDpYFrnRHbjpkMyVdEeREEa2G7rf9"}],
         "official_links": [
             {"name": "website","link":self.driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div[2]/div/div/div[2]/div[2]/section[2]/div/div[2]/div[2]/div[2]/div/div/a").get_attribute("href")
              }
         ],
         "socials": [
         {"name": "twitter","url": "https://twitter.com/dukocoin"},
         {"name": "telegram","url": "https://t.me/+jlScZmFrQ8g2MDg8"}
         ]
         }
         },
         {
        "coin": "NOT",
         "output": {
        }
         },
         {"coin": "GORILLA","output": {}
         }
         ]
        }
        print(data)


    def get_market_cap(self):
        for i in self.coins:
            self.get_data(i)


CoinMarketCap(["duko"])
