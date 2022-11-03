from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

s=Service("../Gmail/driver/chromedriver.exe")

driver = webdriver.Chrome(service=s)
driver.get("https://accounts.google.com/signup")
driver.maximize_window()
driver.implicitly_wait(5)
driver.find_element(By.XPATH,"//input[@aria-label='First name']").send_keys("hjyuugyu")
driver.find_element(By.CSS_SELECTOR,"input[aria-label='Last name']").send_keys("n")
driver.find_element(By.ID,"username").send_keys("askjdhfhfh.123")
driver.find_element(By.XPATH,"//input[@aria-label='Password']").send_keys("Dhoni@123")
driver.find_element(By.XPATH,"//input[@aria-label='Confirm']").send_keys("Dhoni@123")
driver.find_element(By.XPATH,"//input[@type='checkbox']").click()
driver.find_element(By.XPATH,"//span[normalize-space()='Next']").click()
driver.find_element(By.CLASS_NAME,"VfPpkd-fmcmS-wGMbrd ").send_keys("8667065272")

dropdown=Select(driver.find_element(By.XPATH,"//*[@id='month']"))
dropdown.select_by_visible_text("March")

#dropdown=Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
#dropdown.select_by_visible_text("Female")
#dropdown.select_by_index(1)
#dropdown.select by value()









