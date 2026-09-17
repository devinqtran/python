from bot import get_live_prices

def main():
    coin_list = ["bitcoin", "ethereum", "solana", "sui"]

    try:
        print("---Fetching Live Price Data---\n")
        prices = get_live_prices(coin_list)

        for coin, data in prices.items():
            price = data['usd']
            change = data['usd_24h_change']
            print(f"{coin.capitalize()}: ${price:,.2f} (24h change: {change:.2f}%)")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()