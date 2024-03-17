from slc import utils


def test_get_hide_card():
    """
    Проверяет корректность вывода карты/счета
    """
    assert utils.get_hide_card("Maestro 1308795367077170") == 'Maestro 1308 79** **** 7170'
    assert utils.get_hide_card("Счет 35737585785074382265") == 'Счет **2265'
    assert utils.get_hide_card("Счет 71687416928274675290") == 'Счет **5290'
    assert utils.get_hide_card("МИР 5211277418228469") == 'МИР 5211 27** **** 8469'
    assert utils.get_hide_card("Получатель неизвестен") == "Получатель неизвестен"
    assert utils.get_hide_card("Отправитель неизвестен") == 'Отправитель неизвестен'
    assert utils.get_hide_card("Maestro 1308795367077170") == 'Maestro 1308 79** **** 7170'


def test_get_state():
    """
    Проверка успешности операции
    """
    assert utils.get_state("EXECUTED") == 'Успешно'
    assert utils.get_state('CANCELED') == 'Операция не прошла'
    assert utils.get_state('Статус неизвестен') == 'Статус неизвестен'


def test_required_date_format():
    """
    Проверяет корректность вывода даты
    """
    assert utils.required_date_format("2019-11-13T17:38:04.800051") == '13.11.2019'
    assert utils.required_date_format("2019-12-07T06:17:14.634890") == '07.12.2019'
    assert utils.required_date_format("2018-12-23T11:47:52.403285") == '23.12.2018'
    assert utils.required_date_format("2019-02-12T00:08:07.524972") == '12.02.2019'
