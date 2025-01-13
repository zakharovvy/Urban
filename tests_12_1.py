import unittest

class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


class Runner_test(unittest.TestCase):
    def setUp(self):  #Позволяет не прописывать имя в каждом отдельном тесте
        self.runner_1 =Runner('Max')
        self.runner_2 = Runner('Alex')

    def test_walk(self):
        for i in range(10):
            self.runner_1.walk()
        self.assertEqual(self.runner_1.distance,50)

    def test_run(self):
        for i in range(10):
            self.runner_1.run()
        self.assertEqual(self.runner_1.distance,100)

    def test_challenge(self):
        for i in range(10):
            self.runner_1.walk()
            self.runner_2.run()
        self.assertNotEqual(self.runner_1.distance,self.runner_2.distance)

    # def test_fake_challenge(self): #- тест, который при любом введенном значении n будет проваливаться
    #     n = int(input("Введите количество кругов для соревнования \n"))
    #     for i in range(n):
    #         self.runner_1.run()
    #     for i in range(n+1):
    #         self.runner_2.walk()
    #     self.assertEqual(self.runner_1.distance,self.runner_2.distance)