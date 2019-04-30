import random


class Room:

    def __init__(self, number, type, max_people, comfort):
        self.number = number
        self.type = type
        self.max_people = max_people
        self.comfort = comfort

    def __str__(self):
        s = 'номер '+self.number+' '+self.type+' '+self.comfort+' рассчитан на '+self.max_people+' чел'
        return s

    def __repr__(self):
        return self.__str__()


class Accomodation(Room):

    def __init__(self, number, type, max_people, comfort, food):
        super().__init__(self, number, type, max_people, comfort)
        self.food = food


class Hotel:

    def __init__(self, occupation):
        self.occupation = occupation

    def checking(self, number, date): # метод для проверки заполненности номера
        room = self.occupation[number]
        if room[date] == 'занято':
            return 'занято'
        else:
            return 'свободно'

    def taken(self, number, date, days): # метод, который занимает нужные номера
        for day in range(days):
            self.occupation[number][date+day] = 'занято'

    def __str__(self):
        return str(self.occupation)

    def __repr__(self):
        return self.__str__()


class Client:

    def __init__(self, date_in, name, people, date, days, max_summ):
        self.name = name
        self.date_in = date_in
        self.people = people
        self.date = date
        self.days = days
        self.max_summ = max_summ
        if random.randrange(1, 5) == 1:
            self.agreement = False
        else:
            self.agreement = True

    def __str__(self):
        s = self.date_in + ' '
        s += self.name + ' '
        s += self.people + ' '
        s += self.date + ' '
        s += self.days + ' '
        s += self.max_summ

        return s