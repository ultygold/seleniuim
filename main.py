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
time.sleep(5)

browser.find_element(By.XPATH, '/html/body/div[1]/div[1]/header/div/div[2]/div/div/a').click()
time.sleep(6)
time.sleep(1)
asas = "qlichevasadbek@yandex.ru"

browser.find_element(By.XPATH, '/html/body/div[1]/div[4]/main/div[2]/text-suggester/div[1]/form/div[1]/div[2]/div/auto-check/input[1]').send_keys(asas)

