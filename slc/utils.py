import json


def display_last_transactions():
    """
    функция чтение json-файла
    """
    with open('operations.json', 'r', encoding="utf-8") as file:
        data = json.load(file)
        return data


def get_trans(data, element):
    '''
    возвращает всю доступную информацию о переводе
    '''
    transactions = data[element:]

    for transaction in transactions:
        date = transaction.setdefault('date', 'Дата неизвестна')
        state = transaction.setdefault('state', 'Статус неизвестен')
        description = transaction.setdefault('description', 'Назначение неизвестно')
        from_account = transaction.setdefault('from', 'Отправитель неизвестен')
        to_account = transaction.setdefault('to', 'Получатель неизвестен')

        currency = transaction['operationAmount']['currency'].setdefault('name', 'Валюта неизвестна')
        amount = transaction['operationAmount'].setdefault('amount', 'Сумма неизвестна')

        return (date, description, from_account, to_account, amount, currency, state)


def get_hide_card(from_account, to_account):
    """
    Маскирует номер счета/карты
    """
    if from_account != 'Отправитель неизвестен':
        from_account = from_account.split(' ')

        if 'Счет' in from_account:
            # Маскироване номера счета
            masked_account_from = f'{from_account[0]} **{from_account[1][-4:]}'
        else:
            # Маскирование номера карты
            masked_account_from = f'{from_account[0]} {from_account[1][:4]} {from_account[1][4:6]}** **** {from_account[1][-4:]}'
    else:
        masked_account_from = 'Отправитель неизвестен'

    if to_account != 'Получатель неизвестен':
        to_account = to_account.split(' ')

        if 'Счет' in to_account:
            # Маскироване номера счета
            masked_account_to = f'{to_account[0]} **{to_account[1][-4:]}'
        else:
            # Маскирование номера карты
            masked_account_to = f'{to_account[0]} {to_account[1][:4]} {to_account[1][4:6]}** **** {to_account[1][-4:]}'
    else:
        masked_account_to = 'Получатель неизвестен'

    return masked_account_from, masked_account_to

def get_state(state):
    if state == "CANCELED":
        return 'Операция не прошла'
    elif state == "EXECUTED":
        return 'Операция прошла'
    else:
        return 'Статус неизвестен'