from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service(r"C:\Users\ArunkumarM\Downloads\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
radiobuttons=driver.find_elements(By.XPATH,"//input[@type='radio']")
print(len(radiobuttons))

#if radio button not changing its position means we have to use below one.
radiobuttons[2].click()
assert radiobuttons[2].is_selected()
driver.find_element(By.ID,"displayed-text").is_displayed()
driver.find_element(By.ID,"hide-textbox").click()




#if posistion is changing then follow same as per chexkbox

#for radiobutton in radiobuttons:
 #   if radiobutton.get_attribute("value") == "radio2":
  #      radiobutton.click()
   #     assert radiobutton.is_selected()
    #    break












