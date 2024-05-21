def menu():
    print("Welcome to physics.py")
    print("Your options are:")
    print()
    print("1) Power")
    print("2) Electrical potential")
    print("3) Pressure")
    print("4) Surface tension")
    print("5) Quit physics.py")
    print()
    return int(input("Choose your option: "))

def div(a, b):
    print(a, "/", b, "=", a / b)

loop = 1
choice = 0
while loop == 1:
    choice = menu()
    if choice == 1:
        div(float(input("Watt: ")), float(input("Time: ")))
    elif choice == 2:
        div(float(input("Work: ")), float(input("Charge: ")))
    elif choice == 3:
        div(float(input("Force: ")), float(input("Area: ")))
    elif choice == 4:
        div(float(input("Force: ")), float(input("Length: ")))
    elif choice == 5:
        loop = 0

print("Thank you for using studyphysics.py!")
print("Made by Ro706")