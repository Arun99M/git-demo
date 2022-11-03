import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj=Service(r"C:\Users\ArunkumarM\Downloads\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(3)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")

# //a[contains(@href,'shop')]    a[href*='shop']

driver.find_element(By.CSS_SELECTOR,"a[href*='shop']").click()
driver.minimize_window()






















