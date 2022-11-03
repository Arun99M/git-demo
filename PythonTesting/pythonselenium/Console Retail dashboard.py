import time

from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service(r"C:\Users\ArunkumarM\Downloads\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://console.bolt.earth/")
driver.find_element(By.ID,"mui-1").send_keys("tester@revos.in")
driver.find_element(By.CSS_SELECTOR,"input[name='password']").send_keys("ah123cd@")
driver.find_element(By.XPATH,"//button[@type='submit']").click()
driver.find_element(By.XPATH,"//button[@aria-label='Switch to...']//*[name()='svg']").click()
driver.find_element(By.XPATH,"//ul[@class='MuiList-root MuiList-padding css-1ontqvh']/div[1]").click()
driver.find_element(By.CSS_SELECTOR,"a[aria-label='Assembly']").click()
driver.find_element(By.XPATH,"//button[@aria-label='Add Model']").click()
driver.find_element(By.XPATH,"//input[@placeholder='Model Name']").send_keys("thunderbird")
driver.find_element(By.XPATH,"/html/body/div[4]/div[3]/div/div[1]/div[2]/div/div[2]/div/div").click()
driver.find_element(By.XPATH,"//li[@data-value='PNP']").click()
#driver.find_element(By.XPATH,"/html/body/div[6]/div[3]/div/div[1]/div[2]/div/div[3]/div").click()
driver.find_element(By.CLASS_NAME,"MuiInputBase-root MuiOutlinedInput-root MuiInputBase-colorPrimary MuiInputBase-fullWidth MuiInputBase-sizeSmall  css-1nkies2").click()












