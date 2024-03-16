from utils import get_operation, sorting_date_list,get_trans,sorting_date_list

data = sorting_date_list()

for element in range(5):

    date, description, from_account, to_account, amount, currency, state = get_operation(data, element)

    print(f'''{date} {description}
    {from_account} -> {to_account}
    {amount} {currency} : {state}''')
