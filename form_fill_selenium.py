from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys

url = 'http://www.webscrapingfordatascience.com/postform2/'
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get(url)
driver.find_element(By.NAME,'name').send_keys('Seppely')
driver.find_element(By.CSS_SELECTOR,'input[name="gender"][value="M"]').click()
driver.find_element(By.NAME,'pizza').click()
driver.find_element(By.NAME,'salad').click()
Select(driver.find_element(By.NAME,'haircolor')).select_by_value('brown')
driver.find_element(By.NAME,'comments').send_keys(['First line', Keys.ENTER, 'Second line'])
input('Press ENTER to submit the form')
driver.find_element(By.TAG_NAME,'form').submit()
# Or: driver.find_element_by_css_selector('input[type="submit"]').click()
input('Press ENTER to close the automated browser')
driver.quit()