from selenium import webdriver

from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument('headless')
chrome_options.add_argument("--ignore-certificates-errors")

driver =
driver.get("https://rahulshettyacademy.com/angularpractice/")
print(driver.title)

