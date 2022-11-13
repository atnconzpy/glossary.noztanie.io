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

browser.close()