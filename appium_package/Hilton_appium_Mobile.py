from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from appium_package.Globals import capabilities_Pixel7b, Location
from appium_package.Globals import APP_HILTON
from appium import webdriver as app
from time import sleep

appium_server_url_local = 'http://localhost:4723/wd/hub'


class HiltonAppium:
    def __init__(self,driver):
        capabilities = {**capabilities_Pixel7b, **APP_HILTON}
        self.driver = app.Remote(appium_server_url_local, capabilities)
        self.wait = WebDriverWait(self.driver, 15)

    def prepare_for_testing(self):
        """pressing disallow notification and disallow permission when open the hilton app"""
        self.wait.until(EC.presence_of_element_located((AppiumBy.ID, 'com.android.permissioncontroller:id/permission_deny_button')))
        sleep(10)
        notification = self.driver.find_element(by=AppiumBy.ID,value='com.android.permissioncontroller:id/permission_deny_button')
        notification.click()

        self.wait.until(EC.presence_of_element_located((AppiumBy.ID, 'android:id/button2')))
        permission = self.driver.find_element(by=AppiumBy.ID, value='android:id/button2')
        permission.click()

    def put_location(self):
        """pressing the location search box and put the location we want to in hilton app"""
        search = self.driver.find_element(by=AppiumBy.XPATH,value='//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[1]/android.widget.Button')
        search.click()

        self.wait.until(EC.presence_of_element_located((AppiumBy.ID, 'com.hilton.android.hhonors:id/et_inner_locationfield')))
        put_location = self.driver.find_element(by=AppiumBy.ID,value='com.hilton.android.hhonors:id/et_inner_locationfield')
        put_location.send_keys(Location)

    def click_for_search(self):
        """press on the first option we get above the options we get in hilton app"""
        self.wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.hilton.android.hhonors:id/suggestion_text" and @text="Miami, Florida, USA"]')))
        location = self.driver.find_element(by=AppiumBy.XPATH,value='//android.widget.TextView[@resource-id="com.hilton.android.hhonors:id/suggestion_text" and @text="Miami, Florida, USA"]')
        location.click()

    def click_dates_later(self):
        """press on choose dates later in hilton app"""
        self.wait.until(EC.presence_of_element_located((AppiumBy.ID, 'com.hilton.android.hhonors:id/btn_dateless')))
        pick_dates_later = self.driver.find_element(by=AppiumBy.ID,value='com.hilton.android.hhonors:id/btn_dateless')
        pick_dates_later.click()

    def sort_options(self):
        """press on the sort option in hilton app"""
        self.wait.until(EC.presence_of_element_located((AppiumBy.ID, 'com.hilton.android.hhonors:id/action_sort_filter')))
        sort_options = self.driver.find_element(by=AppiumBy.ID,value='com.hilton.android.hhonors:id/action_sort_filter')
        sort_options.click()

    def get_lowest_price_text(self):
        """returns the lowest price text that the app offers"""
        self.wait.until(EC.presence_of_element_located((AppiumBy.ID, 'com.hilton.android.hhonors:id/price_min_value')))
        lowest_price_hotel = self.driver.find_element(by=AppiumBy.ID,value='com.hilton.android.hhonors:id/price_min_value')
        return lowest_price_hotel.text

    def get_highest_price_text(self):
        """returns the highest price text that the app offers"""
        self.wait.until(EC.presence_of_element_located((AppiumBy.ID, 'com.hilton.android.hhonors:id/price_max_value')))
        highest_price_hotel = self.driver.find_element(by=AppiumBy.ID,value='com.hilton.android.hhonors:id/price_max_value')
        return highest_price_hotel.text


    def click_help_button(self):
        """press on the help button at the menu in hilton app"""
        self.wait.until(EC.presence_of_element_located((AppiumBy.ID, 'com.hilton.android.hhonors:id/navigation_help')))
        help_button = self.driver.find_element(by=AppiumBy.ID,value='com.hilton.android.hhonors:id/navigation_help')
        help_button.click()

    def click_request_call(self):
        """press on request call in hilton app"""
        self.wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.ScrollView/android.view.View[4]/android.view.View[2]/android.widget.Button')))
        request_call = self.driver.find_element(by=AppiumBy.XPATH,value='//android.widget.ScrollView/android.view.View[4]/android.view.View[2]/android.widget.Button')
        request_call.click()

    def phone_number_in_hilton_text(self):
        """returns hilton phone number with numbers and words"""
        self.wait.until(EC.presence_of_element_located((AppiumBy.XPATH,'//android.widget.TextView[@text="+1-888-4HONORS"]')))
        phone_number = self.driver.find_element(by=AppiumBy.XPATH,value='//android.widget.TextView[@text="+1-888-4HONORS"]')
        return phone_number.text

    def click_phone_number(self):
        """click on hilton number in hilton app"""
        self.wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@text="+1-888-4HONORS"]')))
        phone_number = self.driver.find_element(by=AppiumBy.XPATH,value='//android.widget.TextView[@text="+1-888-4HONORS"]')
        phone_number.click()

    def phone_number_in_dialer_text(self):
        """returns hilton phone number with only numbers"""
        self.wait.until(EC.presence_of_element_located((AppiumBy.ID, 'com.google.android.dialer:id/digits')))
        phone_number_after = self.driver.find_element(by=AppiumBy.ID,value='com.google.android.dialer:id/digits')
        return phone_number_after.text

    def hotel_distance_text(self):
        """returns the distance of the first hotel"""
        self.wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.hilton.android.hhonors:id/tvDistanceFrom" and @text="0.82 miles away"]')))
        hotel_distance = self.driver.find_element(by=AppiumBy.XPATH,value='//android.widget.TextView[@resource-id="com.hilton.android.hhonors:id/tvDistanceFrom" and @text="0.82 miles away"]')
        hotel_distance_text = hotel_distance.text
        stop_index = hotel_distance_text.find(" ")
        return hotel_distance_text[0:stop_index]

    def click_on_first_hotel(self):
        """press on the first hotel in hilton app"""
        self.wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '(//android.view.View[@resource-id="com.hilton.android.hhonors:id/shade"])[1]')))
        hotel = self.driver.find_element(by=AppiumBy.XPATH,value='(//android.view.View[@resource-id="com.hilton.android.hhonors:id/shade"])[1]')
        hotel.click()

    def click_choose_room(self):
        """press on choose room button in hilton app"""
        self.wait.until(EC.presence_of_element_located((AppiumBy.ID, 'com.hilton.android.hhonors:id/btn_continue')))
        choose_room = self.driver.find_element(by=AppiumBy.ID,value='com.hilton.android.hhonors:id/btn_continue')
        choose_room.click()

    def hotel_name_text(self):
        """returns the name of the hotel we chose"""
        self.wait.until(EC.presence_of_element_located((AppiumBy.ID, 'com.hilton.android.hhonors:id/tv_title')))
        hotel_name = self.driver.find_element(by=AppiumBy.ID,value='com.hilton.android.hhonors:id/tv_title')
        return hotel_name.text

    def click_on_search_location(self):
        """press on search location button in hilton app"""
        self.wait.until(EC.presence_of_element_located((AppiumBy.ID, 'com.hilton.android.hhonors:id/btnMap')))
        location = self.driver.find_element(by=AppiumBy.ID,value='com.hilton.android.hhonors:id/btnMap')
        location.click()

    def hotel_address_text(self):
        """returns the address of the hotel we chose"""
        self.wait.until(EC.presence_of_element_located((AppiumBy.ID, 'com.hilton.android.hhonors:id/location_address')))
        hotel_address = self.driver.find_element(by=AppiumBy.ID,value='com.hilton.android.hhonors:id/location_address')
        return hotel_address.text
