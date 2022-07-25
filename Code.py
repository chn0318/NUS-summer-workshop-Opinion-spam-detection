from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import chromedriver_binary
from selenium.webdriver.common.keys import Keys
import pandas as pd

driver = webdriver.Chrome()

driver.get("https://www.amazon.com/")

electronics = driver.find_element(By.CSS_SELECTOR, "img[alt = 'Electronics']")
electronics.click()

top_reviews = driver.find_element(By.CSS_SELECTOR, ".a-star-medium-4")
top_reviews.click()

top_item = driver.find_element(By.CSS_SELECTOR, ".s-image")
top_item.click()

def get_reviews():
    data = []
    
    reviews = driver.find_element(By.CSS_SELECTOR, ".a-expander-collapsed-height")
    print(len(reviews))
    