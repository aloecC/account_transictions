from utils import get_operation, sorting_date_list
import os


data = sorting_date_list()

for element in range(5):
    date, description, from_account, to_account, amount, currency, state = get_operation(data, element)

    print(f'''{date} {description}
    {from_account} -> {to_account}
    {amount} {currency} : {state}''')


print(os.getcwd())