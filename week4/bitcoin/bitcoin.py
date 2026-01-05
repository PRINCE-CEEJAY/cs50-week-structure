import requests
import sys

# my apiKey = 77bae5184672b5cc1bdf2afa6759ec33881998bfe7f0070e2688c2dc063c14e2

def fetch_btc():
    try:
        response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=77bae5184672b5cc1bdf2afa6759ec33881998bfe7f0070e2688c2dc063c14e2")
        response = response.json()
        return response["data"]["priceUsd"]

    except requests.RequestException:
        return

bitcoin_dollar = fetch_btc()

try:
    if not sys.argv[1]:
         sys.exit("Missing command-line argument")

    user = sys.argv[1]
    result = float(bitcoin_dollar) * float(user)
    print(f"${result:,.4f}")

except ValueError:
        sys.exit("Command-line argument is not a number")


