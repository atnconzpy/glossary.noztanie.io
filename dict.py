from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd
import numpy as np
import os
#Open webdriver
browser = webdriver.Chrome(executable_path="D:/Python/I Just Wanna Test Python/assign/Dictionary/chromedriver.exe")

#Time to loading web

sleep(5)
list_key = []
list_mean = []

##################### Clone Normal Word ##########################

#Get link
url = "https://stword.com/posts/it-programming-tu-vung-ve-lap-trinh"
browser.get(url)

def clear_key(n):
    str_key = str(key.text).strip()
    list_str_key = list(str_key)
    del list_str_key[0: list_str_key.index(".")+1]
    list_key_join = "".join(list_str_key)
    return list_key_join

next_page = browser.find_element(By.XPATH,"/html/body/app-root/app-main-template/div/div/app-posts/section/div/div/div[1]/div[1]/div[2]/div[2]/div/div/app-list-words/div/div/app-pagination/ul/li[14]/a")
for page in range(0,15):
    list_key_mean = browser.find_elements(By.TAG_NAME, "app-word")
    for key_mean in list_key_mean:
        key = key_mean.find_element(By.TAG_NAME,"h4")
        mean = key_mean.find_element(By.CLASS_NAME, "content-word")    
        key_text = clear_key(key) 
        list_key.append(key_text)
        list_mean.append(mean.text)
        print(key_text,":",mean.text)

    browser.execute_script("arguments[0].click();", next_page)
    sleep(1)
    
sleep(2)




url = "https://stword.com/posts/it-general-tu-vung-tieng-anh-tong-quan-khi-su-dung-may-tinh"
browser.get(url)
next_page = browser.find_element(By.XPATH,"/html/body/app-root/app-main-template/div/div/app-posts/section/div/div/div[1]/div[1]/div[2]/div[2]/div/div/app-list-words/div/div/app-pagination/ul/li[14]/a")
for page in range(0,15):
    list_key_mean = browser.find_elements(By.TAG_NAME, "app-word")
    for key_mean in list_key_mean:
        key = key_mean.find_element(By.TAG_NAME,"h4")
        mean = key_mean.find_element(By.CLASS_NAME, "content-word")    
        key_text = clear_key(key) 
        list_key.append(key_text)
        list_mean.append(mean.text)
        print(key_text,":",mean.text)
        
    browser.execute_script("arguments[0].click();", next_page)
    sleep(1)
    
sleep(2)

#################### Clone Blockchain word ##########################
def clear_syntax_mean(m):
    block_text = str(m.text).strip()
    block_list = list(block_text)
    del block_list[0 : block_list.index(":")+1]
    block_join = "".join(block_list)
    return block_join
def clear_syntax_key(n):
    key_text = str(n.text).strip()
    key_list = list(key_text)
    del key_list[-1]
    key_join = "".join(key_list)
    return key_join

url = "https://tenten.vn/tin-tuc/200-thuat-ngu-crypto-va-blockhain/"
browser.get(url)

for line in range(2,28):
    block = browser.find_element(By.XPATH,f'//*[@id="wrap"]/div/div/div[2]/div[1]/article/div[3]/p[{line}]')
    key = block.find_element(By.XPATH, f'//*[@id="wrap"]/div/div/div[2]/div[1]/article/div[3]/p[{line}]/strong')
    block_join = clear_syntax_mean(block)
    key_join = clear_syntax_key(key)
    list_key.append(key_join)
    list_mean.append(block_join)
    print(block_join,":",key_join)


for line in range(29,72):
    block = browser.find_element(By.XPATH,f'//*[@id="wrap"]/div/div/div[2]/div[1]/article/div[3]/p[{line}]')
    key = block.find_element(By.XPATH, f'//*[@id="wrap"]/div/div/div[2]/div[1]/article/div[3]/p[{line}]/strong')
    block_join = clear_syntax_mean(block)
    key_join = clear_syntax_key(key)
    list_key.append(key_join)
    list_mean.append(block_join)
    print(block_join,":",key_join)


for line in range(73,85):
    block = browser.find_element(By.XPATH,f'//*[@id="wrap"]/div/div/div[2]/div[1]/article/div[3]/p[{line}]')
    key = block.find_element(By.XPATH, f'//*[@id="wrap"]/div/div/div[2]/div[1]/article/div[3]/p[{line}]/strong')
    block_join = clear_syntax_mean(block)
    key_join = clear_syntax_key(key)
    list_key.append(key_join)
    list_mean.append(block_join)
    print(block_join,":",key_join)


for line in range(87,125):
    block = browser.find_element(By.XPATH,f'//*[@id="wrap"]/div/div/div[2]/div[1]/article/div[3]/p[{line}]')
    key = block.find_element(By.XPATH, f'//*[@id="wrap"]/div/div/div[2]/div[1]/article/div[3]/p[{line}]/strong')
    block_join = clear_syntax_mean(block)
    key_join = clear_syntax_key(key)
    list_key.append(key_join)
    list_mean.append(block_join)
    print(block_join,":",key_join)


for line in range(126,223):
    block = browser.find_element(By.XPATH,f'//*[@id="wrap"]/div/div/div[2]/div[1]/article/div[3]/p[{line}]')
    key = block.find_element(By.XPATH, f'//*[@id="wrap"]/div/div/div[2]/div[1]/article/div[3]/p[{line}]/strong')
    block_join = clear_syntax_mean(block)
    key_join = clear_syntax_key(key)
    list_key.append(key_join)
    list_mean.append(block_join)
    print(block_join,":",key_join)


sleep(1)
####################### About AI ###############################

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

######################## Deep Learning Word #######################
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
######################## Machine Learning Word #######################



# lists = [list_key, list_mean]
# lists_array = np.array(lists)
# list_data = lists_array.T
# data = pd.DataFrame(list_data, columns = ["Key","Mean"])
# data.to_csv("dict.csv")
# browser.close()x
