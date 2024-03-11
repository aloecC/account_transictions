from utils import display_last_transactions, get_hide_card

for i in range(-5, 0):
    element = i

    date, description, from_account, to_account, amount, currency = display_last_transactions(element)

    from_account, to_account = get_hide_card(from_account, to_account)

    print(f'''{date} {description}
    {from_account} -> {to_account}
    {amount} {currency}''')


