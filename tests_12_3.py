import unittest



class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)
        return finishers

def frozen_decorator(func):
    def wrapper(self,*args,**kwargs):
        name_of_class =  self.__class__
        if name_of_class.is_frozen:
            self.skipTest('Тесты в этом кейсе заморожены')
        else:
            return func(self, *args, **kwargs)
    return wrapper




class Runner_test(unittest.TestCase):
    is_frozen = False

    @frozen_decorator
    def setUp(self):  #Позволяет не прописывать имя в каждом отдельном тесте
        self.runner_1 =Runner('Max')
        self.runner_2 = Runner('Andy')

    @frozen_decorator
    def test_walk(self):
        for i in range(10):
            self.runner_1.walk()
        self.assertEqual(self.runner_1.distance,50)

    @frozen_decorator
    def test_run(self):
        for i in range(10):
            self.runner_1.run()
        self.assertEqual(self.runner_1.distance,100)

    @frozen_decorator
    def test_challenge(self):
        for i in range(10):
            self.runner_1.walk()
            self.runner_2.run()
        self.assertNotEqual(self.runner_1.distance,self.runner_2.distance)



class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @frozen_decorator
    def setUp(self):
        self.runner_1 = Runner('Усэйн', 10)
        self.runner_2 = Runner('Андрей', 9)
        self.runner_3 = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        #print(cls.all_results) #Иначе мешает корректно выводить результат
        pass
    @frozen_decorator
    def test_first_tournament(self):
        tour = Tournament(90, self.runner_1,self.runner_3)
        TournamentTest.all_results = tour.start()
        self.assertEqual(TournamentTest.all_results[2],'Ник')
        TournamentTest.all_results = {k: str(v) for k, v in TournamentTest.all_results.items()}

    @frozen_decorator
    def test_second_tournament (self):
        tour2 = Tournament(90, self.runner_2, self.runner_3)
        result_of_tour2 = tour2.start()
        TournamentTest.all_results = result_of_tour2
        TournamentTest.all_results = {k: str(v) for k, v in TournamentTest.all_results.items()}

    @frozen_decorator
    def test_third_tournament(self):
        tour3 = Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        TournamentTest.all_results = tour3.start()
        TournamentTest.all_results = {k: str(v) for k, v in TournamentTest.all_results.items()}




testing = unittest.TestSuite()
testing.addTests(unittest.TestLoader().loadTestsFromTestCase(Runner_test))
testing.addTests(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))
runner = unittest.TextTestRunner(verbosity=2)
runner.run(testing)
