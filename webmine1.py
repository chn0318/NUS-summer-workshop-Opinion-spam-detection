from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import chromedriver_binary
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time

driver = webdriver.Chrome()

driver.get("https://www.amazon.com/")

time.sleep(1)

searchbox = driver.find_element(By.CSS_SELECTOR, "#twotabsearchtextbox")
time.sleep(1)
searchbox.send_keys("Electronics")
time.sleep(1)
searchbox.send_keys(Keys.RETURN)


time.sleep(1)
top_reviews = driver.find_element(By.CSS_SELECTOR, ".a-star-medium-4")
time.sleep(1)
top_reviews.click()

time.sleep(1)
top_item = driver.find_element(By.CSS_SELECTOR, "#search > div.s-desktop-width-max.s-desktop-content.s-opposite-dir.sg-row > div.s-matching-dir.sg-col-16-of-20.sg-col.sg-col-8-of-12.sg-col-12-of-16 > div > span:nth-child(4) > div.s-main-slot.s-result-list.s-search-results.sg-row > div:nth-child(3) > div > div > div > div > div > div > div > div.sg-col.sg-col-4-of-12.sg-col-8-of-16.sg-col-12-of-20.s-list-col-right > div > div > div.a-section.a-spacing-none.puis-padding-right-small.s-title-instructions-style > h2 > a > span")
time.sleep(1)
top_item.click()

time.sleep(1)
all_reviews = driver.find_element(By.CSS_SELECTOR, "[data-hook = 'see-all-reviews-link-foot']")
time.sleep(1)
all_reviews.click()

def get_reviews():
    data = []



    time.sleep(1)
    section_reviews = driver.find_element(By.CSS_SELECTOR, "#cm_cr-review_list")

    
    time.sleep(1)
    reviews = section_reviews.find_elements(By.CSS_SELECTOR, "[data-hook = 'review']")
 


    for review in reviews:
        time.sleep(1)
        review_element = review.find_element(By.CSS_SELECTOR, "[data-hook = 'review-body']")
        review_text = review_element.text
        time.sleep(1)
        user_element = review.find_element(By.CSS_SELECTOR, ".a-profile-name")
        user = user_element.text
        #polarity_element = positive_review.find_element(By.CSS_SELECTOR, ".title")
        #polarity = polarity_text
        review_type = "Positive"
        #print(review_text)
        #print(userid)
        data.append({"Review": review_text, "User": user, "Polarity": review_type })
    return pd.DataFrame(data)
    

curr_page = 1

overallDF = get_reviews()

while curr_page < 10:
    time.sleep(1)
    next_elem = driver.find_element(By.CSS_SELECTOR, "#cm_cr-pagination_bar > ul > li.a-last > a")
    next_elem.click()
    time.sleep(1)
    
    this_page_df = get_reviews()
    overallDF = pd.concat([overallDF, this_page_df], ignore_index = True)
    curr_page = curr_page + 1

overallDF