from declaration import *

def read_file_rooms(): # считывание комнат из файла и формирование элементов класса комнаты
    with open('fund.txt', 'r', encoding='utf8') as f_in:
        rooms = []
        text = f_in.readlines()
        for item in text:
            item.strip('\n')
            element = item.split()
            rooms.append(Room(element[0], element[1], element[2], element[3]))


    return rooms

def empty_hotel(rooms): # получаем пустой отель, где для всех номеров 31 день свободный
    empty_days = {}
    for day in range(1, 32):
        empty_days[day] = 'свободно'
    occupation = {}
    for room in rooms:
        occupation[room.number] = empty_days
    return Hotel(occupation)



def variants(rooms): # создание словаря со стоимостью БЕЗ ПИТАНИЯ
    options = {}
    type_of_room = {'одноместный': 2900.0, 'двухместный': 2300.0, 'полулюкс': 3200.0, 'люкс': 4100.0}
    type_of_comfort = {'стандарт': 1.0, 'стандарт_улучшенный': 1.2, 'апартамент': 1.5}

    for room in rooms:
        options[room.number] = type_of_room[room.type]*type_of_comfort[room.comfort]

    return options


def food(options, rooms): # формирование кортежей с номером, питанием, количеством человек и типом питания
    lst = []
    type_of_food = {'без питания': 0.0, 'завтрак': 280.0, 'полупансион': 1000.0}
    for key in options.keys():
        for meal in type_of_food.keys():
            for room in rooms:
                if room.number == key:
                    food = (key, options[key]+ type_of_food[meal], int(room.max_people),meal)
                    lst.append(food)

    return lst


def sort(for_sort): # сортировка кортежей
    order_ = sorted(for_sort, key=lambda x: x[1])
    order__ = list(reversed(order_))
    order = sorted(order__, key=lambda x: x[2])
    return order

def read_file_booking(): # считывание данных из файла про гостей
    with open('booking.txt', 'r', encoding='utf8') as f_in:
        clients = []
        text = f_in.readlines()
        for item in text:
            item.strip('\n')
            element = item.split()
            clients.append(Client(element[0], element[1]+' '+element[2]+' '+element[3], element[4], element[5],
                                  element[6], element[7]))

    return clients




def hotel_filling(sorted_rooms, clients, hotel, rooms):

    for client in clients:
        search_people = client.people # количество людей в номер
        search_summ = client.max_summ # максимальная стоимость
        search_date = int(client.date.split('.')[0])
        search_days = int(client.days)
        room_res = searching(sorted_rooms, search_people, search_summ, search_date, search_days, hotel)
        if room_res != 0:
            print ('Найден: \n')
            for room in rooms:
                if room.number == room_res[0]:
                    print(room)






def searching(sorted_rooms, search_people, search_summ, search_date, search_days, hotel):
    switch = 0
    for room in sorted_rooms:
        if search_people == room[3] and search_summ>room[2]:
            if hotel.checking(room[0], search_date) == 'занято':
                continue
            else:
                switch = room
                hotel.taken(room[0], search_date, search_days)
    return switch



def main():
    rooms = read_file_rooms() # читаем и кладем в список экземпляры комнат
    hotel = empty_hotel(rooms) # создаем "свободный" отель
    for_sort = food(variants(rooms), rooms) # формируем кортежи
    sorted_rooms = sort(for_sort) # сортируем кортежи
    clients = read_file_booking() # читаем и кладем в список экземпляры клиентов

    hotel_filling(sorted_rooms, clients, hotel, rooms)

    print(sorted_rooms)
    print(hotel)

main()