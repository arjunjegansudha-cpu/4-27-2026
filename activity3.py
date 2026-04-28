print("Please select your ride:")
print("1. Bike")
print("2. Car")
print("")

choice=int(input("Enter your choice:"))
if(choice==1):
    print("Which bike you want to ride:")
    print("1. Super73")
    print("2. Surron")
    print("")
    
    choice2=int(input("Enter your bike choice:"))
    if choice2==1:
        print("You have selected Super73")
    elif(choice2==2):
        print("You have selected Suron")
    else:
        print("Invalid input")

elif (choice==2):
    print("Which car you want to ride:")
    print("1. Honda")
    print("2. Bently")
    print("")
    
    choice3=int(input("Enter your cars choice:"))
    if(choice3==1):
        print("You have selected Honda")
    elif(choice3==2):
        print("You have selected Bently")
    else:
        print("Invalid input")

else:
    print("Invalid input")