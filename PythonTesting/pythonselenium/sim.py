from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj =Service(r"C:\Users\ArunkumarM\Downloads\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)
driver.get("https://www.airtel.in/m2m/login/")
driver.maximize_window()
driver.find_element(By.NAME,"cmp_login_email_id").send_keys("finance@revos.in")
driver.find_element(By.ID,"cmp_login_email_password").send_keys("Ah1@rocks")
driver.find_element(By.ID,"login_button").click()
driver.find_element(By.XPATH,"//input[@placeholder='Search by MSISDN, SIM Number, IMSI']").send_keys("70565")
driver.find_element(By.XPATH,"//div[@class='arrow']//span[@class='iot-arrowright']").click()
driver.find_element(By.XPATH,"//div[@class='col-md-3 col-lg-3 col-sm-3 pd-0']//select[@class='select-option ng-untouched ng-pristine ng-valid']").send_keys("SIM NO")
driver.find_element(By.ID,"basket-search-input").send_keys("70565")
driver.find_element(By.XPATH,"//input[@name='selectAllCheckBox']").click()
















