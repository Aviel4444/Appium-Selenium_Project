from selenium import webdriver
from selenium.webdriver.common.by import By
from Globals import Location


class HiltonHomePage:
    def __init__(self, driver:webdriver.Edge):
        self.driver = driver

    def search_destination(self):
        """press on the search box and put the location we want in hilton home page web"""
        search_destination = self.driver.find_element(By.NAME,"query")
        search_destination.send_keys(Location)

    def click_find_a_hotel(self):
        """press on find a hotel button"""
        find_hotel_button = self.driver.find_element(By.CLASS_NAME,"shop-form-btn-submit")
        find_hotel_button.click()

    def phone_number_text(self):
        """scrolling down the hilton home page web and returns the hilton hotel number with
        numbers and words"""
        phone_number = self.driver.find_element(By.CLASS_NAME,"uppercase")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", phone_number)
        return phone_number.text

