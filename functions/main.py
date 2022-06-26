#exercise 1
def sum_to(n):
    total = 0
    for num in range(n + 1):
        total += num
    return total
print(sum_to(10))

#exercise 2
def largest(list):
    return max(list)
print(largest([2, 10, 1000, 4]))
 
def largest_loop(list):
    largest = list[0]
    for num in list:
        if num > largest:
            largest = num
    return largest
print(largest_loop([2, 10, 2000, 4]))

#exercise 3
def occurances(str1, str2):
    count = str1.count(str2)
    return count
print(occurances("fleep floop", 'fe'))

#exercise 4
def product(*args):
    multi = 1
    for arg in args:
        multi = multi * arg
    return multi
print(product(4, 0.5, 5))


