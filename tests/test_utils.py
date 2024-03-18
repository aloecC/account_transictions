from slc.utils import *


def test_get_hide_card():
    """
    Проверяет корректность вывода карты/счета
    """
    assert get_hide_card("Maestro 1308795367077170") == 'Maestro 1308 79** **** 7170'
    assert get_hide_card("Счет 35737585785074382265") == 'Счет **2265'
    assert get_hide_card("Счет 71687416928274675290") == 'Счет **5290'
    assert get_hide_card("МИР 5211277418228469") == 'МИР 5211 27** **** 8469'
    assert get_hide_card("Получатель неизвестен") == "Получатель неизвестен"
    assert get_hide_card("Отправитель неизвестен") == 'Отправитель неизвестен'
    assert get_hide_card("Maestro 1308795367077170") == 'Maestro 1308 79** **** 7170'


def test_get_state():
    """
    Проверка успешности операции
    """
    assert get_state("EXECUTED") == 'Успешно'
    assert get_state('CANCELED') == 'Операция не прошла'
    assert get_state('Статус неизвестен') == 'Статус неизвестен'


def test_required_date_format():
    """
    Проверяет корректность вывода даты
    """
    assert required_date_format("2019-11-13T17:38:04.800051") == '13.11.2019'
    assert required_date_format("2019-12-07T06:17:14.634890") == '07.12.2019'
    assert required_date_format("2018-12-23T11:47:52.403285") == '23.12.2018'
    assert required_date_format("2019-02-12T00:08:07.524972") == '12.02.2019'


def test_successful_operations():
    for items in successful_operations():
        assert items['state'] == "EXECUTED"


def test_display_last_transactions():
    assert type(display_last_transactions()) == list


