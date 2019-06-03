from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome()
driver.get("http://amazon.com")

elem=driver.find_element_by_name("field-keywords")
elem.clear()
elem.send_keys("laptops",Keys.ENTER)
driver.find_element_by_xpath("//*[text()='HP']").click()
