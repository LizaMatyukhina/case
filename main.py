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
    occupation = {}
    for room in rooms:
        empty_days = {}
        for day in range(1, 6):
            empty_days[day] = 'свободно'
        occupation[room.number] = empty_days
    return Hotel(occupation)


def variants(rooms): # создание словаря со стоимостью БЕЗ ПИТАНИЯ и
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
    with open('booking.txt', 'r', encoding='utf-8-sig') as f_in:
        clients = []
        text = f_in.readlines()
        for item in text:
            item.strip('\n')
            element = item.split()
            clients.append(Client(element[0], element[1]+' '+element[2]+' '+element[3], element[4], element[5],
                                  element[6], element[7]))

    return clients


def hotel_filling(sorted_rooms, clients, hotel, rooms):
    first_date_in = clients[0].date_in
    last_date_in = clients[len(clients)-1].date_in
    start = first_date_in.split('.')[0]
    for data in range(int(start), int(last_date_in.split('.')[0]) + 1):
            for client in clients:
                search_people = int(client.people) # количество людей в номер
                search_summ = int(client.max_summ) # максимальная стоимость
                search_date = int(client.date.split('.')[0])
                search_days = int(client.days)

                room_res = searching(sorted_rooms, search_people, search_summ, search_date, search_days, hotel, client.agreement)
                counter = 0
                agreement = client.agreement
                while first_date_in == client.date_in:

                    if room_res != 0:
                        print('Поступила заявка на бронирование: ' + '\n')
                        print(client)
                        print(hotel)
                        print('Найден:')
                        for room in rooms:
                            if room.number == room_res[0][0]:
                                print(room, end='. ')
                        print('фактически', search_people, 'чел. ', room_res[0][3], ' стоимость ', room_res[0][1]*room_res[1], ' руб./сутки')
                        if agreement:
                            print('Клиент согласен. Номер забронирован.')
                        else:
                            print('Клиент отказался!!')
                        print(hotel)
                    else:
                        print('Предложений по данному запросу нет. В бронировании отказано.')
                    counter += 1
                    first_date_in = clients[counter].date_in


def searching(sorted_rooms, search_people, search_summ, search_date, search_days, hotel, agreement, percent=1.0):
    switch = 0
    for room in sorted_rooms:
        if search_people == room[2] and search_summ > room[1]:
            if hotel.checking(room[0], search_date) != 'занято':
                switch = [room, percent]
                if agreement:
                    hotel.taken(room[0], search_date, search_days)
                break

    if switch == 0 and search_people < 7:
        return searching(sorted_rooms, search_people+1, search_summ, search_date, search_days, hotel, 0.7)

    return switch



def main():
    rooms = read_file_rooms() # читаем и кладем в список экземпляры комнат
    hotel = empty_hotel(rooms) # создаем "свободный" отель
    for_sort = food(variants(rooms), rooms) # формируем кортежи
    sorted_rooms = sort(for_sort) # сортируем кортежи
    clients = read_file_booking() # читаем и кладем в список экземпляры клиентов
    hotel_filling(sorted_rooms, clients, hotel, rooms)


main()