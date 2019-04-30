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
        print (number)
        for day in range(days):
            self.occupation[number][date+day]='занято'


    def __str__(self):
        return(str(self.occupation))

    def __repr__(self):
        return self.__str__()


class Client:

    def __init__(self, name, date_in, people, date, days, max_summ):
        self.name = name
        self.date_in = date_in
        self.people = people
        self.date = date
        self.days = days
        self.max_summ = max_summ
        self.agreement = True # тут сделать рандом