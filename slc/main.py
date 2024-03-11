from utils import display_last_transactions, get_hide_card, get_trans, get_state

for i in range(-5, 0):
    element = i
    data = display_last_transactions()
    date, description, from_account, to_account, amount, currency, state = get_trans(data,element)

    from_account, to_account = get_hide_card(from_account, to_account)

    state = get_state(state)
    print(f'''{date} {description}
    {from_account} -> {to_account}
    {amount} {currency} : {state}''')


