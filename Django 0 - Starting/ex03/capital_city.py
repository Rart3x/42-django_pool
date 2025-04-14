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

    if sys.argv[1] not in states:
        print(f"\033[91mUnknow State\033[0m")
        return
    else:
        state = sys.argv[1]
        state_abbr = states[state]
        capital_city = capital_cities[state_abbr]

    print(capital_city)


if __name__ == "__main__":
    main()