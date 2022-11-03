import time


from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


service_obj = Service(r"C:\Users\ArunkumarM\Downloads\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://console.bolt.earth/")
#driver.find_element(By.NAME,"email").send_keys("tester@revos.in")
driver.find_element(By.ID,"mui-1").send_keys("tester@revos.in")
#driver.find_element(By.NAME,"password").send_keys("ah123cd@")
driver.find_element(By.CSS_SELECTOR,"input[name='password']").send_keys("ah123cd@")
driver.find_element(By.XPATH,"//button[@type='submit']").click()
#time.sleep(2)
driver.find_element(By.XPATH,"//button[@aria-label='Switch to...']//*[name()='svg']").click()
#driver.find_element(By.CSS_SELECTOR,"//div[@class='MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation8 MuiPopover-paper css-1bq7khx']").click()
driver.find_element(By.XPATH,"//ul[@class='MuiList-root MuiList-padding css-1ontqvh']/div[1]").click()
driver.find_element(By.CSS_SELECTOR,"a[aria-label='Distribution']").click()
driver.find_element(By.CSS_SELECTOR,".MuiButtonBase-root.MuiButton-root.MuiButton-contained.MuiButton-containedPrimary.MuiButton-sizeMedium.MuiButton-containedSizeMedium.css-107goid").click()
driver.find_element(By.CSS_SELECTOR,"input[placeholder='Company Name']").send_keys("virat")
driver.find_element(By.CSS_SELECTOR,"input[placeholder='GST Number']").send_keys("234Ab238777877")
driver.find_element(By.XPATH,"//input[@placeholder='Phone Number']").send_keys("8667065272")
driver.find_element(By.XPATH,"//input[@placeholder='Address']").send_keys("BCCME")
driver.find_element(By.CSS_SELECTOR,"input[placeholder='City/District']").send_keys("Bangalkote")
driver.find_element(By.XPATH,"//input[@placeholder='State']").send_keys("Karnataka")
driver.find_element(By.XPATH,"//input[@placeholder='Pincode']").send_keys("735110")
time.sleep(2)
#driver.find_element(By.XPATH,"//button[contains(text(),'Next')]").click()
driver.find_element(By.XPATH,"//div[@class='MuiDialogActions-root MuiDialogActions-spacing css-14b29qc']//span").click()

#driver.find_element(By.XPATH,"//input[@placeholder='First Name']").send_keys("Akumar")
#driver.find_element(By.XPATH,"//input[@placholder='Last Name']").send_keys("M")
#driver.find_element(By.XPATH,"//input[@placholder='Phone']").send_keys("8667065252")
#driver.find_element(By.XPATH,"//input[@placholder='Email']").send_keys("ak1234@gmail.com")
#driver.find_element(By.XPATH,"//input[@placholder='Password']").send_keys("bolt@123")
#driver.find_element(By.XPATH,"//input[@placholder='Confirm']").send_keys("bolt@123")
#checkbox=driver.find_element(By.XPATH,"//input[@type='checkbox']")
#print(len(radiobuttons))

#if radio button not changing its position means we have to use below one.
#radiobuttons[2].click()
#assert radiobuttons[2].is_selected()
#driver.find_element(By.ID,"displayed-text").is_displayed()
#driver.find_element(By.ID,"hide-textbox").click()

















