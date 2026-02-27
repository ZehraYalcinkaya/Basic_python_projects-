def bill_split(amount, friends):
    taxed_bill= amount + amount *0.2

    final_bill= taxed_bill/friends

    print('taxed bill: ',taxed_bill)

    return final_bill


amount=float(input('enter the bill:'))
friend=int(input('enter the number of your friends:'))
print('Each friend will pay {} Turkish liras'.format(bill_split(amount, friend)))