    # exercise-01 Vowel or Consonant

# Write the code that:
# 1. Prompts the user to enter a letter in the alphabet:
#      Please enter a letter from the alphabet (a-z or A-Z): 
# 2. Write the code that determines whether the letter entered is a vowel
# 3. Print one of following messages (substituting the letter for x):
#      - The letter x is a vowel
#      - The letter x is a consonant

# Hints:  Use the in operator to check if a character is in another string
#         For example, if some_char in 'abc':
def consonant_vowel():
    letter = input('enter letter of alphabet: ').lower()
    if letter in 'aeiou':
        print(f'{letter} is a vowel')
    elif letter in 'qwrtypsdfghjklzxcvbnm':
        print(f'{letter} is a consonant')
    else:
        print('Neither Silly')
#consonant_vowel()

# exercise-02 Length of Phrase
# Write the code that:
# 1. Prompts the user to enter a phrase:
#      Please enter a word or phrase: 
# 2. Print the following message:
#      - What you entered is xx characters long
# 3. Return to step 1, unless the word 'quit' was entered.
def find_length():
    while True:
        phrase = input('Enter word or phrase to find length or type quit to exit: ')
        if phrase != 'quit':
            print(f'{phrase} is {len(phrase)} characters long')
        if phrase == 'quit':
            print('Game Over!')
            break
#find_length()
# exercise-03 Calculate Dog Years

# Write the code that:
# 1. Prompts the user to enter a dog's age in human years like this:
#      Input a dog's age in human years: 
# 2. Calculates the equivalent dog years, where:
#      - The first two years count as 10 years each
#      - Any remaining years count as 7 years each
# 3. Prints the answer in the following format:
#      The dog's age in dog years is xx

# Hint:  Use the int() function to convert the string returned from input() into an integer
def dog_age():
    age = int(input("Enter dog's age in human years to find out how old the dog is in dog years: "))
    if age <= 2:
        dog_age = age * 10
    else:
        dog_age = (age * 7) + 6
    print(f'The dog is {dog_age} years old in dog years.')
#dog_age()

# exercise-04 What kind of Triangle?

# Write the code that:
# 1. Prompts the user to enter the three lengths of a triangle (one at a time):
#      Enter the lengths of three side of a triangle:
#      a: 
#      b:
#      c:
# 2. Write the code that determines if the triangle is:
#      equalateral - all three sides are equal in length
#      scalene - all three sides are unequal in length
#      isosceles - two sides are the same length
# 3. Print a message such as:
#      - A triangle with sides of <a>, <b> & <c> is a <type of triangle> triangle
def what_triange():
    a = int(input('Triangle length a: '))
    b = int(input('Triangle length b: '))
    c = int(input('Triangle length c: '))
    tri_type = None
    if(a == b and c == a):
        tri_type = 'equilateral'
    if(a == b and a != c):
        tri_type = 'isosceles' 
    if (a == c and a !=b):
        tri_type = 'isosceles' 
    if(b == c and b != a):
        tri_type = 'isosceles'
    if(a != b and a != c):
        tri_type = 'scalene'
    print(f'A triangle with sides of {a}, {b} & {c} is a {tri_type} triangle')
#what_triange()

# exercise-05 Fibonacci sequence for first 50 terms

# Write the code that:
# 1. Calculates and prints the first 50 terms of the fibonacci sequence.
# 2. Print each term and number as follows:
#      term: 0 / number: 0
#      term: 1 / number: 1
#      term: 2 / number: 1
#      term: 3 / number: 2
#      term: 4 / number: 3
#      term: 5 / number: 5
#      etc.

# Hint: The next number is found by adding the two numbers before it
def fibo():
    n1 = 0
    n2 = 1
    count = 0
    while count <= 50:
       add = n1 + n2
       n1 = n2
       n2 = add
       count += 1 
       print(f'Term: {count -1} Fib Number: {n2}')
#fibo()


# exercise-06 What's the  Season?

# Write the code that:
# 1. Prompts the user to enter the month (as three characters):
#      Enter the month of the season (Jan - Dec):
# 2. Then propts the user to enter the day of the month: 
#      Enter the day of the month:
# 3. Calculate what season it is based upon this chart:
#      Dec 21 - Mar 19: Winter
#      Mar 20 - Jun 20: Spring
#      Jun 21 - Sep 21: Summer
#      Sep 22 - Dec 20: Fall
# 4. Print the result as follows:
#      <Mmm> <dd> is in <season> 

# Hints:
# Consider using the in operator to check if a string is in a particular list/tuple like this:
# if input_month in ('Jan', 'Feb', 'Mar'):
#
# After setting the likely season, you can use another if...elif...else statement to "adjust" if
# the day number falls within a certain range.
def season():
    month = input(f'Enter the month of the season (Jan - Dec)').lower()
    day = int(input(f'Enter the day of the month'))
    season = None
    if month in ( 'jan', 'feb','mar'):
        season = 'Winter'
    if month in ( 'apr', 'may','jun'):
        season = 'Spring'
    if month in ( 'jul', 'aug','sept'):
        season = 'Summer'
    if month in ( 'oct', 'nov','dec'):
        season = 'Fall'
    upper = month.upper()
    print(f'{upper}, {day} is in {season}')
#season()