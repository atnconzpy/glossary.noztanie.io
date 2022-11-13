from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd
import os
#Open webdriver
browser = webdriver.Chrome(executable_path="D:/Python/I Just Wanna Test Python/assign/chromedriver.exe")
#Get link
list_key = []
list_mean = []
url = "https://tenten.vn/tin-tuc/200-thuat-ngu-crypto-va-blockhain/"
browser.get(url)
def clear_syntax_mean(m):
    block_text = str(m.text)
    block_list = list(block_text)
    del block_list[0 : block_list.index(":")+1]
    block_join = "".join(block_list)
    return block_join
def clear_syntax_key(n):
    key_text = str(n.text)
    key_list = list(key_text)
    del key_list[-1]
    key_join = "".join(key_list)
    return key_join
# line = browser.find_element(By.XPATH,'//*[@id="wrap"]/div/div/div[2]/div[1]/article/div[3]/p[188]')

# key = line.find_element(By.TAG_NAME,"strong")
# print(key.text)
for line in range(87,125):
    block = browser.find_element(By.XPATH,f'//*[@id="wrap"]/div/div/div[2]/div[1]/article/div[3]/p[{line}]')
    key = block.find_element(By.XPATH, f'//*[@id="wrap"]/div/div/div[2]/div[1]/article/div[3]/p[{line}]/strong')
    block_join = clear_syntax_mean(block)
    key_join = clear_syntax_key(key)
    key_text = str(key.text)
    key_list = list(key_text)
    print(key_list)

browser.close()