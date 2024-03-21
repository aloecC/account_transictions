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


def test_successful_operations():
    file_json = 'operations.json'
    for items in utils.successful_operations(file_json):
        assert items['state'] == "EXECUTED"


def test_display_last_transactions():
    file_json = 'operations.json'
    assert type(utils.display_last_transactions(file_json)) == list


def test_sorting_date_list():
    file_json = 'operations.json'
    assert utils.sorting_date_list(file_json) == [{
        'id': 863064926,
        'state': 'EXECUTED',
        'date': '2019-12-08T22:46:21.935582',
        'operationAmount': {
            'amount': '41096.24',
            'currency': {
                'name': 'USD',
                'code': 'USD'
            }},
        'description': 'Открытие вклада',
        'to': 'Счет 90424923579946435907'}, {
        'id': 114832369,
        'state': 'EXECUTED',
        'date': '2019-12-07T06:17:14.634890',
        'operationAmount': {
            'amount': '48150.39',
            'currency': {
                'name': 'USD',
                'code': 'USD'
            }},
        'description': 'Перевод организации',
        'from': 'Visa Classic 2842878893689012',
        'to': 'Счет 35158586384610753655'}, {
        'id': 154927927, 'state':
            'EXECUTED', 'date': '2019-11-19T09:22:25.899614',
        'operationAmount': {
            'amount': '30153.72',
            'currency': {
                'name': 'руб.',
                'code': 'RUB'
            }},
        'description': 'Перевод организации',
        'from': 'Maestro 7810846596785568',
        'to': 'Счет 43241152692663622869'}, {
        'id': 482520625,
        'state': 'EXECUTED',
        'date': '2019-11-13T17:38:04.800051',
        'operationAmount': {
            'amount': '62814.53',
            'currency': {
                'name': 'руб.',
                'code': 'RUB'}},
        'description': 'Перевод со счета на счет',
        'from': 'Счет 38611439522855669794',
        'to': 'Счет 46765464282437878125'}, {
        'id': 801684332,
        'state': 'EXECUTED',
        'date': '2019-11-05T12:04:13.781725',
        'operationAmount': {
            'amount': '21344.35',
            'currency': {
                'name': 'руб.',
                'code': 'RUB'
            }},
        'description': 'Открытие вклада',
        'to': 'Счет 77613226829885488381'}, {
        'id': 509645757,
        'state': 'EXECUTED',
        'date': '2019-10-30T01:49:52.939296',
        'operationAmount': {
            'amount': '23036.03',
            'currency': {
                'name': 'руб.',
                'code': 'RUB'
            }},
        'description': 'Перевод с карты на счет',
        'from': 'Visa Gold 7756673469642839',
        'to': 'Счет 48943806953649539453'
    }
    ]