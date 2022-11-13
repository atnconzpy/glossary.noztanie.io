from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd
import numpy as np
import os
#Open webdriver
browser = webdriver.Chrome(executable_path="D:/Python/I Just Wanna Test Python/assign/Dictionary/chromedriver.exe")
#Get link
list_key =[]
list_mean =[]

url = "https://www.ntdvn.net/khoa-hoc/9-thuat-ngu-tieng-anh-quan-trong-trong-nganh-tri-tue-nhan-tao-364763.html#table_content_2"
browser.get(url)
div = browser.find_elements(By.TAG_NAME,"tbody")
for i in div:
    x = i.find_elements(By.TAG_NAME,"tr")
    for j in x:
        a = j.find_elements(By.TAG_NAME,"td")
        key_a = a[1].text
        mean_a = a[2].text
        print(key_a,":",mean_a)
        list_key.append(key_a)
        list_mean.append(mean_a)

# for i in div:
#     a = i.find_element_by_css_selector("li.active a")
#     print(a)  
browser.close()