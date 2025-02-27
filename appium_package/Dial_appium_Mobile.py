from appium.webdriver.common.appiumby import AppiumBy
from appium_package.Globals import capabilities_Pixel7b
from appium_package.Globals import APP_DIALER
from appium import webdriver as app
from appium.webdriver.common.touch_action import TouchAction

appium_server_url_local = 'http://localhost:4723/wd/hub'


class DialAppium:
    def __init__(self, driver):
        capabilities = {**capabilities_Pixel7b, **APP_DIALER}
        self.driver = app.Remote(appium_server_url_local, capabilities)

    def go_to_numbers_pane(self):
        """going to the dialer numbers in the dialer app"""
        numbers = self.driver.find_element(by=AppiumBy.ID,value='com.google.android.dialer:id/dialpad_fab')
        numbers.click()

    def click_numbers(self):
        """pressing the numbers for making phone number in the dialer app"""
        number1 = self.driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@resource-id="com.google.android.dialer:id/dialpad_key_letters" and @text="+"]')
        TouchAction(self.driver).long_press(number1).release().perform()

        number2 = self.driver.find_element(by=AppiumBy.ID, value='com.google.android.dialer:id/one')
        number2.click()

        number3 = self.driver.find_element(by=AppiumBy.ID, value='com.google.android.dialer:id/eight')
        number3.click()

        number4 = self.driver.find_element(by=AppiumBy.ID, value='com.google.android.dialer:id/eight')
        number4.click()

        number5 = self.driver.find_element(by=AppiumBy.ID, value='com.google.android.dialer:id/eight')
        number5.click()

        number6 = self.driver.find_element(by=AppiumBy.ID, value='com.google.android.dialer:id/four')
        number6.click()

        number7 = self.driver.find_element(by=AppiumBy.ID, value='com.google.android.dialer:id/four')
        number7.click()

        number8 = self.driver.find_element(by=AppiumBy.ID, value='com.google.android.dialer:id/six')
        number8.click()

        number9 = self.driver.find_element(by=AppiumBy.ID, value='com.google.android.dialer:id/six')
        number9.click()

        number10 = self.driver.find_element(by=AppiumBy.ID, value='com.google.android.dialer:id/six')
        number10.click()

        number11 = self.driver.find_element(by=AppiumBy.ID, value='com.google.android.dialer:id/seven')
        number11.click()

        number12 = self.driver.find_element(by=AppiumBy.ID, value='com.google.android.dialer:id/seven')
        number12.click()

    def full_number_text(self):
        """returns the full number we typed"""
        full_number = self.driver.find_element(by=AppiumBy.ID, value='com.google.android.dialer:id/digits')
        return full_number.text

    def click_call(self):
        """press the call button in the dialer app"""
        call = self.driver.find_element(by=AppiumBy.ID,value='com.google.android.dialer:id/dialpad_voice_call_button')
        call.click()







