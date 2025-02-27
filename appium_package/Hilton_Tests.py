from unittest import TestCase
from appium import webdriver as app
from selenium import webdriver as web
from selenium.webdriver.ie.service import Service
from Hilton_Home_Page_Web import HiltonHomePage
from Hilton_Hotel_Page_Web import HiltonHotelPage
from Hilton_Hotel_Details_Page_Web import HiltonHotelDetailsPage
from Hilton_appium_Mobile import HiltonAppium
from Dial_appium_Mobile import DialAppium
from Globals import capabilities_Pixel7b,HILTON_URL,APPIUM_SERVER
from time import sleep


class Tests(TestCase):
    def setUp(self):
        service = Service(executable_path='path/to/edgedriver')
        self.driver = web.Edge (service=service)
        self.driver.get(HILTON_URL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)

        self.hilton_home_page = HiltonHomePage(self.driver)
        self.hilton_hotel_page = HiltonHotelPage(self.driver)
        self.hilton_hotel_details_page = HiltonHotelDetailsPage(self.driver)

        capabilities = {**capabilities_Pixel7b}
        self.mobile_driver = app.Remote(APPIUM_SERVER, capabilities)
        self.mobile_driver.implicitly_wait(20)



    def test_lowest_price_app_and_web(self):
        """Testing if the lowest price hotel at miami in the web and in the app are not same"""
        self.hilton_appium = HiltonAppium(self.mobile_driver)

        self.hilton_home_page.search_destination()
        self.hilton_home_page.click_find_a_hotel()
        self.hilton_hotel_page.sort_by_price_low_to_high()
        website_lowest_price = self.hilton_hotel_page.get_lowest_price_hotel_text(0)
        print(f"website lowest hotel price is: {website_lowest_price}$")

        self.hilton_appium.prepare_for_testing()
        self.hilton_appium.put_location()
        self.hilton_appium.click_for_search()
        self.hilton_appium.click_dates_later()
        self.hilton_appium.sort_options()
        app_lowest_price = self.hilton_appium.get_lowest_price_text()
        print(f"app lowest hotel price: {app_lowest_price}$")

        self.assertEqual(app_lowest_price, website_lowest_price,"the lowest price miami hotel in the web and in the app are not the same")


    def test_highest_price_app_and_web(self):
        """Testing if the highest price hotel at miami in the web and in the app are equals"""
        self.hilton_appium = HiltonAppium(self.mobile_driver)

        self.hilton_home_page.search_destination()
        self.hilton_home_page.click_find_a_hotel()
        self.hilton_hotel_page.sort_by_price_high_to_low()
        website_highest_price = self.hilton_hotel_page.get_highest_price_hotel_text(0)
        print(f"website highest hotel price is: {website_highest_price}$")

        self.hilton_appium.prepare_for_testing()
        self.hilton_appium.put_location()
        self.hilton_appium.click_for_search()
        self.hilton_appium.click_dates_later()
        self.hilton_appium.sort_options()
        app_highest_price = self.hilton_appium.get_highest_price_text()
        print(f"app highest hotel price: {app_highest_price}$")

        self.assertEqual(app_highest_price, website_highest_price,"the highest price miami hotel in the web and in the app are not the same")


    def test_phone_number_app_and_web(self):
        """testing if the 'hilton hotel' number is the same in the web and in the app"""
        self.hilton_appium = HiltonAppium(self.mobile_driver)

        website_phone_number = self.hilton_home_page.phone_number_text()
        print(f"website phone number is: {website_phone_number}")

        self.hilton_appium.prepare_for_testing()
        self.hilton_appium.click_help_button()
        self.hilton_appium.click_request_call()
        app_phone_number = self.hilton_appium.phone_number_in_hilton_text()
        print(f"app phone number is: {app_phone_number}")

        self.assertEqual(app_phone_number, website_phone_number, "the phone number in the web and in the app are not the same")


    def test_hotel_distance_app_and_web(self):
        """testing if the distance of the first hotel option at miami is the same in the app and in the web"""
        self.hilton_appium = HiltonAppium(self.mobile_driver)

        self.hilton_home_page.search_destination()
        self.hilton_home_page.click_find_a_hotel()
        web_hotel_distance = self.hilton_hotel_page.get_hotel_distance_text(6)
        print(f"website hotel distance is: {web_hotel_distance} miles")

        self.hilton_appium.prepare_for_testing()
        self.hilton_appium.put_location()
        self.hilton_appium.click_for_search()
        self.hilton_appium.click_dates_later()
        app_hotel_distance = self.hilton_appium.hotel_distance_text()
        print(f"app hotel distance is: {app_hotel_distance} miles")

        self.assertEqual(web_hotel_distance, app_hotel_distance, "the distance of a specific hotel in the web and in the app are not the same")


    def test_hotel_address(self):
        """Testing if the hotel's name at Miami we picked is the same on the web and in the app,and if they are, we check if their addresses are the same"""
        self.hilton_appium = HiltonAppium(self.mobile_driver)

        original_window = self.hilton_home_page.driver.current_window_handle #gets the current window we are at
        self.hilton_home_page.search_destination()
        self.hilton_home_page.click_find_a_hotel()
        web_hotel_name = self.hilton_hotel_page.get_hotel_name_text(0)
        print(f"The hotel name we picked on the website is: {web_hotel_name}")
        self.hilton_hotel_page.click_select_dates(0)
        self.hilton_hotel_page.choose_date()
        self.hilton_hotel_page.click_choose_room()

        while len(self.hilton_home_page.driver.window_handles) == 1: #while the total number of windows is one, wait 1 second till new window opens
            sleep(1)
        for window_handle in self.hilton_home_page.driver.window_handles: #if we are at the new window, break
            if window_handle != original_window:
                self.hilton_home_page.driver.switch_to.window(window_handle)
                break

        web_hotel_address = self.hilton_hotel_details_page.hotel_address_text()
        print(f"The hotel address we picked on the website is: {web_hotel_address}")

        self.hilton_appium.prepare_for_testing()
        self.hilton_appium.put_location()
        self.hilton_appium.click_for_search()
        self.hilton_appium.click_dates_later()
        self.hilton_appium.click_on_first_hotel()
        self.hilton_appium.click_choose_room()
        app_hotel_name = self.hilton_appium.hotel_name_text()
        print(f"the hotel name we picked in the app is: {app_hotel_name}")
        self.hilton_appium.click_on_search_location()
        app_hotel_address = self.hilton_appium.hotel_address_text()
        print(f"the hotel address we picked in the app is: {app_hotel_address}")

        if web_hotel_name == app_hotel_name:  #if the hotel name we picked in the web equal the hotel name we picked in the app, compare their addresses
            self.assertEqual(web_hotel_address, app_hotel_address,"the addresses of the hotel in the app and in the web are not the same")
        else:
            print("we picked different hotels")


    def test_call_phone_number(self):
        """testing if the 'hilton hotel' number in the app is the same as the number we put in the dialer,and if they are,we will call this number"""
        self.hilton_appium = HiltonAppium(self.mobile_driver)

        self.hilton_appium.prepare_for_testing()
        self.hilton_appium.click_help_button()
        self.hilton_appium.click_request_call()
        self.hilton_appium.click_phone_number()
        hilton_app_phone_number = self.hilton_appium.phone_number_in_dialer_text()

        self.dial_appium = DialAppium(self.mobile_driver)

        self.dial_appium.go_to_numbers_pane()
        self.dial_appium.click_numbers()
        dial_app_phone_number = self.dial_appium.full_number_text()

        if hilton_app_phone_number == dial_app_phone_number: #if the phone number from hilton app is the same as the number we typed in dialer, call the phone
            self.dial_appium.click_call()
        else:
            print("the numbers are not the same")



    def tearDown(self):
        self.driver.close()
        self.mobile_driver.quit()

