def main():
    """Main function"""
    parts = []

    try:
        with open("numbers.txt", "r") as file:
            numbers = file.readlines()

        for line in numbers:
            parts = line.strip().split(",")

        for number in parts:
            print(number)

    except Exception as e:
        print(f"\033[91mError: {e}\033[0m")
        return


if __name__ == "__main__":
    main()