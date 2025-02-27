from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class HiltonHotelDetailsPage:
    def __init__(self, driver:webdriver.Edge):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)

    def hotel_address_text(self):
        """returns the address of the hotel we chose"""
        self.wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "whitespace-pre-line")))
        addresses = self.driver.find_elements(By.CLASS_NAME, "whitespace-pre-line")
        hotel_address = addresses[0]
        return hotel_address.text

