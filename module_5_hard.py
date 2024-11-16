import time
import random
class User:
    """Класс User, включащий атрибуты nickname, password, age"""
    def __init__(self, nickname:str, password:str, age:int):
        self.nickname = nickname
        self.hashed_password = hash(password)
        self.age = age

    def __str__(self):
        return self.nickname

    def __repr__(self):
        return str(self)

class Video:
    """Класс Video, включающий атрибуты title, duration, time_now, adult_mode"""
    def __init__(self, title:str, duration:int, time_now:int = 0, adult_mode:bool = False):
        self.title = title
        self.duration = duration
        self.adult_mode = adult_mode
        self.time_now = time_now
    def __contains__(self, item):
        if isinstance(item, str):
            return self.title == item
        if isinstance(item, Video):
            return self == item

    def __str__(self):
        return self.title

    def __repr__(self):
        return str(self)

class UrTube:
    """Класс UrTube - имитация видеохостинга"""

    def __init__(self):
        self.users = []
        self.current_user:User | None = None
        self.videos = []

    def log_in(self, nickname:str, password:str):
        password = hash(password)
        for user in self.users:
            if user.nickname != nickname:
                continue
            if user.hashed_password == hash(password):
                self.current_user = user



    def register (self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                print(f"Пользователь {nickname} уже существует")
                return
        user = User (nickname, password, age)
        self.users.append(user)
        self.current_user = user

    def log_out (self):
        self.current_user = None

    def add(self, *videos):
        for video in videos:
            if video in self.videos:
                continue
            else:
                self.videos.append (video)

    def get_videos(self, search_word:str) -> list [Video]:
        search_word = search_word.lower()
        result = []
        for video in self.videos:
            if video.title.lower().count(search_word) > 0:
                result.append(video)

        return result

    def watch_video (self, title:str):
        found_video: Video|None = None
        for video in self.videos:
            if video.title == title:
                found_video = video
                break

        if found_video is None:
            return
        if self.current_user is None:
            print ("Войдите в аккаунт, чтобы смотреть видео")
            return
        if self.current_user.age < 18 and found_video.adult_mode:
            print ("Вам нет 18 лет, пожалуйста покиньте страницу")
            return
        found_video.time_now = 0
        while found_video.time_now < found_video.duration:
            print(found_video.time_now, end=" ")
            found_video.time_now += 1
            time.sleep(1)
        print("Конец видео")
        found_video.time_now = 0



if __name__ == "__main__":
    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

    # Добавление видео
    ur.add(v1, v2)
    # Проверка поиска
    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))

    # Проверка на вход пользователя и возрастное ограничение
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')

    # Проверка входа в другой аккаунт
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user)

    # Попытка воспроизведения несуществующего видео
    ur.watch_video('Лучший язык программирования 2024 года!')
