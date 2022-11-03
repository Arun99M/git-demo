from selenium import webdriver

# chrome diver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service(r"C:\Users\ArunkumarM\Downloads\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/angularpractice/")
#ID,XPATH,CSSELECTOR,NAME,CLASSNAME,LINKTEXT
driver.find_element(By.NAME,"name").send_keys("arun")
driver.find_element(By.NAME,"email").send_keys("hello@gmail.com")
driver.find_element(By.ID,"exampleInputPassword1").send_keys("123456")
driver.find_element(By.ID,"exampleCheck1").click()

#Xpath-//tagname[@attribute='vale'] ->  //input[@type='submit']
#CSS - tagname[attribute='vale] ->  input[type='submit]
#driver.find_element(By.CSS_SELECTOR,"input[name='name']").send_keys("rahul")
#driver.find_element(By.CSS_SELECTOR,"#inlineRadio1").click()

#static dropdown
dropdown=Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(1)
#dropdown.select by value()















