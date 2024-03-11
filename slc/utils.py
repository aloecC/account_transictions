import json


def display_last_transactions(element=int):
    with open('operations.json', 'r', encoding="utf-8") as file:
        data = json.load(file)

        transactions = data[element:]

        for transaction in transactions:
            date = transaction.setdefault('date', 'Дата неизвестна')
            description = transaction.setdefault('description', 'Назначение неизвестно')
            from_account = transaction.setdefault('from', 'Отправитель неизвестен')
            to_account = transaction.setdefault('to', 'Получатель неизвестен')
            amount = transaction['operationAmount'].setdefault('amount', 'Сумма неизвестна')
            currency = transaction['operationAmount']['currency'].setdefault('name', 'Валюта неизвестна')


            return (date, description, from_account, to_account, amount, currency)

def get_hide_card(from_account, to_account):

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
