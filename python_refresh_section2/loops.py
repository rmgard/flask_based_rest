my_variable = 'hello'

print(my_variable[0])
print(my_variable[1])
print(my_variable[2])
print(my_variable[3])
print(my_variable[4])


## for loop version
for character in my_variable: # iterables are strings, lists, sets, tuples and more
    print(character)


my_list = [1, 3, 5, 7, 9]

for number in my_list:
    print(number ** 2)


user_wants_number = True
while user_wants_number == True:
    print(10)

    user_input = input('Should we print againi? (y/n) ') 
    if user_input == 'n':
        user_wants_number = False
