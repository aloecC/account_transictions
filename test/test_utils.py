from slc import utils

def test_get_hide_card():
    assert utils.get_hide_card("Maestro 1308795367077170","Счет 96527012349577388612") == ('Maestro 1308 79** **** 7170','Счет **8612')
    assert utils.get_hide_card("Отправитель неизвестен", "Счет 35737585785074382265") == (
    'Отправитель неизвестен', 'Счет **2265')
    assert utils.get_hide_card("Счет 71687416928274675290", "Счет 87448526688763159781") == (
        'Счет **5290', 'Счет **9781')
    assert utils.get_hide_card("Maestro 1308795367077170", "МИР 5211277418228469") == (
        'Maestro 1308 79** **** 7170', 'МИР 5211 27** **** 8469')
    assert utils.get_hide_card("Отправитель неизвестен", "Получатель неизвестен") == (
        'Отправитель неизвестен', 'Получатель неизвестен')
    assert utils.get_hide_card("Maestro 1308795367077170", "Получатель неизвестен") == (
        'Maestro 1308 79** **** 7170', 'Получатель неизвестен')

def test_get_state():
    assert utils.get_state("EXECUTED") == 'Операция прошла'
    assert utils.get_state('CANCELED') == 'Операция не прошла'
    assert utils.get_state('Статус неизвестен') == 'Статус неизвестен'

