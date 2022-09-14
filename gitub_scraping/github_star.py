import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from repo_details import RepoDetails


drive = webdriver.Chrome("chromedriver.exe")



## spoken language
def spoken_language_set():
    url = "https://github.com/trending"
    drive.get(url)
    drive.implicitly_wait(10)
    drive.find_element(By.CLASS_NAME, 'text-bold').click()
    language_element = drive.find_element(By.ID, "text-filter-field-spoken-language")
    action = ActionChains(driver=drive)
    time.sleep(2)
    action.click(language_element).send_keys('English').key_down(Keys.ENTER).key_up(Keys.ENTER).perform()

# programming language
def programming_set():
    url = "https://github.com/trending?spoken_language_code=en"
    drive.get(url)
    drive.implicitly_wait(10)
    drive.find_element(By.ID, 'select-menu-language').click()
    language_element = drive.find_element(By.CLASS_NAME, "select-menu-text-filter")
    action = ActionChains(driver=drive)
    time.sleep(5)
    action.click(language_element).send_keys('Python').key_down(Keys.ENTER).key_up(Keys.ENTER).perform()


def repo_getter():
    spoken_language_set()
    time.sleep(10)
    programming_set()
    result = RepoDetails()
    links = result.repo_link()
    stars = result.repo_stars()
    for link,star in zip(links, stars):
        print(link+"---->"+star)


repo_getter()
input("Press ENter to exit")
drive.quit()

