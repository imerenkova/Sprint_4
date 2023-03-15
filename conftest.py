import pytest as pytest
from selenium import webdriver


@pytest.fixture(scope='function')
def driver():
    firefox_options = webdriver.FirefoxOptions()
    firefox_options.add_argument('--window-size=1440,900')
    driver = webdriver.Firefox(options=firefox_options)
    driver.get('https://qa-scooter.praktikum-services.ru/')
    yield driver
    driver.quit()
