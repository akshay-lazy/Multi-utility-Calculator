
def arithmetic():
    print("\n--- Arithmetic Operations ---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")

    choice = int(input("Choose operation: "))

    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if choice == 1:
        print("Result:", a + b)

    elif choice == 2:
        print("Result:", a - b)

    elif choice == 3:
        print("Result:", a * b)

    elif choice == 4:
        if b != 0:
            print("Result:", a / b)
        else:
            print("Cannot divide by zero")

    elif choice == 5:
        print("Result:", a % b)

    else:
        print("Invalid choice")


def currency():
    print("\n--- Currency Conversion ---")
    print("1. INR to USD")
    print("2. USD to INR")

    choice = int(input("Choose conversion: "))
    amount = float(input("Enter amount: "))

    if choice == 1:
        print("Converted:", amount / 88)

    elif choice == 2:
        print("Converted:", amount * 88)

    else:
        print("Invalid choice")

    print("Note: Example exchange rate only.")


def unit_conversion():
    print("\n--- Unit Conversion ---")
    print("1. KM to Miles")
    print("2. Miles to KM")
    print("3. Celsius to Fahrenheit")
    print("4. Fahrenheit to Celsius")
    print("5. KG to Grams")
    print("6. Grams to KG")

    choice = int(input("Choose conversion: "))
    value = float(input("Enter value: "))

    if choice == 1:
        print("Miles:", value * 0.621371)

    elif choice == 2:
        print("KM:", value / 0.621371)

    elif choice == 3:
        print("Fahrenheit:", (value * 9/5) + 32)

    elif choice == 4:
        print("Celsius:", (value - 32) * 5/9)

    elif choice == 5:
        print("Grams:", value * 1000)

    elif choice == 6:
        print("KG:", value / 1000)

    else:
        print("Invalid choice")


# Main program

while True:

    print("\n===== MULTI-UTILITY CALCULATOR =====")
    print("1. Arithmetic")
    print("2. Currency Conversion")
    print("3. Unit Conversion")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        arithmetic()

    elif choice == 2:
        currency()

    elif choice == 3:
        unit_conversion()

    elif choice == 4:
        print("Thank you for using the calculator!")
        break

    else:
        print("Invalid choice. Try again.")
