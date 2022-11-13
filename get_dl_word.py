from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd
import os
#Open webdriver
list_key = []
list_mean = []
browser = webdriver.Chrome(executable_path="D:/Python/I Just Wanna Test Python/assign/chromedriver.exe")
#Get link
url = "https://d2l.aivivn.com/glossary.html"
browser.get(url)
#Time to loading web
l = browser.find_elements(By.TAG_NAME,"tbody")

for i in l:
    x = i.find_elements(By.TAG_NAME,"tr")
    for j in x:
        a = j.find_elements(By.TAG_NAME,"td")
        key = a[0].text
        mean = a[1].text
        print(key,":",mean)
        list_key.append(key)
        list_mean.append(mean)
sleep(5)
browser.close() 