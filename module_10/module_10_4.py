import random
import threading
import queue
import time
from queue import Queue
from threading import Thread

class Table:
    def __init__(self, number: int):
        self.number = number
        self.guest = None

class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        rand_int = random.randint(3, 10)
        time.sleep(rand_int)

class Cafe:
    def __init__(self, *tables: Table):
        self.tables = tables
        self.queue = Queue()

    def guest_arrival(self, *guests: Guest):
        for guest in guests:
            seated = False
            for table in self.tables:
                if table.guest is None:
                    table.guest = guest
                    print(f"{guest.name} сел за стол номер {table.number}.")
                    guest.start()
                    seated = True
                    break
            if not seated:
                self.queue.put(guest)
                print(f"{guest.name} в очереди.")

    def discuss_guests(self):
        while not self.queue.empty() or any(table.guest is not None for table in self.tables):
            for table in self.tables:
                if table.guest and not table.guest.is_alive():
                    print(f"{table.guest.name} покушал(-а) и ушёл(ушла)")
                    print(f"Стол номер {table.number} свободен")
                    table.guest = None

                if table.guest is None and not self.queue.empty():
                    next_guest = self.queue.get()
                    table.guest = next_guest
                    next_guest.start()
                    print(f"{next_guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}.")




tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()





#
