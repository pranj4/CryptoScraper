from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from time import sleep


# Set options for not prompting DevTools information
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")


print("testing started")
driver = webdriver.Chrome(options=options)
print("")
driver.get("https://www.saucedemo.com/")
sleep(3)

# Get page title
title = driver.title

# Test if title is correct
assert "Swag Labs" in title
print("TEST 0: `title` test passed")

# Close the driver
driver.quit()