import selenium
import selenium.webdriver.edge.options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

options = selenium.webdriver.edge.options.Options()
driver = selenium.webdriver.Edge(options=options)
driver.get("http://www.shawnee.edu")
searchLink = driver.find_element(By.CLASS_NAME, "search-open")
searchLink.click()
textbox = driver.find_element(By.ID, "edit-keys")
textbox.send_keys("gaming" + Keys.ENTER)

time.sleep(3)       #just for humans to see what's happened
driver.quit()