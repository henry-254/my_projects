usd_ksh = 112.5
eur_ksh = 132.45
usd_eur = 1.2
add = 0 
def currency_converter(convert_to,amount):
        if convert_to == 1:
            add = usd_ksh * amount
            print(add)
        elif convert_to == 2:
            add = eur_ksh * amount
            print(add)
        elif convert_to == 3:
            add = usd_eur * amount
            print(add)
        else:
            print("number entered is invalid")
    

convert_to_1 = int(input("please enter your choice for conversion\n 1. usd to ksh\n 2. eur_ksh\n 3. usd_eur\n reply with 1, 2 or 3: "))
amount_1 = int(input("enter amount to be converted: "))

currency_converter(convert_to_1, amount_1)   