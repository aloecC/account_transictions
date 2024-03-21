from slc.utils import get_operation, sorting_date_list
import os
import sys

# определяет путь к файлу со скриптом (main.py)
print(sys.argv[0])
print(os.path.abspath(sys.argv[0]))
print(os.path.dirname(os.path.abspath(sys.argv[0])))
SCRIPT_DIR = os.path.dirname(os.path.abspath(sys.argv[0]))
FILE_JSON = os.path.join(SCRIPT_DIR, 'operations.json')

data = sorting_date_list(FILE_JSON)

for element in range(5):
    date, description, from_account, to_account, amount, currency, state = get_operation(data, element)

    print(f'''{date} {description}
    {from_account} -> {to_account}
    {amount} {currency} : {state}''')
    print('-------')
