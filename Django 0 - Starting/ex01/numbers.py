def main():
    """Main function"""
    try:
        with open("numbers.txt", "r") as file:
            numbers = file.readlines()

        for line in numbers:
            parts = line.strip().split(",")

        for number in parts:
            print(number)
    except:
        print("\033[91mError: An error occurred while reading the file.\033[0m")
        return


if __name__ == "__main__":
    main()