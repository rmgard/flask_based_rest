lottery_player_dict = {
        'name': 'Rolf',
        'numbers': (5, 9, 12, 3, 1, 21)
        }


class LotteryPlayer:
    def __init__(self, name):
        self.name = "Rolf"
        self.numbers = (5, 9, 12, 3, 1, 21)

    def total(self):
        return sum(self.numbers)


player_one = LotteryPlayer('Rolf')
player_two = LotteryPlayer('John')
# print(player.name)
# rint(player.total())
print(player_one.name == player_two.name)

##

class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []


    def average(self):
        return sum(self.marks)/len(self.marks)

    @staticmethod
    def go_to_school():
        print("I'm going to school!")


    @classmethod
    def no_school(cls):
        print("I'm a {}".format(cls))


anna = Student('Anna', 'MIT')
anna.marks.append(56)
print(anna.marks)
