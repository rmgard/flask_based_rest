my_list = [0, 1, 2, 3, 4]
an_equal_list = [x for x in range(5)] # [0, 1, 2, 3, 4]

multiply_list = [x * 3 for x in range(5)]
print(multiply_list)

print(8 % 3) # 8 / 3 == 6r2, so 8 % 3 == 2

print(9 % 2) # 4 % 2 == 0, 5 % 2 == 1

print([n for n in range(10) if n % 2 == 0])

people_you_know = ['Rolf', ' John', 'anna', 'GREG']
normalized_people = [person.strip().lower() for person in people_you_know]
print(normalized_people)
