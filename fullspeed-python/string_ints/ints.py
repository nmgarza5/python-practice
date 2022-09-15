# Exercises with numbers

print('----- Question 1 ----')
# 1. Try the following mathematical calculations and guess what is happening: ((3 / 2)),
    # ((3 // 2)), ((3 % 2)), ((3**2)).
print(f'Float: {3 / 2 }')
print(f'Integer: {3 // 2 }')
print(f'Modulo: {3 % 2 }')
print(f'Exponent: {3 ** 2 }')

# Suggestion: check the Python library reference at https://docs.python.org/3/library/
    # stdtypes.html#numeric-types-int-float-complex.

print('\n----- Question 2 ----')
# 2. Calculate the average of the following sequences of numbers:
a = [2, 4]
b = [4, 8, 9]
c = [12,14/6, 15]

def getAverage(list):
    return print(f'Average: {sum(list) / len(list)}')
getAverage(a)
getAverage(b)
getAverage(c)

print('\n----- Question 3 ----')
# 3. The volume of a sphere is given by (4/3 * pi * rˆ3). Calculate the volume of a sphere
    # of radius 5. Suggestion: create a variable named “pi” with the value of 3.1415.
def calc_sphere_vol(radius, pi=3.1415):
    return print(f'Volume: {(4/3 * pi * (radius ** 3))}')
calc_sphere_vol(5)

print('\n----- Question 4 ----')
# 4. Use the modulo operator (%) to check which of the following numbers is even or
    # odd: (1, 5, 20, 60/7). Suggestion: the remainder of (x/2) is always zero when (x) is even.
nums = [1, 5, 20, 60/7]
def odd_or_even(list):
    return print(f'Is Even: {[(num, num % 2 == 0) for num in list]}')
odd_or_even(nums)
# 5. Find some values for (x) and (y) such that (x < 1/3 < y) returns “True” on the
    # Python REPL. Suggestion: try (0 < 1/3 < 1) on the REPL.
print('\n----- Question 5 ----')
print(0 < 1/3 < 1)
