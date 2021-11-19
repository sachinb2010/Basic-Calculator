def add(number,numbers):

    return number+numbers
def subtract():
    return number-numbers
def multiply():
    return number*numbers
def divide():
    return numbers%numbers


print("Welcome to the calculator ")
while True:

    number=int(input("Enter the Number : "))
    numbers=int(input("Enter the Number : "))

    print('''Press 1. for add
        press 2. for subteract
        press 3. for multiply
        press 4. for divide 
        press 5. for end 
    ''')
    choice=int(input("please enter your choice"))

    if choice == 1:
        ans=add(number,numbers)
        print(ans)
    if choice == 2:
        ans=subtract(number,numbers)
        print(ans)
    if choice == 3:
        ans=multiply(number,numbers)
        print(ans)
    if choice == 4:
        ans=divide(number,numbers)
        print(ans)
    if choice == 5:
        print("please visit again Thankyou")
        exit()
        

