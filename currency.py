import tkinter as tk
from tkinter import ttk
from currency_converter import CurrencyConverter

# -----------------------------
# App Configuration
# -----------------------------
APP_TITLE = "Currency Converter"
APP_SIZE = "520x360"

converter = CurrencyConverter()

# -----------------------------
# Conversion Logic
# -----------------------------
def convert_currency():
    try:
        amount = float(amount_entry.get())
        from_currency = from_currency_combo.get()
        to_currency = to_currency_combo.get()

        if not from_currency or not to_currency:
            raise ValueError("Please select both currencies.")

        result = converter.convert(amount, from_currency, to_currency)
        result_label.config(
            text=f"{amount:.2f} {from_currency} = {result:.2f} {to_currency}",
            foreground="green"
        )

    except ValueError as e:
        result_label.config(text=str(e), foreground="red")
    except Exception:
        result_label.config(text="Conversion failed. Try again.", foreground="red")


# -----------------------------
# GUI Setup
# -----------------------------
root = tk.Tk()
root.title(APP_TITLE)
root.geometry(APP_SIZE)
root.resizable(False, False)

style = ttk.Style()
style.theme_use("clam")

# -----------------------------
# Main Frame
# -----------------------------
main_frame = ttk.Frame(root, padding=20)
main_frame.pack(expand=True)

# -----------------------------
# Title
# -----------------------------
title_label = ttk.Label(
    main_frame,
    text="💱 Currency Converter",
    font=("Segoe UI", 22, "bold")
)
title_label.pack(pady=(0, 20))

# -----------------------------
# Currency Selection
# -----------------------------
currency_frame = ttk.Frame(main_frame)
currency_frame.pack(pady=10)

available_currencies = sorted(converter.currencies)

from_currency_combo = ttk.Combobox(
    currency_frame, values=available_currencies, state="readonly", width=15
)
to_currency_combo = ttk.Combobox(
    currency_frame, values=available_currencies, state="readonly", width=15
)

from_currency_combo.set("USD")
to_currency_combo.set("EUR")

ttk.Label(currency_frame, text="From").grid(row=0, column=0, padx=10, pady=5)
ttk.Label(currency_frame, text="To").grid(row=0, column=1, padx=10, pady=5)

from_currency_combo.grid(row=1, column=0, padx=10)
to_currency_combo.grid(row=1, column=1, padx=10)


# -----------------------------
# Amount Entry
# -----------------------------
ttk.Label(main_frame, text="Amount").pack(pady=(15, 5))

amount_entry = ttk.Entry(main_frame, width=25)
amount_entry.pack()
amount_entry.focus()

# -----------------------------
# Convert Button
# -----------------------------
convert_button = ttk.Button(
    main_frame,
    text="Convert",
    command=convert_currency
)
convert_button.pack(pady=20)

# -----------------------------
# Result
# -----------------------------
result_label = ttk.Label(
    main_frame,
    text="Enter an amount and select currencies",
    font=("Segoe UI", 12)
)
result_label.pack()

root.mainloop()

