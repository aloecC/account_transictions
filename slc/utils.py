import json


def display_last_transactions():
    with open('operations.json', 'r', encoding="utf-8") as file:
        data = json.load(file)

        transactions = data['transactions']

        for transaction in transactions:
            date = transaction['date']
            description = transaction['description']
            from_account = transaction['from']
            to_account = transaction['to']
            amount = transaction['operationAmount']['amount']
            currency = transaction['operationAmount']['currency']['name']

            return (date, description, from_account, to_account, amount, currency)



# Пример использования функции
