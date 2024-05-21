# GFC stands for Gravity, Force, Current
# This program calculates gravity, force, and current based on user input.
def menu():
    """
    Print the main menu and prompt for a choice.
    """
    print("Welcome to calculator.py")
    print("Your options are:")
    print()
    print("1) Gravity")
    print("2) Force")
    print("3) Current")
    print("4) Quit calculator.py")
    print()
    return input("Choose your option: ")

def gravity(G, m1, m2, r):
    """
    Calculate gravity using the given parameters.
    """
    print(G, "*", m1, "*", m2, "/", r**2, "=", G * m1 * m2 / r**2)

def force(m, g):
    """
    Calculate force using the given mass and acceleration due to gravity.
    """
    print(m, "*", g, "=", m * g)

def current(q, t):
    """
    Calculate current using the given charge and time.
    """
    print(q, "/", t, "=", q / t)

# Main program
loop = True
while loop:
    choice = menu()
    if choice == "1":
        gravity(float(input("G: ")), float(input("m1: ")), float(input("m2: ")), float(input("r: ")))
    elif choice == "2":
        force(float(input("m: ")), float(input("g: ")))
    elif choice == "3":
        current(float(input("q: ")), float(input("t: ")))
    elif choice == "4":
        loop = False

print("Thank you for using study.py!")
