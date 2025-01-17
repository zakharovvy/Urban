import math
class Figure:
    sides_count = 0
    def __init__(self, color: tuple[int, int, int], *sides: list):
        self.__sides = [1] * self.__class__.sides_count
        self.__color = color
        self.filled = True

        if self.__is_valid_sides(*sides):
            self.set_sides(*sides)

    def get_color(self):
        return (list(self.__color))

    def __is_valid_color(self, r:int,g:int,b:int):
        if isinstance(r, int) and isinstance(g, int) and isinstance(b, int):
            if (0 <= r <= 255 and
                0 <= g <= 255 and
                0 <= b <= 255):
                return True
            else:
                return False
        else:
            return False

    def  set_color(self, r:int,g:int,b:int):
        if self.__is_valid_color(r, g, b):
            self.__color = (r, g, b)
        else:
            pass

    def __is_valid_sides(self, *new_sides):
        if len(new_sides) != len(self.__sides):
            return False
        for side in new_sides:
            if not isinstance(side, int) or side <= 0:
                return False
        return True


    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)


class Circle (Figure):
    sides_count = 1
    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        if len(self.get_sides()) == 1:
            self.__radius = self.get_sides()[0] / (2 * math.pi)

    def get_square(self):
        return math.pi * (self.__radius ** 2)


class Triangle (Figure):
    sides_count = 3
    def get_square(self):
        a, b, c = self.get_sides()
        s = (a + b + c) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))


class Cube (Figure):
    sides_count = 12

    def __init__(self, color, side_length, *sides):
        super().__init__(color, *sides)
        self.set_sides(*[side_length] * self.__class__.sides_count)

    def get_volume(self):
        side_length = self.get_sides()[0]
        return side_length ** 3

circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())