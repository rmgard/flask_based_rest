my_variable = 'hello'

grade_one = 77
grade_two = 80
grade_three = 90
grade_four = 95
grade_five = 100

grades = [77, 80, 90, 95, 100, 105, 107]
tuple_grades = (77, 80, 90, 95, 100, 105, 107) # immutable
set_grades = {77, 80, 90, 100, 100} # unique & unordered

print(sum(grades) / len(grades))
grades.append(108)

print(grades)

tuple_grades = tuple_grades + (100, )

print(tuple_grades)

grades[0] = 60
print(grades[0])


## Set operations
your_lottery_numbers = {1, 2, 3, 4, 5}
winning_numbers = {1, 3, 5, 7, 9, 11}

print(your_lottery_numbers.intersection(winning_numbers))
print(your_lottery_numbers.union(winning_numbers))
print({1, 2, 3, 4}.difference({1,2}))
