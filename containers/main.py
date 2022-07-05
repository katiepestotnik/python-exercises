# # exercise 1
# students = ['bob', 'joe', 'sandy', 'cindy']
# print(students[1])
# print(students[-1])

# #exercise 2
#foods = ('fries', 'pizza', 'ice cream', 'chocolate')
# for food in foods:
#     print(f'{food} is a good food')

# #exercise 3
# for food in foods[-2:]:
#       print(food)

# #exercise 4
# home_town = {
#     'city': 'Arvada',
#     'state': 'Colorado',
#     'population': 1000
# }
# print(f'I was born in {home_town["city"]}, {home_town["state"]} with a population of {home_town["population"]}')

# # exercise 5
# for key, val in home_town.items():
#     print(f'{key} = {val}')

# #exercise 6
# cohort = []
# for idx, student in enumerate(students):
#     cohort.append({
#         'student': student,
#         'fav_foods': foods[idx]
#     })
# for student in cohort:
#     print(student)
 
# #exercise 7   
# awesome_students = [f'{student} is awesome' for student in students]
# print(awesome_students)

# #exercise 8
# a_foods = [food for food in foods if 'a' in food]
# print(a_foods)
