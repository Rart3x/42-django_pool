def my_var():
    """My var function, print 9 variable types"""
    int = 42
    str = "42"
    str2 = "quarante-deux"
    float = 42.0
    bool = True
    list = [42]
    dict = {42: 42}
    tuple = (42,)
    set_var = set()

    for var in [int, str, str2, float, bool, list, dict, tuple, set_var]:
        print(f"{var} est de type {type(var)}")


def main():
    """Main function"""
    my_var()


if __name__ == "__main__":
    main()