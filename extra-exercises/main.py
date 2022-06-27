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
print(reverse_loop('hello again'))