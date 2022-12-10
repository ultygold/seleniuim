from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys

import time

browser = webdriver.Chrome(executable_path="chromedriver.exe")

browser.set_window_size(1920, 1080)

# browser.get("https://google.com/")

# logo = 'kwork.ru'

# browser.find_element(By.NAME, 'q').send_keys(logo)

# browser.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]').click()

# time.sleep(1)

# browser.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/div/div/div/div/div[1]/a/h3').click()

# time.sleep(1)

browser.get('https://github.com/')
time.sleep(3)

browser.find_element(By.XPATH, '/html/body/div[1]/div[1]/header/div/div[2]/div/div/div[2]/a').click()
time.sleep(3)
gold = "ultygold"
browser.find_element(By.XPATH, '/html/body/div[1]/div[3]/main/div/div[4]/form/input[2]').send_keys(gold)
time.sleep(3)
ulty = "AB@8bzWWD9rtGKi"
browser.find_element(By.XPATH, '/html/body/div[1]/div[3]/main/div/div[4]/form/div/input[1]').send_keys(ulty)

time.sleep(3)
browser.find_element(By.XPATH, '/html/body/div[1]/div[3]/main/div/div[4]/form/div/input[11]').click()

time.sleep(3)
browser.find_element(By.XPATH, '/html/body/div[1]/div[5]/div/aside/div/loading-context/div/div[1]/div/ul/li/div/div/a').click()
time.sleep(3)

browser.find_element(By.XPATH, '/html/body/div[1]/div[5]/div/main/turbo-frame/div/div/div/div[3]/div[1]/div[3]/div[3]/div[1]/div[5]/div[2]/span/a').click()
time.sleep(3)
