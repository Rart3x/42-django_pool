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

    try:
        args = sys.argv[1].split(",")
        args = [arg.strip() for arg in args]

        if '' in args:
            return

        for arg in args:
            if arg.capitalize() in states:
                print(f"\033[92m{arg.capitalize()} is a state\033[0m")
            elif arg.capitalize() in capital_cities.values():
                for state, abbr in states.items():
                    if capital_cities[abbr] == arg.capitalize():
                        print(f"\033[92m{arg.capitalize()} is the capital of {state}\033[0m")
            else:
                print(f"\033[91m{arg.capitalize()} is neither a capital city nor a state\033[0m")

    except Exception as e:
        print(f"\033[91mError: {e}\033[0m")
        return

if __name__ == "__main__":
    main()