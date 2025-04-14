import sys

def main():
    """Main function"""
    states = {
        "Oregon" : "OR",
        "Alabama" : "AL",
        "New Jersey": "NJ",
        "Colorado" : "CO"
    }
    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
    }

    if len(sys.argv) != 2:
        return

    if sys.argv[1] not in capital_cities.values():
        print(f"\033[91mUnknow capital city\033[0m")
        return
    else:
        capital_city = sys.argv[1]
        capital_code = [key for key, value in capital_cities.items() if value == capital_city]
        state = [code for code, abbr in states.items() if abbr == capital_code[0]]
        print(state[0])


if __name__ == "__main__":
    main()