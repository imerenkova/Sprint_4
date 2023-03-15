import pytest
import allure

from locators.main_page_locators import MainPageLocators
from pages.base_page import HeaderPageScooter
from pages.main_page import MainPageScooter


@allure.title('Клик по логотипу "Яндекс" открывает в новом окне главную страницу Яндекс.Дзен')
@allure.description('Открываем сервис Яндекс.Самокат, переходим на форму создания заказа, далее кликаем по лого '
                    'Яндекс. Переходим на открывшуюся соседнюю вкладку и проверяем, что это url Яндекс.Дзен')
def test_move_to_ya_dzen(driver):
    main_page = MainPageScooter(driver)
    main_page.wait_for_load_main_page()

    header = HeaderPageScooter(driver)
    header.click_order_button_header()
    assert header.get_current_url() == 'https://qa-scooter.praktikum-services.ru/order'

    header.click_logo_yandex()
    window_after = driver.window_handles[1]
    driver.switch_to.window(window_after)
    header.wait_load_ya_dzen()

    current_url = driver.current_url
    assert current_url == 'https://dzen.ru/?yredirect=true'


@allure.title('Клик по логотипу "Самокат" возвращает на главную страницу «Яндекс.Самоката».')
@allure.description('Открываем сервис Яндекс.Самокат, переходим на форму создания заказа, проверяем, что при этом '
                    'поменялся url (добавилось /order), далее кликаем по лого "Самокат" и проверяем, что вернулись на '
                    'главную страницу «Яндекс.Самоката».')
def test_move_to_main_page_scooter(driver):
    main_page = MainPageScooter(driver)
    main_page.wait_for_load_main_page()

    header = HeaderPageScooter(driver)
    header.click_order_button_header()
    assert header.get_current_url() == 'https://qa-scooter.praktikum-services.ru/order'
    header.click_logo_scooter()

    current_url = header.get_current_url()
    assert current_url == 'https://qa-scooter.praktikum-services.ru/'


@allure.title('Проверка ответов в секции "Вопросы о важном"')
@allure.description('Поочередно кликаем по вопросам в секции "Вопросы о важном" и проверяем текст ответа')
@pytest.mark.parametrize('num_question,answer',
                         [
                             [1, 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'],
                             [2, 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, '
                                 'можете просто сделать несколько заказов — один за другим.'],
                             [3, 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. '
                                 'Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если '
                                 'мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'],
                             [4, 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'],
                             [5, 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по '
                                 'красивому номеру 1010.'],
                             [6, 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже '
                                 'если будете кататься без передышек и во сне. Зарядка не понадобится.'],
                             [7, 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не '
                                 'попросим. Все же свои.'],
                             [8, 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'],
                         ])
def test_check_answers_to_questions(driver, num_question, answer):
    main_page = MainPageScooter(driver)
    main_page.wait_for_load_main_page()
    main_page.scroll_to(*MainPageLocators.FAQ_SECTION)
    main_page.wait_FAQ_section()
    main_page.click_question(num_question)
    main_page.wait_text_answer(num_question)
    got_answer = main_page.text_answer(num_question)
    assert got_answer == answer


@allure.title('Проверка текста вопросов в секции "Вопросы о важном"')
@allure.description('Поочередно кликаем по вопросам в секции "Вопросы о важном" и проверяем текст вопроса')
@pytest.mark.parametrize('num_question,text_question',
                         [
                             [1, 'Сколько это стоит? И как оплатить?'],
                             [2, 'Хочу сразу несколько самокатов! Так можно?'],
                             [3, 'Как рассчитывается время аренды?'],
                             [4, 'Можно ли заказать самокат прямо на сегодня?'],
                             [5, 'Можно ли продлить заказ или вернуть самокат раньше?'],
                             [6, 'Вы привозите зарядку вместе с самокатом?'],
                             [7, 'Можно ли отменить заказ?'],
                             [8, 'Я жизу за МКАДом, привезёте?']])
def test_check_text_question(driver, num_question, text_question):
    main_page = MainPageScooter(driver)
    main_page.wait_for_load_main_page()
    main_page.scroll_to(*MainPageLocators.FAQ_SECTION)
    main_page.wait_FAQ_section()
    main_page.click_question(num_question)
    main_page.wait_text_answer(num_question)
    got_text_question = main_page.text_question(num_question)
    assert got_text_question == text_question
