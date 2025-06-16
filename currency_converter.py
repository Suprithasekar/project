import tkinter as tk
from tkinter import messagebox
root=tk.Tk()
root.title("Currency Converter")
root.geometry("400x300")
amount_label=tk.Label(root,text="Enter amount:")
amount_label.pack(pady=5)
amount_entry=tk.Entry(root)
amount_entry.pack(pady=5)
from_label=tk.Label(root,text="From Currency:")
from_label.pack(pady=5)
from_currency=tk.StringVar()
from_currency.set("USD")
from_dropdown=tk.OptionMenu(root,from_currency,"USD","INR","EUR","JPY","GBP")
from_dropdown.pack(pady=5)
to_label=tk.Label(root,text="To Currency:")
to_label.pack(pady=5)
to_currency=tk.StringVar()
to_currency.set("INR")
to_dropdown=tk.OptionMenu(root,to_currency,"USD","INR","EUR","JPY","GBP")
to_dropdown.pack(pady=5)
exchange_rates={"USD":{"INR":83.0,"EUR":0.93,"JPY":157.0,"GBP":0.79},"INR":{"USD":0.012,"EUR":0.011,"JPY":1.89,"GBP":0.0095},"EUR":{"USD":1.08,"INR":89.0,"JPY":168.5,"GBP":0.85},"JPY":{"USD":0.0064,"INR":0.53,"EUR":0.0059,"GBP":0.005},"GBP":{"USD":1.27,"INR":104.5,"EUR":1.17,"JPY":200.0}}
def convert_currency():
    try:
        amount=float(amount_entry.get())
        from_curr=from_currency.get()
        to_curr=to_currency.get()
        if from_curr==to_curr:
            result=amount
        else:
            rate=exchange_rates.get(from_curr,{}).get(to_curr)
            if rate:
                result=amount*rate
            else:
                messagebox.showerror("Error","Conversion rate not available")
                return
            messagebox.showinfo("Converted Amount",f"{amount}{from_curr}={round(result,2)}{to_curr}")
    except ValueError:
        messagebox.showerror("Error","Please enter a valid number")
convert_button=tk.Button(root,text="Convert",command=convert_currency)
convert_button.pack(pady=10)
root.mainloop()
