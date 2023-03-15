from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.base_page_locators import HeaderPageLocators


class HeaderPageScooter:

    def __init__(self, driver):
        self.driver = driver

    def click_logo_yandex(self):
        self.driver.find_element(*HeaderPageLocators.LOGO_YANDEX).click()

    def click_logo_scooter(self):
        self.driver.find_element(*HeaderPageLocators.LOGO_SCOOTER).click()

    def click_order_button_header(self):
        self.driver.find_element(*HeaderPageLocators.HEADER_ORDER_BUTTON).click()

    def click_button_state_order(self):
        self.driver.find_element(*HeaderPageLocators.HEADER_STATE_ORDER_BUTTON).click()

    def get_current_url(self):
        return self.driver.current_url

    def wait_load_ya_dzen(self):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(HeaderPageLocators.YA_DZEN))
