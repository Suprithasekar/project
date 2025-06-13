exchange_rates={"USD": 1.0,"INR": 83.15,"EUR": 0.92,"GBP": 0.78,"JPY": 157.35}
amount=float(input("Enter amount: "))
from_currency=input("From currency (e.g. USD): ").upper()
to_currency=input("To currency (e.g. INR): ").upper()
if from_currency not in exchange_rates or to_currency not in exchange_rates:
    print("Currency not supported")
else:
    amount_in_usd=amount/exchange_rates[from_currency]
    converted_amount=amount_in_usd*exchange_rates[to_currency]
    print(f"{amount} {from_currency} = {round(converted_amount, 2)} {to_currency}")
