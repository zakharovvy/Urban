import threading
import time

class Knight(threading.Thread):
    def __init__(self,name:str, power:int):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power
        self.counter_days = 0
        self.enemy = 100
    def run (self):
        print (f"{self.name}, на вас напали!")
        while self.enemy != 0:
            self.counter_days += 1
            self.enemy -=self.power
            print(f"{self.name} сражается {self.counter_days} дней..., осталось {self.enemy} вражеских воинов.\n")
            time.sleep(1)
        print(f"{self.name} одержал победу спустя {self.counter_days} дней(дня)!")


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()