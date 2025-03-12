import requests

def convert_currency(amount, from_currency, to_currency):
    url = f"https://api.frankfurter.app/latest?from={from_currency}&to={to_currency}"
    response = requests.get(url)

    if response.status_code != 200:
        print("Error fetching data from the API.")
        return None

    data = response.json()
    rates = data.get('rates')

    if rates and to_currency in rates:
        conversion_rate = rates[to_currency]
        converted_amount = amount * conversion_rate
        
        # Displaying the math behind the conversion
        print(f"\nExchange Rate: 1 {from_currency} = {conversion_rate:.4f} {to_currency}")
        print(f"Calculation: {amount} × {conversion_rate:.4f} = {converted_amount:.2f} {to_currency}\n")
        
        return converted_amount
    else:
        print(f"Conversion rate for {to_currency} not found.")
        return None

if __name__ == "__main__":
    amount = float(input("Enter amount: "))
    from_currency = input("Enter the currency you are converting from (e.g., USD, EUR): ").upper()
    to_currency = input("Enter the currency you are converting to (e.g., USD, EUR): ").upper()

    result = convert_currency(amount, from_currency, to_currency)

    if result:
        print(f"Final Result: {amount} {from_currency} is equal to {result:.2f} {to_currency}")
