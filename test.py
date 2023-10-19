from random import randint

class Player:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.score = 0

    def show_info(self):
        print('Name:', self.name)
        print('Hp:', self.hp)
        print('Score:', self.score)

    def set_name(self, new_name):
        self.name = new_name

    def set_hp(self, hp):
        '''
        if hp < 100 and hp > 0:
            self.hp = hp
        else:
            print('Ошибка hp')
            '''
        self.hp = hp

    def set_score(self, score):
        if score > 0:
            self.score = score

    def is_alive(self):
        return self.hp > 0

player = Player('krytoi')
player.show_info()

while player.is_alive():
    num = randint(1, 2)
    if num == 1:
        damage = randint(1, 20)
        player.set_hp(player.hp - damage)
        print(f'{player.name} получил урон: {damage}')
    elif num == 2:
        score = randint(1, 10)
        player.set_score(player.score + score)
        print(f'{player.name} получил очков: {score}')



player.show_info()

