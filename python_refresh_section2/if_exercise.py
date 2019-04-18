def who_do_you_know():
    string_of_known_people = input('Enter a list of people you know without any commas: ')
    people_list = string_of_known_people.split()
    return(people_list)


def ask_user(list_of_people):
    name = input("What is the name of a person you know? ")
    if name in list_of_people:
        print('You know {}!'.format(name))
    else:
        print('You dont know {}'.format(name))
