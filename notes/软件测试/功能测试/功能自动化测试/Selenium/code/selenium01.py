from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select, By
driver = webdriver.Chrome()

driver.get("https://www.baidu.com")

driver.find_element_by_id("")


driver.quit()