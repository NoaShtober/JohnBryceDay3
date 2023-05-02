from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

class welcomePage(object):

    def __init__(self, driver):
        self.driver = driver

    def Welcome(self):
        prices = self.driver.find_elements(By.CLASS_NAME, "inventory_item_price")
        return prices


    def send_keys_over_element(self, element, pattern):
        element.click()
        element.clear()
        element.send_keys(pattern)
