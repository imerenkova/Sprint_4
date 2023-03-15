from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.order_page_locators import OrderPageLocators
from methods import *


class OrderScooterPage:

    def __init__(self, driver):
        self.driver = driver

    def wait_for_order_form(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(OrderPageLocators.ORDER_FORM))

    def set_name(self, name):
        self.driver.find_element(*OrderPageLocators.FIELD_NAME_IN_ORDER).send_keys(name)

    def set_surname(self, name):
        self.driver.find_element(*OrderPageLocators.FIELD_SURNAME_IN_ORDER).send_keys(name)

    def set_address(self, text):
        self.driver.find_element(*OrderPageLocators.FIELD_ADDRESS_IN_ORDER).send_keys(text)

    def set_metro(self, metro_station):
        ac = ActionChains(self.driver)
        element = self.driver.find_element(*OrderPageLocators.FIELD_METRO_IN_ORDER)
        ac.click(element)
        ac.send_keys(metro_station)
        ac.perform()
        method, locator = OrderPageLocators.METRO_STATION
        locator = locator.format(metro_station)
        station = self.driver.find_element(method, locator)
        ac.send_keys_to_element(station).perform()

    def set_phone(self, phone_number):
        self.driver.find_element(*OrderPageLocators.FIELD_PHONE_IN_ORDER).send_keys(phone_number)

    def go_forward(self):
        self.driver.find_element(*OrderPageLocators.NEXT_STEP_BUTTON).click()

    def choose_start_date_rent(self, date):
        self.driver.find_element(*OrderPageLocators.FIELD_DATE_RENT_IN_ORDER).click()
        self.driver.find_element(*transform(*OrderPageLocators.DATE_FROM_CALENDAR, date)).click()

    def wait_order_form_about_rent(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(OrderPageLocators.ABOUT_RENT))

    def choose_rental_period(self, period):
        self.driver.find_element(*OrderPageLocators.FIELD_RENTAL_PERIOD_IN_ORDER).click()
        self.driver.find_element(*transform(*OrderPageLocators.RENTAL_PERIOD_VARIANT, period)).click()

    def set_scooter_color(self, color):
        self.driver.find_element(*transform(*OrderPageLocators.FIELD_COLOR_SCOOTER_IN_ORDER, color)).click()

    def set_comment(self, text):
        self.driver.find_element(*transform(*OrderPageLocators.FIELD_COMMENT_IN_ORDER, text)).send_keys(text)

    def click_buttton(self, button):
        self.driver.find_element(*transform(*OrderPageLocators.BUTTON_UNDER_ORDER, button)).click()

    def wait_modal_window(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(OrderPageLocators.MODAL_WINDOW_ORDER))

    def text_modal_window(self):
        return self.driver.find_element(*OrderPageLocators.MODAL_WINDOW_ORDER).text

    def fill_first_part_order(self, name, surname, address, metro_station, phone_number):
        self.set_name(name)
        self.set_surname(surname)
        self.set_address(address)
        self.set_metro(metro_station)
        self.set_phone(phone_number)

    def fill_second_part_order(self, date, rental_period, color, comment):
        self.choose_start_date_rent(date)
        self.choose_rental_period(rental_period)
        self.set_scooter_color(color)
        self.set_comment(comment)
