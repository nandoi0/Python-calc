



# functions
def print_menu():
    print("================================")
    print("pyCalc 3000")
    print("================================")

    print("[1] Sum")
    print("[2] Subtract")
    print("[3] Multiply")
    print("[4] Divide")
    print("[5] Repeat message")

    #ask for a message
    #ask for the num times



    # plain instructions 

print_menu()
option = input("Please select an option")

num1 = float(input("Please provide the num 1:"))
num2 = float(input("Please provide the num 2:"))

if option == "1":
    res= num1 + num2
    
    print(f"The result is: {res}")

# else if the option is 2, ask for the number and show the result of num1

elif option == "2":
    res = num1 - num2
    print(f"The result is: {res}")

elif option == "3":
    res = num1 * num2
    print(f"The result is: {res}")

elif option == "4":
    if num2 == 0:
        print("Dont divide by zero")
    else:
        res = num1 / num2
        print(f"The result is: {res}")

elif option == "5":
    message = input("Provide your messsage: ")
    times = input("How many times?")

    for i in range(0, times):
        print(message)