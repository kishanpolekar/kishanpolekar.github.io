cost=float(input('Enter the cost of the item: '))
amount=float(input('Enter the amount given: '))
if (amount-cost<0):
    print ('Please pay more than the item\'s cost!!')
else:
    change=(amount-cost)*100
    dollar_bills=int(change/100)
    quarters=int((change-(dollar_bills*100))/25)
    dimes=int((change-(dollar_bills*100)-(quarters*25))/10)
    nickels=int((change-(dollar_bills*100)-(quarters*25)-(dimes*10))/5)
    pennies=int((change-(dollar_bills*100)-(quarters*25)-(dimes*10)-(nickels*5)))
    print ('Your change is ${:.2f}.\nDollar bills: {}\tQuarters: {}\tDimes: {}\tNickels: {}\tPennies: {}\n'.format(change/100, dollar_bills, quarters, dimes, nickels, pennies))
