# Exercises with strings
# Using the Python documentation on strings (https://docs.python.org/3/library/stdtypes.
# html?#text-sequence-type-str), solve the following exercises:

# 1. Initialize the string “abc” on a variable named “s”:

print('\n----- Question 1.1 ----')
# 1.1 Use a function to get the length of the string.
s = 'abc'
def length(string):
    return print(f'Length: {len(string)}')

length(s)

print('\n----- Question 1.2 ----')
# 1.2 Write the necessary sequence of operations to transform the string “abc” in
    # “aaabbbccc”. Suggestion: Use string concatenation and string indexes.
def char_multiplier(string):
    new = ''
    for char in string:
        new += char*3
    return new

char_multiplier(s)
print(f'String Multiplied: {char_multiplier(s)}')
# 2. Initialize the string “aaabbbccc” on a variable named “s”:
print('\n----- Question 2.1 ----')
# 2.1 Use a function that allows you to find the first occurence of “b” in the string,
# and the first occurence of “ccc”.
string = char_multiplier(s)
sub_list = ['b', 'ccc']
def first_occurence(string, sub_list):
    indices = []
    for sub in sub_list:
        indices.append((sub, f'Index: {string.find(sub)}'))
    return indices
print(first_occurence(string, sub_list))

print('\n----- Question 2.2 ----')
# 2.2 Use a function that allows you to replace all occurences of “a” to “X”, and
# then use the same function to change only the first occurence of “a” to “X”.
all = True
all2 = False
def change_occurence(string, all):
    if all:
        return string.replace('a', 'x')
    else:
        return string.replace('a', 'x', 1)
print(change_occurence(string, all))
print(change_occurence(string, all2))

# 3. Starting from the string “aaa bbb ccc”, what sequences of operations do you need
# to arrive at the following strings? You can use the “replace” function.
# 3.1 “AAA BBB CCC”
str = 'aaa bbb ccc'
print(str.upper())

# 3.2 “AAA bbb CCC”
print(str.replace('a', 'A').replace('c', 'C'))
