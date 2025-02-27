from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep

class HiltonHotelPage:
    def __init__(self, driver:webdriver.Edge):
        self.driver = driver

    def sort_by_price_low_to_high(self):
        """sort the hotels by low to high price in the hilton hotel page web"""
        sort = self.driver.find_element(By.ID,"selectSortBy")
        sort_drop = Select(sort)
        sort_drop.select_by_visible_text("Price: low-high")

    def sort_by_price_high_to_low(self):
        """sort the hotels by high to low price in the hilton hotel page web"""
        sort = self.driver.find_element(By.ID,"selectSortBy")
        sort_drop = Select(sort)
        sort_drop.select_by_visible_text("Price: high-low")

    def get_lowest_price_hotel_text(self, index):
        """returns the lowest price of hotel in the hilton hotel page web"""
        lowest_price = self.driver.find_elements(By.CLASS_NAME,"text-lg")
        return lowest_price[index].text[1:]

    def get_highest_price_hotel_text(self, index):
        """returns the highest price of hotel in the hilton hotel page web"""
        highest_price = self.driver.find_elements(By.CLASS_NAME,"text-lg")
        return highest_price[index].text[1:]

    def get_hotel_distance_text(self, index):
        """returns the distance of the hotel based on index in the hilton hotel page web"""
        sleep(10)
        distances = self.driver.find_elements(By.CLASS_NAME,"whitespace-nowrap")
        distance_text = distances[index].text
        stop_index = distance_text.find(" ")
        return distance_text[0:stop_index]

    def get_hotel_name_text(self, index):
        """returns the hotel name based on index in the hilton hotel page web"""
        sleep(10)
        hotels = self.driver.find_elements(By.CLASS_NAME,"break-words")
        hotel = hotels[index]
        return hotel.text

    def click_select_dates(self, index):
        """press on select dates button in the hilton hotel page web"""
        buttons = self.driver.find_elements(By.CLASS_NAME,"btn-primary")
        select_date_button = buttons[index]
        select_date_button.click()

    def choose_date(self):
        """scroll down the calendar and press on random available date in the hilton hotel page web"""
        sleep(10)
        dates = self.driver.find_elements(By.CLASS_NAME, "ring-inset")
        date = dates[27]
        self.driver.execute_script("arguments[0].scrollIntoView(true);", date)
        date.click()

    def click_choose_room(self):
        """press on choose room button in the hilton hotel page web"""
        choose_room = self.driver.find_elements(By.CLASS_NAME,"btn-xl")
        choose_room_button = choose_room[1]
        choose_room_button.click()





