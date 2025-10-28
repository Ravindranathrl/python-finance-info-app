
import yfinance as yf
from datetime import datetime

# Predefined list of top companies
TOP_COMPANIES = {
    "AAPL": "Apple Inc.",
    "MSFT": "Microsoft Corporation",
    "GOOGL": "Alphabet Inc. (Google)",
    "AMZN": "Amazon.com, Inc.",
    "META": "Meta Platforms, Inc.",
    "TSLA": "Tesla, Inc.",
    "NVDA": "NVIDIA Corporation"
}


def fetch_stock(symbol):
    """Fetch and display stock info for a given symbol."""
    try:
        stock = yf.Ticker(symbol)
        info = stock.info

        company_name = info.get("longName", "N/A")
        current_price = info.get("regularMarketPrice")
        previous_close = info.get("regularMarketPreviousClose")

        if current_price is None or previous_close is None:
            print(f"⚠️  Unable to retrieve data for {symbol}. Please check the symbol or your network.\n")
            return

        value_change = current_price - previous_close
        percentage_change = (value_change / previous_close) * 100
        sign = "+" if value_change >= 0 else "-"

        current_time = datetime.now().strftime("%a %b %d %H:%M:%S %Z %Y")

        print("-----------------------------------------------------")
        print(f"{current_time}")
        print(f"{company_name} ({symbol.upper()})")
        print(f"💰 Price: ${current_price:.2f}")
        print(f"📈 Change: {sign}${abs(value_change):.2f} ({sign}{abs(percentage_change):.2f}%)")
        print("-----------------------------------------------------\n")

    except Exception as e:
        print(f"❌ Error fetching data for {symbol}: {e}\n")


def show_top_companies():
    """Display stock info for all predefined top companies."""
    print("\n🌍 Showing stock information for top companies:\n")
    for symbol in TOP_COMPANIES.keys():
        fetch_stock(symbol)


def option_enter_symbol():
    """Allows the user to enter multiple symbols and return to menu when needed."""
    print("\n📥 Enter stock symbols one by one.")
    print("Type 'menu' to return to the main menu or 'exit' to quit.\n")

    while True:
        symbol = input("Please enter a stock symbol (e.g., AAPL): ").strip().upper()

        if symbol.lower() == "menu":
            print("\n🔙 Returning to main menu...\n")
            return  # Goes back to main()
        elif symbol.lower() == "exit":
            print("\n👋 Exiting the program. Goodbye!\n")
            exit()
        elif symbol == "":
            print("⚠️  Please enter a valid stock symbol.\n")
        else:
            fetch_stock(symbol)


def main():
    """Main menu to choose between user input or top companies."""
    while True:
        print("=== 📊 Welcome to the Python Finance Info App ===")
        print("1️⃣  Enter a stock symbol")
        print("2️⃣  Show stock info for top companies")
        print("3️⃣  Exit the program")
        print("-----------------------------------------------------")

        choice = input("Please choose an option (1, 2, or 3): ").strip()

        if choice == "1":
            option_enter_symbol()
        elif choice == "2":
            show_top_companies()
        elif choice == "3":
            print("\n👋 Exiting the program. Goodbye!\n")
            break
        else:
            print("⚠️  Invalid choice. Please enter 1, 2, or 3.\n")


if __name__ == "__main__":
    main()
