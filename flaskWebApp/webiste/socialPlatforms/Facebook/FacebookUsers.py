from configparser import ConfigParser
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep, time

class FacebookData:

    def __init__(self, config_path):
        self.config_path = config_path

    def get_credentials(self):
        myconfig = ConfigParser()
        # myconfig.read('webiste/socialPlatforms/Instagram/config.ini')
        myconfig.read(self.config_path)
        username = myconfig['API']['USERNAME']
        password = myconfig['API']['PASSWORD']
        return username, password

    def get_users(targetName, self):
        userName, passWord = FacebookData.get_credentials(self)
        chrome_options = webdriver.ChromeOptions()
        prefs = {"profile.default_content_setting_values.notifications": 2}
        chrome_options.add_experimental_option("prefs", prefs)
        driver = webdriver.Chrome('C:/Users/goaim/chromedriver.exe', chrome_options=chrome_options)
        driver.get("http://www.facebook.com")
        username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='email']")))
        password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='pass']")))
        username.clear()
        username.send_keys(str(userName))
        password.clear()
        password.send_keys(str(passWord))
        button = WebDriverWait(driver, 2).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()

        # We are logged in!
        sleep(2)
        searchbox = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@type='search']")))
        searchbox.clear()
        # keyword = "narendra modi"
        searchbox.send_keys(targetName)
        searchbox.send_keys(Keys.ENTER)
        url = f'https://www.facebook.com/search/top?q={targetName}'
        driver.get(url)
        # time.sleep(5)
        anchors = driver.find_elements(By.TAG_NAME, 'a')
        names_list = []
        ref_list = []
        for a in anchors:
            link = a.get_attribute('href')
            if str(link).endswith('__tn__=%3C'):
                names_list.append(a.get_attribute('aria-label'))
                ref_list.append(a.get_attribute('href'))
        print(ref_list)
        print(names_list)
        return ref_list, names_list




