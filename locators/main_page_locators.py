from selenium.webdriver.common.by import By


class MainPageLocators:
    # Главная страница
    MAIN_PAGE = By.XPATH, "//div[@class = 'Home_HomePage__ZXKIX']"
    # Всплывающее окно c кнопкой об использовании кук
    COOKIE_FORM = By.XPATH, "//button[text() = 'да все привыкли' and contains(@class, 'App_CookieButton')]"
    # Секция Вопросы о важном
    FAQ_SECTION = By.CLASS_NAME, 'Home_FAQ__3uVm4'
    # Вопросы в секции Вопросы о важном
    QUESTION = By.XPATH, "//div[@id = 'accordion__heading-{}']"
    # Ответы в секции Вопросы о важном
    ANSWER = By.XPATH, "//div[@id = \'accordion__panel-{}\' and not(@hidden = \'\')]/p"
    # Кнопка Заказать на главной странице
    MAIN_PAGE_ORDER_BUTTON = By.XPATH, "//div[contains(@class, 'Home_FinishButton')]/button[text() = 'Заказать']"
