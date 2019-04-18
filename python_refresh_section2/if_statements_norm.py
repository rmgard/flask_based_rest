## Exercise

def who_do_you_know():
    """
    Ask the user for a list of people they know
    Split the string into a list
    Return that list
    """
    people = input('Enter the names of the people you know, separated by commas: ') # John, Rolf, Anna, Greg

    people_without_spaces = [person.strip() for person in people.split(',')]

    return people_without_spaces


def ask_user():
    """
    Ask the user for their name
    See if their name is in the list of people they know
    Print out that they know the person
    """
    person = input('Enter the person you know: ')
    if person in who_do_you_know():
        print('YOU KNOW {}'.format(person))
        

