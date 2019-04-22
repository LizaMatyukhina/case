from declaration import *

def read_file_rooms():
    with open('fund.txt', 'r', encoding='utf8') as f_in:
        rooms = []
        text = f_in.readlines()
        for item in text:
            item.strip('\n')
            element = item.split()
            rooms.append(Room(element[0], element[1], element[2], element[3]))

    return rooms


def variants(rooms):
    options = {}
    type_of_room = {'одноместный': 2900.0, 'двухместный': 2300.0, 'полулюкс': 3200.0, 'люкс': 4100.0}
    type_of_comfort = {'стандарт': 1.0, 'стандарт_улучшенный': 1.2, 'апартамент': 1.5}

    for room in rooms:
        options[room.number] = type_of_room[room.type]*type_of_comfort[room.comfort]

    return options


def food(options):
    lst = []
    type_of_food = {'без': 0.0, 'завтрак': 280.0, 'полупансион': 1000.0}
    for key in options.keys():
        for meal in type_of_food.keys():
            food = (key, options[key]+ type_of_food[meal])
            lst.append(food)

    return lst


def sort(for_sort):
    order = sorted(for_sort, key=lambda x: x[1])
    print(list(reversed(order)))

def read_file_booking():
    pass
    # считывание данных из файла про гостей


def main():
    rooms = read_file_rooms()
    for_sort = food(variants(rooms))
    sort(for_sort)

main()