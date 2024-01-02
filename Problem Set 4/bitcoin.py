import sys
import requests

def get_bitcoin_price():
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response.raise_for_status()
        bitcoin_data = response.json()
        return bitcoin_data["bpi"]["USD"]["rate_float"]

    except requests.RequestException as e:
        print(f"Error fetching Bitcoin price: {e}")
        sys.exit(1)

def main():
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    try:
        bitcoins_to_buy = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    bitcoin_price = get_bitcoin_price()
    total_cost = bitcoins_to_buy * bitcoin_price

    print(f"${total_cost:,.4f}")

if __name__ == "__main__":
    main()



# sample coindesk API
# {
#    "time":{
#       "updated":"May 2, 2022 15:27:00 UTC",
#       "updatedISO":"2022-05-02T15:27:00+00:00",
#       "updateduk":"May 2, 2022 at 16:27 BST"
#    },
#    "disclaimer":"This data was produced from the CoinDesk Bitcoin Price Index (USD). Non-USD currency data converted using hourly conversion rate from openexchangerates.org",
#    "chartName":"Bitcoin",
#    "bpi":{
#       "USD":{
#          "code":"USD",
#          "symbol":"&#36;",
#          "rate":"38,761.0833",
#          "description":"United States Dollar",
#          "rate_float":38761.0833
#       },
#       "GBP":{
#          "code":"GBP",
#          "symbol":"&pound;",
#          "rate":"30,827.6198",
#          "description":"British Pound Sterling",
#          "rate_float":30827.6198
#       },
#       "EUR":{
#          "code":"EUR",
#          "symbol":"&euro;",
#          "rate":"36,800.2764",
#          "description":"Euro",
#          "rate_float":36800.2764
#       }
#    }
# }
