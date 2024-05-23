def display_menu():
    """
    Print the main menu and prompt for a choice.
    """
    print("Welcome to the Physics Calculator")
    print("Your options are:")
    print()
    print("1) Surface Energy")
    print("2) Moment of Inertia")
    print("3) Latent Heat")
    print("4) Entropy")
    print("5) Quit Program")
    print()
    return int(input("Choose your option: "))

def calculate_division(a, b):
    """
    Divide two numbers given.
    """
    print(a, "/", b, "=", a / b)

def calculate_multiplication(a, b):
    """
    Multiply two numbers given.
    """
    print(a, "*", b ** 2, "=", a * (b ** 2))

# Main program
loop = True
while loop:
    choice = display_menu()
    if choice == 1:
        calculate_division(float(input("Enter work: ")), float(input("Enter area: ")))
    elif choice == 2:
        calculate_multiplication(float(input("Enter mass: ")), float(input("Enter distance: ")))
    elif choice == 3:
        calculate_division(float(input("Enter heat: ")), float(input("Enter mass: ")))
    elif choice == 4:
        calculate_division(float(input("Enter heat: ")), float(input("Enter temperature: ")))
    elif choice == 5:
        loop = False

print("Thank you for using the Physics Calculator!")
print("Made by Ro706")
