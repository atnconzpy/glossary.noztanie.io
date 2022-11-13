from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd
import os
#Open webdriver
browser = webdriver.Chrome(executable_path="D:/Python/I Just Wanna Test Python/assign/chromedriver.exe")
#Get link
browser.get("https://stword.com/posts/it-programming-tu-vung-ve-lap-trinh")
#Time to loading web
sleep(5)

next_page = browser.find_element(By.XPATH,"/html/body/app-root/app-main-template/div/div/app-posts/section/div/div/div[1]/div[1]/div[2]/div[2]/div/div/app-list-words/div/div/app-pagination/ul/li[14]/a")
list_key = []
list_mean = []
def clear_key(n):
    str_key = str(key.text)
    list_str_key = list(str_key)
    del list_str_key[0: list_str_key.index(".")+1]
    list_key_join = "".join(list_str_key)
    return list_key_join
for page in range(0,15):
    list_key_mean = browser.find_elements(By.TAG_NAME, "app-word")
    for key_mean in list_key_mean:
        key = key_mean.find_element(By.TAG_NAME,"h4")
        mean = key_mean.find_element(By.CLASS_NAME, "content-word")    
        key_text = clear_key(key) 
        print(key_text)

    # sleep(5)
    # browser.execute_script("arguments[0].click();", next_page)
    sleep(5)
    
sleep(5)


browser.close()