from selenium.webdriver.common.by import By


class OrderPageLocators:
    # Форма заказа самоката
    ORDER_FORM = By.CLASS_NAME, 'Order_Content__bmtHS'
    # Поле Имя при оформлении заказа
    FIELD_NAME_IN_ORDER = By.XPATH, "//input[@placeholder = '* Имя']"
    # Поле Фамилия при оформлении заказа
    FIELD_SURNAME_IN_ORDER = By.XPATH, "//input[@placeholder = '* Фамилия']"
    # Поле Адрес при оформлении заказа
    FIELD_ADDRESS_IN_ORDER = By.XPATH, "//input[@placeholder = '* Адрес: куда привезти заказ']"
    # Поле станция метро при оформлении заказа
    FIELD_METRO_IN_ORDER = By.XPATH, "//input[@placeholder = '* Станция метро']"
    # Станции метро
    METRO_STATION = By.XPATH, "//div[contains(text(), '{}')]"
    # Поле Телефон при оформлении заказа
    FIELD_PHONE_IN_ORDER = By.XPATH, "//input[@placeholder = '* Телефон: на него позвонит курьер']"
    # Кнопка Далее
    NEXT_STEP_BUTTON = By.XPATH, "//div[contains(@class, 'Order_NextButton')]/button[text() = 'Далее']"
    # Поле Когда привезти самокат при оформлении заказа
    FIELD_DATE_RENT_IN_ORDER = By.XPATH, "//input[@placeholder = '* Когда привезти самокат']"
    # Выбор даты в календаре
    DATE_FROM_CALENDAR = By.XPATH, "//div[contains(@class, 'react-datepicker__day') and text()='{}']"
    # Поле Срок аренды
    FIELD_RENTAL_PERIOD_IN_ORDER = By.XPATH, "//div[@class = 'Dropdown-placeholder' and text() = '* Срок аренды']"
    # Варианты для срока аренды (выпадающий список)
    RENTAL_PERIOD_VARIANT = By.XPATH, "//div[@class = 'Dropdown-option' and text() = '{}']"
    # Заголовок Про аренду
    ABOUT_RENT = By.XPATH, "//div[text() = 'Про аренду']"
    # Поле Цвет самоката
    FIELD_COLOR_SCOOTER_IN_ORDER = By.XPATH, "//input[@id = '{}']"
    # Поле комментарий для курьера
    FIELD_COMMENT_IN_ORDER = By.XPATH, "//input[@placeholder = 'Комментарий для курьера']"
    # Кнопки Заказать / Назад / Да под формой заказа
    BUTTON_UNDER_ORDER = By.XPATH, "//div[contains(@class, 'Order_Buttons')]/button[text() = '{}']"
    # Модальное окно подтверздения заказа
    MODAL_WINDOW_ORDER = By.XPATH, "//div[contains(@class, 'Order_ModalHeader')]"
