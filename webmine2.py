from selenium import webdriver
import time
import argparse
import chromedriver_binary
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import pandas as pd
def get_product_url(url):
    driver.get(url)
    product_url=[]
    for i in range(1,27):
        Css_path="#search > div.s-desktop-width-max.s-desktop-content.s-opposite-dir.sg-row > div.s-matching-dir.sg-col-16-of-20.sg-col.sg-col-8-of-12.sg-col-12-of-16 > div > span:nth-child(4) > div.s-main-slot.s-result-list.s-search-results.sg-row > div:nth-child({}) > div > div > div > div > div.a-section.a-spacing-small.puis-padding-left-small.puis-padding-right-small > div.a-section.a-spacing-none.a-spacing-top-micro > div > span:nth-child(2) > a".format(i)
        try:
            product=driver.find_element(By.CSS_SELECTOR,Css_path)
            product_url.append(product.get_attribute('href'))
        except:
            pass
    return product_url
def get_review_from_one_page():
    review_collect=[]
    reviews_id=driver.find_elements(By.CSS_SELECTOR,"div[data-hook=genome-widget] a")
    reviews_id=reviews_id[2:] #eliminate the review called "Most helpful positive/negative reviews"
    reviews_body=driver.find_elements(By.CSS_SELECTOR,"span[data-hook=review-body]")
    reviews_body_text=[]
    for i in range(len(reviews_body)):
        reviews_body_text.append(reviews_body[i].text)
    # get the information of reviewer
    for i in range(len(reviews_id)):
        # go to the reviewer's homepage
        reviews_id[i].click()
        time.sleep(2)
        try:
            reviewer_name=driver.find_element(By.CSS_SELECTOR,"#customer-profile-name-header > div.a-row.a-spacing-none.name-container > span")
            reviewer_impact=driver.find_elements(By.CSS_SELECTOR,"span.impact-text")
            text=reviews_body_text[i].replace('\n', ' ')
            name=reviewer_name.text.replace(',', '')
            influence=reviewer_impact[0].text.replace(',', '')
            comment=reviewer_impact[1].text.replace(',','')
            review_collect.append((name,influence,comment,text))
        except:
            pass
        driver.back()
        time.sleep(2)
        # if we refresh the webpage, sometime there will be a error: "stale element reference: element is not attached to the page document"
        # to fix this problem, we need to relocate the elements by css_selector
        reviews_id=driver.find_elements(By.CSS_SELECTOR,"div[data-hook=genome-widget] a")
        reviews_id=reviews_id[2:]
        reviews_body=driver.find_elements(By.CSS_SELECTOR,"span[data-hook=review-body]")
    return review_collect 


options = Options()
options.add_argument("window-size=500,800")
driver = webdriver.Chrome(options=options)
# Define the format of data
df=pd.DataFrame(columns=["product","reviewer","influence","comment","text"])
# Define the category of the product you want to get. For example, the url for  "TV and video" is https://www.amazon.com/s?i=specialty-aps&bbn=16225009011&rh=n%3A%2116225009011%2Cn%3A1266092011&language=zh&ref=nav_em__nav_desktop_sa_intl_television_and_video_0_2_5_14
category_name="TV_and_video"
# use the funtion:get_product_url(url of TV and video) to get the product belongs to "TV and video"
product_url=get_product_url("https://www.amazon.com/s?i=specialty-aps&bbn=16225009011&rh=n%3A%2116225009011%2Cn%3A1266092011&language=zh&ref=nav_em__nav_desktop_sa_intl_television_and_video_0_2_5_14")
# traverse all the url of the product which belong to the same category
for index in range(len(product_url)):
    # go to the product's homepage
    driver.get(product_url[index])
    # get the product name
    product_name=driver.find_element(By.CSS_SELECTOR,"#productTitle").text
    # go to the webpage which contain all the reviews
    review=driver.find_element(By.CSS_SELECTOR,"#reviews-medley-footer > div.a-row.a-spacing-medium > a")
    review.click()
    # Get 10 pages of reviews for each product
    for i in range(10):
        time.sleep(2)
        # get the review from one page
        try:
            collect=get_review_from_one_page()
            # add the data to the df
            for j in range(len(collect)):
                df=df.append(pd.Series({"product":product_name,"reviewer":collect[j][0],"influence":collect[j][1],"comment":collect[j][2],"text":collect[j][3]}),ignore_index=True)
        # click the "next page" button
        except:
            pass
        next_page_button=driver.find_element(By.CSS_SELECTOR,"#cm_cr-pagination_bar > ul > li.a-last")
        next_page_button.click()
path="./amazon_data/"+category_name+"/"+category_name+".csv"
df.to_csv(path,sep=',',index=False,header=True) 
