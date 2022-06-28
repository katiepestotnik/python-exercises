#exercise 1
def calculate():
    operation = input('What calculation would you like to perform? (add, sub, mult, div): ' ).lower()
    num1 = int(input('First number? '))
    num2 = int(input('Second number? '))
    answer = None
    if operation == 'add':
        answer = num1 + num2
    if operation == 'sub':
        answer = num1 - num2
    if operation == 'mult':
        answer = num1 * num2
    if operation == 'div':
        answer = num1 / num2
    return f'Your answer is: {answer}'
#print(calculate())

#exercise 2
def reverse(str):
    return str[::-1]
print(reverse('hello'))

#exercise 2 / loop
def reverse_loop(str):
    new_string = ''
    length = len(str)
    for s in str:
        length -= 1
        #print(str[length])
        new_string += str[length]
    return new_string
#print(reverse_loop('hello again'))

#exercise3
def bank_transations():
    balance = int(input('What is your starting balance?\n'))
    while True:
        user_input = input("Would you like to check balance, deposit or withdraw? Select one: balance, deposit, withdraw or quit to exit\n")
        if user_input == 'balance':
            print(f'Your balance is {balance}')
        if user_input == 'deposit':
            deposit = int(input('How much do you want to deposit?\n'))
            balance += deposit
            print(f'Thank you for your deposit of ${deposit} your new balance is ${balance}')
        if user_input == 'withdraw':
            withdraw = int(input('How much do you want to withdraw?\n'))
            balance -= withdraw
            print(f'You have withdrawn ${withdraw} your new balance is ${balance}')
        if user_input == 'quit':
            print("Thank's, come again!")
            break
#bank_transations()

#exercise4

def alpha():
    string = input("Give me a string\n")
    sort_list = sorted(string)
    new_string = ''
    for s in sort_list:
        new_string += '' + s
    return new_string
print(f'Your sorted string is: {alpha()}')