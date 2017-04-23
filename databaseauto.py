from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome('/users/VANXV/downloads/chromedriver')
driver.get("https://business.facebook.com/home/accounts?business_id=1015408745240297")
#driver = webdriver.PhantomJS('/users/VANXV/downloads/phantomjs211/bin/phantomjs')
#driver.get("https://ps.rsd.edu/public/")
assert "facebook" in driver.title
elem = driver.find_element_by_name("placeholder")
elem.send_keys("ironvanxv@gmail.com")
elem = driver.find_element_by_name("placeholder")
elem.send_keys("1q2w3e4r")
elem = driver.find_element_by_name("pass_again")
elem.send_keys("1q2w3e4r")
#elem.send_keys(Keys.RETURN)
elem = driver.find_element_by_name("phone_num")
elem.send_keys("18606622210")
elem = driver.find_element_by_id("year_value").click()

#
#driver.find_element_by_name("month_value")
driver.find_element_by_id("submit").click()
assert "QQ." not in driver.page_source
#driver.quit()

#elem = driver.find_element_by_name("account")
#elem.send_keys("aa")
#elem2 = driver.find_element_by_name("pw")
#elem2.send_keys("bb")
#elem.send_keys(Keys.RETURN)

#driver.quit()