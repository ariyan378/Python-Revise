def menu():
    print('\nEnter Your Choice')
    print('1. +')
    print('2. -')
    print('3. *')
    print('4. /')
    print('5. Quit')


while True:

    menu()  
    choice = int(input('Enter Your Choice (1-5): '))

    if choice == 5:
        print('Quitting...')
        break


    num1 = float(input('Enter first number: '))
    num2 = float(input('Enter second number: '))

    if choice == 1:
        print("Result:", num1 + num2)

    elif choice == 2:
        print("Result:", num1 - num2)

    elif choice == 3:
        print("Result:", num1 * num2)

    elif choice == 4:
        if num2 == 0:
            print("Error: Cannot divide by zero")
        else:
            print("Result:", num1 / num2)

    else:
        print("Invalid choice. Try again.")