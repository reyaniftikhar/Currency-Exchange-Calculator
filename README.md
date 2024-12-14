Overview
This application allows users to convert an amount from one currency to another using real-time exchange rates.
It supports a wide variety of currencies and provides a user-friendly interface with the following features:

Input the amount you wish to convert.
Select the base currency and the target currency.
See the converted amount displayed immediately.
The application uses the ExchangeRate-API to fetch real-time conversion rates.

Requirements
Before running the application, make sure you have the following installed:

Python 3.x
requests library (for fetching real-time data from the API)
Tkinter (which is generally included with Python installations, but ensure it's available)

Installation Instructions
Download the Code: Download the currency_converter.py file or clone this repository to your local machine.

Get Your API Key:

Visit ExchangeRate-API, sign up, and get your free API key.
Replace the api_key variable in the code with your actual API key.
Run the Application:

Open a terminal or command prompt in the directory where the code is located.
Run the following command:
bash
Copy code
How to Use
Input Amount: Enter the amount you want to convert in the "Input Amount" field.
Select the Base Currency: Use the dropdown to select the currency from which you want to convert (e.g., USD, EUR).
Select the Destination Currency: Use the second dropdown to select the currency you want to convert to (e.g., IDR, EUR).
Click "Convert": The application will display the converted amount below the button.
Clear Fields: If you wish to clear the input and results, click the "Clear" button.
Code Explanation
1. CurrencyConverter Class
Purpose: This class handles the API requests and performs the currency conversion.
Methods:
__init__(self, url): Initializes the converter with the API URL and fetches exchange rates.
fetch_rates(self): Fetches the exchange rates from the provided API URL. It handles errors if the API request fails or returns invalid data.
convert(self, amount, base_currency, des_currency): Converts the given amount from one currency to another by first converting to USD (if necessary), then to the desired currency.
2. Main Class (Tkinter GUI)
Purpose: This class creates the graphical user interface using Tkinter.
Methods:
__init__(self, converter): Initializes the application, checks if exchange rates are available, and sets up the UI.
setup_ui(self): Builds the GUI components such as labels, entry fields, dropdowns, and buttons.
clear_fields(self): Clears the input and result fields.
process_conversion(self): Reads the user input, calls the conversion method, and displays the result.
3. Main Program Execution
The if __name__ == '__main__' block initializes the application by setting the API URL, creating a CurrencyConverter object, and starting the Tkinter main loop.
Error Handling
The program handles a variety of errors, including:

Invalid User Input: If the user enters a non-numeric value in the "Input Amount" field, a warning message will appear.
API Failures: If the program cannot fetch exchange rates from the API, it will display an error message and close the application.
Unexpected Errors: General errors during the conversion or UI setup are caught, and appropriate error messages are displayed.
Sample Screenshots
Main Application Window

Conversion Result


