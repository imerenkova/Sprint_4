from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.main_page_locators import MainPageLocators
from methods import *


class MainPageScooter:

    def __init__(self, driver):
        self.driver = driver
        self.close_cookie_form()
        self.wait_close_cookie_form()

    def wait_for_load_main_page(self):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.MAIN_PAGE))

    def close_cookie_form(self):
        self.driver.find_element(*MainPageLocators.COOKIE_FORM).click()

    def wait_close_cookie_form(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.invisibility_of_element(MainPageLocators.COOKIE_FORM))

    def scroll_to(self, method, locator):
        element = self.driver.find_element(method, locator)
        return self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def wait_FAQ_section(self):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.FAQ_SECTION))

    def click_question(self, num):
        # индексация с 0, но в тесте для удобства с 1
        self.driver.find_element(*transform(*MainPageLocators.QUESTION, num - 1)).click()

    def text_question(self, num):
        return self.driver.find_element(*transform(*MainPageLocators.QUESTION, num - 1)).text

    def text_answer(self, num):
        # индексация с 0, но в тесте для удобства с 1
        return self.driver.find_element(*transform(*MainPageLocators.ANSWER, num - 1)).text

    def wait_text_answer(self, num):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(transform(*MainPageLocators.ANSWER, num - 1)))

    def click_order_button_on_mail_page(self):
        self.driver.find_element(*MainPageLocators.MAIN_PAGE_ORDER_BUTTON).click()

    def wait_order_button_on_mail_page(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.MAIN_PAGE_ORDER_BUTTON))
