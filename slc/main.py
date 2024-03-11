from utils import display_last_transactions, get_hide_card, get_trans, get_state
k = -1
count = 0
while count != 5:
    element = k
    data = display_last_transactions()
    date, description, from_account, to_account, amount, currency, state = get_trans(data,element)

    from_account, to_account = get_hide_card(from_account, to_account)

    state = get_state(state)
    if state == 'Операция не прошла':
        k -= 1
        continue
    else:
        k -= 1
        count += 1
        print(f'''{date} {description}
        {from_account} -> {to_account}
        {amount} {currency} : {state}''')