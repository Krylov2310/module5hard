import time
print('Дополнительное практическое задание по модулю*')
print('Задание "Свой YouTube":')
print('Студент Крылов Эдуард Васильевич')
thanks = 'Благодарю за внимание :-)'
print()


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age

    def __str__(self):
        return self.nickname

    def __hash__(self):
        return self.password

    def __int__(self):
        return self.age



class Video:
    def __init__(self, title: str, duration: int, adult_mode: bool = False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

    def __eq__(self, other):
        return self.title == other.title

    def __contains__(self, title_):
        return title_ in self.title


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def register(self, nickname: str, password, age: int):
        for user in self.users:
            if user.nickname == nickname:
                print(f"Пользователь {nickname} уже существует")
                return

        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user

    def log_out(self):
        self.current_user = None

    def log_in(self, login: str, password: str):
        for user in self.users:
            if login == user.nickname and password == user.password:
                self.current_user = user

    def add(self, *args):
        for video in args:
            if video not in self.videos:
                self.videos.append(video)

    def get_videos(self, video_text: str):
        list_video = []
        for video in self.videos:
            if video_text.upper() in video.title.upper():
                list_video.append(video.title)
        return list_video

    def watch_video(self, video_title: str):
        if not self.current_user:
            print('Войдите в аккаунт, чтобы смотреть видео')
            return

        for j in self.videos:
            if j.title == video_title:
                if j.adult_mode and self.current_user.age < 18:
                    print(f'{self.current_user} Вам нет 18 лет, пожалуйста, покиньте страницу c фильмом '
                          f'"{video_title}"')
                    return

                for i in range(j.duration):
                    print(i + 1, end='->')
                    time.sleep(1)
                    j.time_now += 1
                    j.time_now = 0
                print('Конец видео')
                print(f'{self.current_user}, Вы посмотрели фильм: "{video_title}"')


# Код для проверки:
ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
# print(ur.get_videos('лучший'))
# print(ur.get_videos('ПРОГ'))
print(f'По поиску "лучший" найдено: {ur.get_videos('лучший')}')
print(f'По поиску "ПРОГ" найдено: {ur.get_videos('ПРОГ')}')

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
print()
print(thanks)
