class Room:

    def __init__(self, number, type, max_people, comfort):
        self.number = number
        self.type = type
        self.max_people = max_people
        self.comfort = comfort


class Accomodation(Room):

    def __init__(self, number, type, max_people, comfort, food):
        super().__init__(self, number, type, max_people, comfort)
        self.food = food


class Hotel:

    def __init__(self, occupation):
        self.occupation = occupation


class Client:

    def __init__(self, name, date, people, days, max_summ):
        self.name = name
        self.date = date
        self.people = people
        self.days = days
        self.max_summ = max_summ