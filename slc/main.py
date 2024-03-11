from utils import display_last_transactions, get_hide_card, get_trans

for i in range(-5, 0):
    element = i
    data = display_last_transactions()
    date, description, from_account, to_account, amount, currency = get_trans(data,element)

    from_account, to_account = get_hide_card(from_account, to_account)

    print(f'''{date} {description}
    {from_account} -> {to_account}
    {amount} {currency}''')


