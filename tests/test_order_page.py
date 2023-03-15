import allure
from locators.main_page_locators import MainPageLocators
from pages.base_page import HeaderPageScooter
from pages.main_page import MainPageScooter
from pages.order_page import OrderScooterPage


@allure.title('Заказ самоката через кнопку «Заказать» вверху страницы')
@allure.description('Вверху страницы ищем кнопку «Заказать», нажимаем на нее, заполняем поля формы заказа и формируем '
                    'заказ. Проверяем, что заказ сформирован ')
def test_order_scooter_via_header_button(driver):
    main_page = MainPageScooter(driver)
    main_page.wait_for_load_main_page()
    header = HeaderPageScooter(driver)
    header.click_order_button_header()

    order = OrderScooterPage(driver)
    order.wait_for_order_form()

    order.fill_first_part_order('Вера',
                                'Комарова',
                                'г. Москва, ул. Академика Королева, 12',
                                'Преображенская площадь',
                                '88002000600')
    order.go_forward()
    order.wait_order_form_about_rent()
    order.fill_second_part_order('28',
                                 'двое суток',
                                 'black',
                                 'Предварительно позвонить по указанному телефону')
    order.click_buttton('Заказать')
    order.click_buttton('Да')
    order.wait_modal_window()

    assert 'Заказ оформлен' in order.text_modal_window()


@allure.title('Заказ самоката через кнопку «Заказать» на главной странице внизу')
@allure.description('Скроллим вниз до кнопки «Заказать», нажимаем на нее, заполняем поля формы заказа и формируем '
                    'заказ. Проверяем, что заказ сформирован ')
def test_order_scooter_via_button_on_main_page(driver):
    main_page = MainPageScooter(driver)
    main_page.wait_for_load_main_page()
    main_page.scroll_to(*MainPageLocators.MAIN_PAGE_ORDER_BUTTON)
    main_page.wait_order_button_on_mail_page()
    main_page.click_order_button_on_mail_page()

    order = OrderScooterPage(driver)
    order.wait_for_order_form()
    order.fill_first_part_order('Владимир',
                                'Широков',
                                'ул. 300-летия Москвы, 74',
                                'Охотный Ряд',
                                '88009379992')
    order.go_forward()
    order.wait_order_form_about_rent()
    order.fill_second_part_order('30',
                                 'сутки',
                                 'grey',
                                 'Свяжитесь со мной перед доставкой')
    order.click_buttton('Заказать')
    order.click_buttton('Да')
    order.wait_modal_window()

    assert 'Заказ оформлен' in order.text_modal_window()
