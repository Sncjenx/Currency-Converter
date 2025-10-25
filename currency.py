import tkinter as tk
from tkinter import ttk
from currency_converter import CurrencyConverter

converter = CurrencyConverter()

### Conversion Functions ###

def convert_and_round(amount, exchange_rate):
    """
    Converts an amount from one currency to another and rounds the result.

    Args:
        amount (float): The amount to convert.
        exchange_rate (float): The exchange rate.

    Returns:
        float: The converted and rounded amount.
    """
    converted_amount = amount * exchange_rate
    return round(converted_amount, 2)


def convert_currency():
    try:
        amount = float(entry_amount.get())
        from_currency = combo_from_currency.get()
        to_currency = combo_to_currency.get()

        ### Convert using CurrencyConverter ###
        result = converter.convert(amount, from_currency, to_currency)

        ### Round result to 2 decimal places ###
        rounded_result = round(result, 2)

        label_result.config(
            text=f"{amount} {from_currency} = {rounded_result} {to_currency}"
        )
    except ValueError:
        label_result.config(text="Please enter a valid number.")
    except Exception as e:
        label_result.config(text=f"Error: {e}")


### GUI Setup ###

root = tk.Tk()
root.geometry("800x420")
root.title("Currency Converter")

### Labels ###

label_heading = tk.Label(root, text="SKA", font="Times 25 bold")
label_from_currency = tk.Label(root, text="First Currency:", font="Times 18 bold")
label_to_currency = tk.Label(root, text="Second Currency:", font="Times 18 bold")
label_amount = tk.Label(root, text="Amount:", font="Times 18 bold")
label_result = tk.Label(root, text="Result:", font="Times 18 bold")

### Input Fields ###

entry_amount = tk.Entry(root)
available_currencies = converter.currencies
currency_list = sorted(list(available_currencies))  # sorted for better UI
combo_from_currency = ttk.Combobox(root, values=currency_list)
combo_to_currency = ttk.Combobox(root, values=currency_list)
convert_button = tk.Button(root, text="Convert", command=convert_currency)

### Layout ###

label_heading.pack(pady=10)
label_from_currency.pack()
combo_from_currency.pack()
label_to_currency.pack()
combo_to_currency.pack()
label_amount.pack()
entry_amount.pack()
convert_button.pack(pady=10)
label_result.pack(pady=10)

root.mainloop()
