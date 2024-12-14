# Import required modules
from tkinter import *  # This imports all tkinter classes
from tkinter import ttk  # For ttk widgets like Combobox
from tkinter import messagebox  # For message boxes
import requests
import datetime as dt

# Currency Converter Class
class CurrencyConverter:
    def __init__(self, url):
        self.url = url
        print("[DEBUG] Initializing CurrencyConverter with URL:", url)  # Debugging statement
        self.rates = self.fetch_rates()

    def fetch_rates(self):
        """Fetch rates from the API and handle errors."""
        print("[DEBUG] Fetching currency rates...")  # Debugging statement
        try:
            response = requests.get(self.url)
            response.raise_for_status()  # Raise an error for bad HTTP responses
            data = response.json()
            print("[DEBUG] API Response:", data)  # Debugging statement
            rates = data.get('conversion_rates')  # Corrected key from 'rates' to 'conversion_rates'

            if not rates:
                raise ValueError("Rates data is missing from the API response.")

            print("[DEBUG] Successfully fetched rates.")  # Debugging statement
            return rates
        except (requests.exceptions.RequestException, ValueError) as e:
            print("[ERROR] Failed to fetch rates:", e)  # Debugging statement
            messagebox.showerror("Error", f"Failed to fetch currency rates: {e}")
            return {}  # Return an empty dictionary if API call fails

    def convert(self, amount, base_currency, des_currency):
        """Convert an amount from one currency to another."""
        try:
            print(f"[DEBUG] Converting {amount} from {base_currency} to {des_currency}.")  # Debugging statement
            if base_currency != 'USD':  # Convert to USD first if the base is not USD
                amount /= self.rates.get(base_currency, 1)  # Avoid division by None

            # Convert from USD to the desired currency
            amount = round(amount * self.rates.get(des_currency, 1), 2)
            print(f"[DEBUG] Converted Amount: {amount}")  # Debugging statement
            return '{:,}'.format(amount)  # Format the result with commas
        except Exception as e:
            print("[ERROR] Conversion failed:", e)  # Debugging statement
            messagebox.showerror("Error", f"Failed to convert currency: {e}")
            return "Conversion Error"

# Main Window Class
class Main(Tk):
    def __init__(self, converter):
        super().__init__()
        print("[DEBUG] Initializing Main application...")  # Debugging statement
        self.title('Currency Converter')
        self.geometry('400x400')
        self.config(bg='#3A3B3C')
        self.CurrencyConverter = converter

        # Check if rates are available
        if not self.CurrencyConverter.rates:
            print("[ERROR] Currency rates not available. Exiting application.")  # Debugging statement
            messagebox.showerror("Error", "Currency rates could not be loaded. Please check your internet connection.")
            self.destroy()  # Close the application if no rates are available
            return

        self.setup_ui()

    def setup_ui(self):
        """Set up the user interface."""
        print("[DEBUG] Setting up UI...")  # Debugging statement
        try:
            # Title Label
            Label(self, text='Currency Converter', bg='#3A3B3C', fg='white', 
                  font=('franklin gothic medium', 20), relief='sunken').place(x=200, y=35, anchor='center')

            # Date Label
            Label(self, text=f'{dt.datetime.now():%A, %B %d, %Y}', bg='#3A3B3C', 
                  fg='white', font=('calibri', 10)).place(x=0, y=400, anchor='sw')

            # Version Label
            Label(self, text='v1.0', bg='#3A3B3C', fg='white', font=('calibri', 10)).place(x=400, y=400, anchor='se')

            # Amount Entry
            Label(self, text='Input Amount: ', bg='#3A3B3C', fg='white', 
                  font=('franklin gothic book', 15)).place(x=200, y=80, anchor='center')
            self.amount_entry = Entry(self, width=25)
            self.amount_entry.place(x=200, y=110, anchor='center')

            # Base Currency Dropdown
            Label(self, text='From: ', bg='#3A3B3C', fg='white', font=('franklin gothic book', 15)).place(x=200, y=140, anchor='center')
            self.currency_variable1 = StringVar(self, 'USD')
            self.currency_combobox1 = ttk.Combobox(self, width=20, textvariable=self.currency_variable1, 
                                                   values=list(self.CurrencyConverter.rates.keys()), state='readonly')
            self.currency_combobox1.place(x=200, y=170, anchor='center')

            # Destination Currency Dropdown
            Label(self, text='To: ', bg='#3A3B3C', fg='white', font=('franklin gothic book', 15)).place(x=200, y=200, anchor='center')
            self.currency_variable2 = StringVar(self, 'IDR')
            self.currency_combobox2 = ttk.Combobox(self, width=20, textvariable=self.currency_variable2, 
                                                   values=list(self.CurrencyConverter.rates.keys()), state='readonly')
            self.currency_combobox2.place(x=200, y=230, anchor='center')

            # Convert Button
            Button(self, text='Convert', bg='#52595D', fg='white', command=self.process_conversion).place(x=170, y=270, anchor='center')

            # Clear Button
            Button(self, text='Clear', bg='red', fg='white', command=self.clear_fields).place(x=230, y=270, anchor='center')

            # Result Field
            self.final_result = Label(self, text='', bg='#52595D', fg='white', font=('calibri', 12), 
                                      relief='sunken', width=40)
            self.final_result.place(x=200, y=310, anchor='center')

        except Exception as e:
            print("[ERROR] UI setup failed:", e)  # Debugging statement
            messagebox.showerror("Error", f"Failed to set up UI: {e}")

    def clear_fields(self):
        """Clear input and result fields."""
        print("[DEBUG] Clearing fields...")  # Debugging statement
        self.amount_entry.delete(0, END)
        self.final_result.config(text='')

    def process_conversion(self):
        """Perform currency conversion and display the result."""
        print("[DEBUG] Starting conversion process...")  # Debugging statement
        try:
            # Get user input
            given_amount = float(self.amount_entry.get())
            base_currency = self.currency_variable1.get()
            destination_currency = self.currency_variable2.get()
            print(f"[DEBUG] Amount: {given_amount}, From: {base_currency}, To: {destination_currency}")  # Debugging

            # Perform conversion
            converted_amount = self.CurrencyConverter.convert(given_amount, base_currency, destination_currency)
            given_amount = '{:,}'.format(given_amount)  # Format the input amount with commas

            # Display the result
            self.final_result.config(text=f'{given_amount} {base_currency} = {converted_amount} {destination_currency}')
            print("[DEBUG] Conversion successful.")  # Debugging statement

        except ValueError as ve:
            print("[ERROR] Invalid input:", ve)  # Debugging statement
            messagebox.showwarning('WARNING!', 'Please enter a valid number in the Amount field!')
        except Exception as e:
            print("[ERROR] Conversion process failed:", e)  # Debugging statement
            messagebox.showerror("Error", f"An unexpected error occurred: {e}")

# Main Program
if __name__ == '__main__':
    api_key = "6055b552315f6107d7cc5caa"  # Replace with your actual API key
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/USD"
    converter = CurrencyConverter(url)
    app = Main(converter)
    app.mainloop()
