import time

from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service(r"C:\Users\ArunkumarM\Downloads\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://staging.revos.in/")
#driver.find_element(By.NAME,"email").send_keys("tester@revos.in")
driver.find_element(By.ID,"mui-1").send_keys("tester@revos.in")
#driver.find_element(By.NAME,"password").send_keys("ah123cd@")
driver.find_element(By.CSS_SELECTOR,"input[name='password']").send_keys("ah123cd@")
driver.find_element(By.XPATH,"//button[@type='submit']").click()
#time.sleep(2)
driver.find_element(By.XPATH,"//button[@aria-label='Switch to...']//*[name()='svg']").click()
#driver.find_element(By.CSS_SELECTOR,"//div[@class='MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation8 MuiPopover-paper css-1bq7khx']").click()
driver.find_element(By.XPATH,"//ul[@class='MuiList-root MuiList-padding css-1ontqvh']/div[1]").click()
#driver.find_element(By.XPATH,"//ul[@class='MuiList-root MuiList-padding css-1ontqvh']/div[2]").click()
driver.find_element(By.CSS_SELECTOR,"a[aria-label='Assembly']").click()
driver.find_element(By.XPATH,"//button[@aria-label='Add Model']").click()
driver.find_element(By.XPATH,"//div[@class='MuiFormControl-root MuiFormControl-fullWidth MuiTextField-root css-feqhe6']/div/input").send_keys("thunderbird")
dropdown=Select(driver.find_element(By.CLASS_NAME,'MuiInputBase-root MuiOutlinedInput-root MuiInputBase-colorPrimary MuiInputBase-fullWidth Mui-focused MuiInputBase-sizeSmall  css-1nkies2')).click()
dropdown=Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
#dropdown.select_by_visible_text("Female")














