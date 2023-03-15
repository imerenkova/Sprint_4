from selenium.webdriver.common.by import By


class HeaderPageLocators:
    # Логотип "Яндекс" вверху страницы
    LOGO_YANDEX = By.XPATH, '//a[@href="//yandex.ru"]'
    # Логотип "Самокат" вверху страницы
    LOGO_SCOOTER = By.XPATH, '//a[@href="/"]'
    # Кнопка Заказать вверху страницы
    HEADER_ORDER_BUTTON = By.XPATH, "//div[contains(@class, 'Header_Nav')]/button[text()='Заказать']"
    # Кнопка Статус заказа вверху страницы
    HEADER_STATE_ORDER_BUTTON = By.XPATH, "//button[text()='Статус заказа']"
    # Яндекц.Дзен
    YA_DZEN = By.XPATH, "//main[contains(@class, 'esktop-layout')]"
