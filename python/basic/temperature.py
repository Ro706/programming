def print_options():
    """
    Print the available options.
    """
    print("Options:")
    print(" 'p' print options")
    print(" 'c' convert from celsius")
    print(" 'f' convert from fahrenheit")
    print(" 'q' quit the program")

def celsius_to_fahrenheit(c_temp):
    """
    Convert Celsius temperature to Fahrenheit.
    """
    return 9.0 / 5.0 * c_temp + 32

def fahrenheit_to_celsius(f_temp):
    """
    Convert Fahrenheit temperature to Celsius.
    """
    return (f_temp - 32.0) * 5.0 / 9.0

choice = "p"
while choice != "q":
    if choice == "c":
        temp = float(input("Celsius temperature: "))
        print("Fahrenheit:", celsius_to_fahrenheit(temp))
    elif choice == "f":
        temp = float(input("Fahrenheit temperature: "))
        print("Celsius:", fahrenheit_to_celsius(temp))
    elif choice != "q":
        print_options()
    choice = input("option: ")
