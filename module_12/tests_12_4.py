import unittest
import logging



format_logs = '%(levelname)s - %(message)s'
logging.basicConfig(level=20, filemode='w', filename='../runner_tests.log', encoding='UTF-8', format=format_logs)

class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Runner_test(unittest.TestCase):
    is_frozen = False

    # def setUp(self):
    #     format_logs = '%(levelname)s - %(message)s'
    #     logging.basicConfig(level=20, filemode='w', filename='runner_tests.log', encoding='UTF-8', format=format_logs)

    def test_walk(self):
        try:
            runner_1 = Runner('Вася', speed=-5)
            for i in range(10):
                runner_1.walk()
            self.assertEqual(runner_1.distance, 50)
            logging.info('"test_walk"выполнен успешно')
        except ValueError as e:
            logging.warning('Неверная скорость для Runner', exc_info=True)
            self.assertEqual(str(e), f'Скорость не может быть отрицательной, сейчас -5')



    def test_run(self):
        try:
            runner_2 = Runner(2.6)
            for i in range(10):
                runner_2.run()
            self.assertEqual(runner_2.distance, 100)
            logging.info('"test_run"выполнен успешно')
        except TypeError as e:
            logging.warning("Неверный тип данных для объекта Runner", exc_info=True)
            self.assertEqual(str(e), f'Имя может быть только строкой, передано {type(2.6).__name__}')



if __name__ == '__main__':
    unittest.main()
#
# t = Tournament(101, first, second)
# print(t.start())