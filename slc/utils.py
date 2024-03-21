import json
from operator import itemgetter
from datetime import datetime


def display_last_transactions(file_json):
    """
    функция чтение json-файла
    """
    with open(file_json, 'r', encoding="utf-8") as file:
        file = json.load(file)
        return file


def successful_operations(file_json):
    """
    Функция возвращает список успешных операций
    """
    file = display_last_transactions(file_json)
    executed_operations = []
    for item in file:
        if not item:
            continue
        if item['state'] == "EXECUTED":
            executed_operations.append(item)
    return executed_operations


def sorting_date_list(success_list):
    """
    Функция возвращает отсортированный по дате список
    """
    date_operations = successful_operations(success_list)
    number_of_operations = 6
    return sorted(date_operations, key=itemgetter('date'), reverse=True)[0:number_of_operations]


def required_date_format(date_time):
    """
    Функция возвращает требуемый формат даты
    """
    date_obj = datetime.strptime(date_time, '%Y-%m-%dT%H:%M:%S.%f')
    return datetime.strftime(date_obj.date(), '%d.%m.%Y')


def get_trans(data, element):
    """
    возвращает всю доступную информацию о переводе
    """
    transactions = data[element:]

    for transaction in transactions:
        date = transaction.setdefault('date', 'Дата неизвестна')
        state = transaction.setdefault('state', 'Статус неизвестен')
        description = transaction.setdefault('description', 'Назначение неизвестно')
        from_account = transaction.setdefault('from', 'Отправитель неизвестен')
        to_account = transaction.setdefault('to', 'Получатель неизвестен')

        currency = transaction['operationAmount']['currency'].setdefault('name', 'Валюта неизвестна')
        amount = transaction['operationAmount'].setdefault('amount', 'Сумма неизвестна')

        return date, description, from_account, to_account, amount, currency, state


def get_hide_card(card_number):
    """
    Функция возвращает требуемый формат номера карты/cчета
    """
    if card_number:
        numbers = ""
        for item in card_number:
            if item.isdigit():
                numbers += item
        string_out = card_number[:card_number.find(numbers) - 1]
        numbers_out = card_number[card_number.find(numbers):]
        if len(numbers_out) == 16:
            numbers_out = numbers_out[:4] + ' ' + numbers_out[4:6] + "**" + " " + "****" + " " + numbers_out[-4:]
        elif len(numbers_out) == 20:
            numbers_out = "**" + numbers_out[-4:]
        if 'неизвестен' in numbers_out:
            return f'{numbers_out}'
        return f"{string_out} {numbers_out}"
    else:
        return "VVVVVVVV"


def get_state(state):
    """
    функция проверяет точно ли операция прошла успешно
    """
    if state == "CANCELED":
        return 'Операция не прошла'
    elif state == "EXECUTED":
        return 'Успешно'
    else:
        return 'Статус неизвестен'


def get_operation(data, element):
    """
    функция приводит все данные к требуемому формату
    """
    date, description, from_account, to_account, amount, currency, state = get_trans(data, element)
    date = required_date_format(date)
    from_account = get_hide_card(from_account)
    to_account = get_hide_card(to_account)
    state = get_state(state)
    return date, description, from_account, to_account, amount, currency, state
