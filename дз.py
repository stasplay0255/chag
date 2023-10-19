import random

class Human:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.money = 0
        self.alive = True

    def to_study(self):
        print('Время учиться')
        self.progress += 0.12
        self.gladness -= 3

    def to_chill(self):
        print('отдых')
        self.gladness += 5
        self.progress -= 0.1
        self.money -= 5

    def to_sleep(self):
        print('Я буду спать')
        self.gladness += 3

    def to_work(self):
        print('я буду работать')
        self.money += 10

    def is_alive(self):
        if self.progress < -0.5:
            print('Cast out...')
            self.alive = False
        elif self.gladness <= 0:
            print('депрессия...')
            self.alive = False
        elif self.progress > 5:
            print('Пройдено внешне')
            self.alive = False
        elif self.money < -0:
            print('я обонкротилься...')
            self.alive = False

    def end_day(self):
        print(f'Gladness = {self.gladness}')
        print(f'Progress = {round(self.progress, 2)}')
        print(f'Money = {self.money}')

    def live(self, day):
        day = 'Day' + str(day) + 'of' + self.name + 'life'
        print(f'{day:=^50}')
        live_cube = random.randint(1,4)
        if live_cube == 1:
            self.to_study()
            self.end_day()
            self.is_alive()
        elif live_cube == 2:
            self.to_sleep()
            self.end_day()
            self.is_alive()
        elif live_cube == 3:
            if self.money < 10:
                print("Слишком мало денег, надо работать :(")
                self.to_work()
            elif self.progress < 0:
                print('Мне нужно поучиться')
                self.to_study()
            else:
                self.to_chill()
            self.end_day()
            self.is_alive()
        elif live_cube == 4:
            self.to_work()
            self.end_day()
            self.is_alive()

nick = Human(name='Nick')

for day in range(365):
    if nick.alive == False:
        break
    nick.live(day)