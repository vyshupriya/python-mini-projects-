currency = [580,700,400,650,450,200]
symbols = ["USD", "GBP", "CAD", "EUR","CHF","YEN"]


print('''Welcome to your currency converter App

         For USD conversion to Naira type 0,
         For GBP conversion to Naira type 1,
         For CAD conversion to Naira type 2,
         For EUR conversion to Naira type 3,
         For CHF conversion to Naira type 4,
         For YEN conversion to Naira type 5,*''')


signs = int(input('Type the currency you want to convert to: '))
amount = float(input('Enter the amount you want to convert: '))

if signs ==0 or signs ==1 or signs ==2 or signs ==3 or signs ==4 or signs ==5:
    conversion = amount * currency[signs]
    currency_symbols = symbols[signs]
    print("The conversion of {}{} to naria is NGN {}".format(currency_symbols,amount, conversion))
else:
    print("You have entered a wrong value for the conversion")