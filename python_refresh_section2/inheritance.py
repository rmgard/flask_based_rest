class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)

    # def friend(self, friend_name):
        # return a new student called 'friend_name' in the same school as self
    #    return Student(friend_name, self.school)

    @classmethod
    def friend(cls, origin, friend_name, salary):
        return cls(friend_name, origin.school, salary)


anna = Student("Anna", "Oxford")

friend = anna.friend("greg")
print(friend.name)
print(friend.school)


##


class WorkingStudent(Student):
    def __init__(self, name, school, salary):
        super().__init__(name, school)
        self.salary = salary


anna = WorkingStudent("Anna", "Oxford", 20.00)
print(anna.salary)

# Greg is NOT a working student
friend = WorkingStudent.friend(anna, "Greg", 17.50)
print(friend.name)
print(friend.school)

