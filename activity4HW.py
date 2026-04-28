try:
    age = int(input("Enter your age: "))
    valid_range = range(10, 21)

    if age in valid_range:
        print("The age is between 10 and 20.")
    else:
        print("The age is NOT between 10 and 20.")
except ValueError:
    print("Please enter a valid number.")