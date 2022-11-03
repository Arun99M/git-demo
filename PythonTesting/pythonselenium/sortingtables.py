from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
browserSortveggies=[]
service_obj = Service(r"C:\Users\ArunkumarM\Downloads\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
driver.find_element(By.XPATH,"//span[text()='Veg/fruit name']").click()
veggieWebElements = driver.find_elements(By.XPATH,"//tr/td[1]")
for ele in veggieWebElements:
    browserSortveggies.append(ele.text)

originalbrowserSortedList = browserSortveggies.copy()

browserSortveggies.sort()

assert browserSortveggies == originalbrowserSortedList












