import random, sys, os
import pygame


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)

    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()

    return image 


MANA = 12 #

def poison(a, time):
    if time:
        a.hp -= 1
        if random.randint(0, 1):
            a.atk -= 1
        time -= 1


def vigilant(a, time):
    if time:
        a.sup_atk = 2
        time -= 1

def bleeding(a, lvl, time):
    if time:
        if lvl == 1:
            a.hp -= 1
        elif lvl == 2:
            a.hp -= 2
        else:
            a.hp -= 3
            if random.randint(0, 4):
                a.is_poisoned += 1
        time -= 1

def shine(a, lvl, time):
    if time:
        if lvl == 1:
            a.hp -= 1
        elif lvl == 2:
            a.hp -= (random.randint(0, 1) + 1)
        if lvl >= 3:
            a.hp -= 1
            a.in_game = (False, 1)
        time -= 1

def devastated(a, lvl, time):
    if time:
        a.hp -= (lvl - 1)
        a.is_poisoned=False
        a.is_afraid=False
        a.is_wet=False
        a.is_burn=False
        a.is_windy=False
        a.is_devastated=False
        a.is_illuminated=False
        a.is_illusion=False
        a.is_bleeding=False
        a.is_vigilant=False
        a.is_protected=False
        time -= 1




class Card():
    def __init__(self, is_poisoned=False, is_afraid=False,
                 is_wet=False, is_burn=False, is_windy=False, is_devastated=False,
                 is_illuminated=False, is_illusion=False, is_bleeding=False, is_vigilant=False,
                 is_protected=False, hp=10, purpose=False, act1_mana=0, act2_mana=0, in_game=True, flag=True, atk=0, type=0, sup_atk=0, txt1=None, txt2=None):
        self.is_poisoned = is_poisoned # эффект яд
        self.is_afraid = is_afraid # эффект страх
        self.is_wet = is_wet # эффект сырости
        self.is_burn = is_burn # эффект горение
        self.is_windy = is_windy # эффект ветренности
        self.is_devastated = is_devastated # эффект опустошение
        self.is_illuminated = is_illuminated # эффект свет
        self.is_illusion = is_illusion # эффект иллюзия
        self.is_bleeding = is_bleeding # эффект кровотечение
        self.is_vigilant = is_vigilant # эффект бдительность
        self.is_protected = is_protected # эффект щит
        self.hp = hp # здоровье
        self.purpose = purpose # цель действий
        self.act1_mana = act1_mana # мана за использование 1ого действие
        self.act2_mana = act2_mana # мана за использование 2ого действие
        self.in_game = in_game # игровая ли карта или нет (стан)
        self.flag = flag # использованно ли действие в этом ходу(1 - не использованно, 0 - использованно)
        self.atk = atk # атака
        self.type = type # тип
        self.all_stats = [self.is_poisoned,
                    self.is_afraid,
                    self.is_wet,
                    self.is_burn,
                    self.is_windy,
                    self.is_devastated,
                    self.is_illuminated,
                    self.is_illusion,
                    self.is_bleeding,
                    self.is_vigilant,
                    self.is_protected]

        def next_step(self):
            self.is_poisoned = is_poisoned # эффект яд
            self.is_afraid = is_afraid # эффект страх
            self.is_wet = is_wet # эффект сырости
            self.is_burn = is_burn # эффект горение
            self.is_windy = is_windy # эффект ветренности
            self.is_devastated = is_devastated # эффект опустошение
            self.is_illuminated = is_illuminated # эффект свет
            self.is_illusion = is_illusion # эффект иллюзия
            self.is_bleeding = is_bleeding # эффект кровотечение
            self.is_vigilant = is_vigilant # эффект бдительность
            self.is_protected = is_protected # эффект щит


        def act1(self, MANA):
            '''Функция для 1ого действия'''
            if MANA >= self.act1_mana and self.flag:
                MANA -= self.act1_mana
                self.flag = 0

        def act2(self, MANA):
            '''Функция для 2ого действия'''
            if MANA >= self.act1_mana and self.flag:
                MANA -= self.act1_mana
                self.flag = 0


class Elemental(Card):
    def __init__(self, is_poisoned=False, is_afraid=False,
                 is_wet=False, is_burn=False, is_windy=False, is_devastated=False,
                 is_illuminated=False, is_illusion=False, is_bleeding=False, is_vigilant=False,
                 is_protected=False, hp=10, purpose=False, act1_mana=0, act2_mana=0, act3_mana=3, level=1, in_game=True, flag=True, atk=0, type=0, txt1=None, txt2=None):
        super().__init__(is_poisoned, is_afraid, is_wet, is_burn, is_windy, is_devastated,
                 is_illuminated, is_illusion, is_bleeding, is_vigilant,
                 is_protected, hp, purpose, act1_mana, act2_mana, in_game, flag, atk, type, txt1, txt2)
        self.cost_upgrade = act3_mana
        self.level = level

    def upgrade(self, MANA):
        '''у каждой карты данного класса есть доп функция
                УЛУЧШЕНИЕ уровня карты(ур + 1)'''
        MANA += 1
        return MANA


class Shadow(Elemental):
    def __init__(self, is_poisoned=False, is_afraid=False,
                 is_wet=False, is_burn=False, is_windy=False, is_devastated=False,
                 is_illuminated=False, is_illusion=False, is_bleeding=False, is_vigilant=False,
                 is_protected=False, hp=10, purpose=False, act1_mana=7, act2_mana=3, act3_mana=3, level=1, in_game=True, flag=True, atk=0, type=0, txt1=None, txt2=None):
        super().__init__(is_poisoned, is_afraid, is_wet, is_burn, is_windy, is_devastated,
                 is_illuminated, is_illusion, is_bleeding, is_vigilant,
                 is_protected, hp, purpose, act1_mana, act2_mana, act3_mana, level, in_game, flag, atk, type, txt1, txt2)

        self.image = load_image('Cards/Card_1.png')
        self.txt1 = "1-е: Удар по карте"
        self.txt2 = "2-е: Уменьшить урон"

    def act1(self, MANA):
        '''Цель получает стан 1/2
            Все впажеские карты страх level/2'''
        return 'bleeding'
    
    def act2(self, MANA):
        '''Все впажеские карты страх level/1(50% шанс)
            и 1 атк'''
        return 'vigilant'

    def next_move(self):
        self.is_afraid = False


class Rodia(Elemental):
    def __init__(self, is_poisoned=False, is_afraid=False,
                 is_wet=(1, 10000), is_burn=False, is_windy=False, is_devastated=False,
                 is_illuminated=False, is_illusion=False, is_bleeding=False, is_vigilant=False,
                 is_protected=False, hp=10, purpose=False, act1_mana=4, act2_mana=5, act3_mana=3, level=1, in_game=True, flag=True, atk=0, type=0, txt1=None, txt2=None):
        super().__init__(is_poisoned, is_afraid, is_wet, is_burn, is_windy, is_devastated,
                 is_illuminated, is_illusion, is_bleeding, is_vigilant,
                 is_protected, hp, purpose, act1_mana, act2_mana, act3_mana, level, in_game, flag, atk, type, txt1, txt2)

        self.image = load_image('Cards/Card_11.png')
        self.txt1 = "1-е: Отравление карт"
        self.txt2 = "2-е: Защита карты"

    def act1(self, MANA):
        '''Цель получает 3 урона
            2 рандомные карты сырость'''
        return 'poison'

    def act2(self, MANA):
        '''Все впажеские карты сырость level/1
            и цели 2 HP + 2 HP если сырость '''
        return 'proteck'


class Shiny(Elemental):
    def __init__(self, is_poisoned=False, is_afraid=False,
                 is_wet=False, is_burn=False, is_windy=False, is_devastated=False,
                 is_illuminated=False, is_illusion=False, is_bleeding=False, is_vigilant=False,
                 is_protected=False, hp=10, purpose=False, act1_mana=5, act2_mana=2, act3_mana=3, level=1, in_game=True, flag=True, atk=0, type=0, txt1=None, txt2=None):
        super().__init__(is_poisoned, is_afraid, is_wet, is_burn, is_windy, is_devastated,
                 is_illuminated, is_illusion, is_bleeding, is_vigilant,
                 is_protected, hp, purpose, act1_mana, act2_mana, act3_mana, level, in_game, flag, atk, type, txt1, txt2)

        self.image = load_image('Cards/Card_9.png')
        self.txt1 = "1-е: Увеличение урона"
        self.txt2 = "2-е: Уменьшить урон"

    def act1(self, MANA):
        '''Цель получает свет ур/1 и 2 атк'''
        
        return 'shine'
    def act2(self, MANA):
        '''Все впажеские карты 1 или 2 урона  и 50% шанс 1 урон каждой своей карье'''
        
        return 'vigilant'


class Oilus(Elemental):
    def __init__(self, is_poisoned=False, is_afraid=False,
                 is_wet=False, is_burn=(1, 1000000000), is_windy=False, is_devastated=False,
                 is_illuminated=False, is_illusion=False, is_bleeding=False, is_vigilant=False,
                 is_protected=False, hp=10, purpose=False, act1_mana=1, act2_mana=4, act3_mana=3, level=1, in_game=True, flag=True, atk=0, type=0, txt1=None, txt2=None):
        super().__init__(is_poisoned, is_afraid, is_wet, is_burn, is_windy, is_devastated,
                 is_illuminated, is_illusion, is_bleeding, is_vigilant,
                 is_protected, hp, purpose, act1_mana, act2_mana, act3_mana, level, in_game, flag, atk, type, txt1, txt2)

        self.image = load_image('Cards/Card_8.png')
        self.txt1 = "1-е: Увеличение хп"
        self.txt2 = "2-е: Увеличение урона"

    def act1(self, MANA):
        '''Цель получает горение 1/1'''
        
        return 'afraid'


    def act2(self, MANA):
        '''выбранной карте атк + 3'''
        
        return 'shine'


class Silf(Elemental):
    def __init__(self, is_poisoned=False, is_afraid=False,
                 is_wet=False, is_burn=False, is_windy=False, is_devastated=False,
                 is_illuminated=False, is_illusion=False, is_bleeding=False, is_vigilant=False,
                 is_protected=False, hp=10, purpose=False, act1_mana=3, act2_mana=4, act3_mana=3, level=1, in_game=True, flag=True, atk=0, type=0, txt1=None, txt2=None):
        super().__init__(is_poisoned, is_afraid, is_wet, is_burn, is_windy, is_devastated,
                 is_illuminated, is_illusion, is_bleeding, is_vigilant,
                 is_protected, hp, purpose, act1_mana, act2_mana, act3_mana, level, in_game, flag, atk, type, txt1 ,txt2)

        self.image = load_image('Cards/Card_7.png')
        self.txt1 = "1-е: Увеличение урона"
        self.txt2 = "2-е: Увеличение хп"

    def act1(self, MANA):
        '''на две выбранные карты ветренность 1/1'''
        
        return 'proteck'

    def act2(self, MANA):
        '''2 враж рандомные карты 2 атк и на одну из них ветренность 1/1'''
        
        return 'afraid'


class Nothing(Elemental):
    def __init__(self, is_poisoned=False, is_afraid=False,
                 is_wet=False, is_burn=False, is_windy=False, is_devastated=False,
                 is_illuminated=False, is_illusion=False, is_bleeding=False, is_vigilant=False,
                 is_protected=False, hp=10, purpose=False, act1_mana=1, act2_mana=12, act3_mana=3, level=1, in_game=True, flag=True, atk=0, type=0, txt1=None, txt2=None):
        super().__init__(is_poisoned, is_afraid, is_wet, is_burn, is_windy, is_devastated,
                 is_illuminated, is_illusion, is_bleeding, is_vigilant,
                 is_protected, hp, purpose, act1_mana, act2_mana, act3_mana, level, in_game, flag, atk, type, txt1, txt2)

        self.image = load_image('Cards/Card_13.png')
        self.txt1 = "1-е: Увеличение урона"
        self.txt2 = "2-е: Увеличение урона"
    
    def act1(self, MANA):
        '''Цель получает горение 1/1'''
        
        return 'proteck'


    def act2(self, MANA):
        '''выбранной карте атк + 3'''
        
        return 'shine'

    def act1(self, MANA):
        '''все эффекты -'''
        if MANA >= self.act1_mana and self.flag:
            MANA -= self.act1_mana
            self.purpose.flag = 0
            self.purpose.is_poisoned=False
            self.purpose.is_afraid=False
            self.purpose.is_wet=False
            self.purpose.is_burn=False
            self.purpose.is_windy=False
            self.purpose.is_devastated=False
            self.purpose.is_illuminated=False
            self.purpose.is_illusion=False
            self.purpose.is_bleeding=False
            self.purpose.is_vigilant=False
            self.purpose.is_protected=False

    def act2(self, MANA):
        '''цель сдохла'''
        MANA += 1
        return 'mana'


class Vampire(Card):
    def __init__(self, is_poisoned=False, is_afraid=False,
                 is_wet=False, is_burn=False, is_windy=False, is_devastated=False,
                 is_illuminated=False, is_illusion=False, is_bleeding=False, is_vigilant=False,
                 is_protected=False, hp=10, purpose=False, act1_mana=0, act2_mana=0, level=1, in_game=True, flag=True, atk=0, type=0, txt1=None, txt2=None):
        super().__init__(is_poisoned, is_afraid, is_wet, is_burn, is_windy, is_devastated,
                 is_illuminated, is_illusion, is_bleeding, is_vigilant,
                 is_protected, hp, purpose, act1_mana, act2_mana, in_game, flag, atk, type, txt1, txt2)


    def ataka(self, MANA):
        '''у каждой карты данного класса есть доп функция
                УЛУЧШЕНИЕ уровня карты(ур + 1)'''
        if MANA >= self.cost_upgrade and self.level < 3:
            pass


class Oboroten(Vampire):
    def __init__(self, is_poisoned=False, is_afraid=False,
                 is_wet=False, is_burn=False, is_windy=False, is_devastated=False,
                 is_illuminated=False, is_illusion=False, is_bleeding=False, is_vigilant=False,
                 is_protected=False, hp=10, purpose=False, act1_mana=4, act2_mana=3, level=1, in_game=True, flag=True, atk=0, type=0, txt1=None, txt2=None):
        super().__init__(is_poisoned, is_afraid, is_wet, is_burn, is_windy, is_devastated,
                 is_illuminated, is_illusion, is_bleeding, is_vigilant,
                 is_protected, hp, purpose, act1_mana, act2_mana, level, in_game, flag, atk, type, txt1, txt2)

        self.image = load_image('Cards/Card_6.png')
        self.txt1 = "1-е: Отравление карты"
        self.txt2 = "2-е: Удар по карте"

    def act1(self, MANA):
        '''все противнихи яд 1\1 -'''
        
        return 'poison'

    def act2(self, MANA):
        '''цель 2 урона х 2'''
        
        return 'bleeding'


class Red_duet(Vampire):
    def __init__(self, is_poisoned=False, is_afraid=False,
                 is_wet=False, is_burn=False, is_windy=False, is_devastated=False,
                 is_illuminated=False, is_illusion=False, is_bleeding=False, is_vigilant=False,
                 is_protected=False, hp=18, purpose=False, act1_mana=6, act2_mana=6, level=1, in_game=True, flag=True, atk=0, txt1=None, txt2=None):
        super().__init__(is_poisoned, is_afraid, is_wet, is_burn, is_windy, is_devastated,
                 is_illuminated, is_illusion, is_bleeding, is_vigilant,
                 is_protected, hp, purpose, act1_mana, act2_mana, level, in_game, flag, atk, txt1, txt2)

    def act1(self, MANA):
        '''все противнихи яд 1\1 -'''
        self.txt1 = "1-е: Отравление карты"
        return 'poison'
    
    def act2(self, MANA):
        '''цель 2 урона х 2'''
        self.txt2 = "2-е: Уменьшить урон карты"
        return 'vigilant'


class Bobik(Vampire):
    def __init__(self, is_poisoned=False, is_afraid=False,
                 is_wet=False, is_burn=False, is_windy=False, is_devastated=False,
                 is_illuminated=False, is_illusion=False, is_bleeding=False, is_vigilant=False,
                 is_protected=False, hp=10, purpose=False, act1_mana=2, act2_mana=5, level=1, in_game=True, flag=True, atk=0, txt1=None, txt2=None):
        super().__init__(is_poisoned, is_afraid, is_wet, is_burn, is_windy, is_devastated,
                 is_illuminated, is_illusion, is_bleeding, is_vigilant,
                 is_protected, hp, purpose, act1_mana, act2_mana, level, in_game, flag, atk, txt1, txt2)

    def act1(self, MANA):
        '''все противнихи яд 1\1 -'''
        self.txt1 = "1-е: Отравление карты"
        return 'poison'

    def act2(self, MANA):
        '''цель 2 урона х 2'''
        self.txt2 = "2-е: Уменьшить урон карты"
        return 'vigilant'


class Mishka_Narushka(Vampire):
    def __init__(self, is_poisoned=False, is_afraid=False,
                 is_wet=False, is_burn=False, is_windy=False, is_devastated=False,
                 is_illuminated=False, is_illusion=False, is_bleeding=False, is_vigilant=False,
                 is_protected=False, hp=10, purpose=False, act1_mana=0, act2_mana=1, level=1, in_game=True, flag=True, atk=0, txt1=None, txt2=None):
        super().__init__(is_poisoned, is_afraid, is_wet, is_burn, is_windy, is_devastated,
                 is_illuminated, is_illusion, is_bleeding, is_vigilant,
                 is_protected, hp, purpose, act1_mana, act2_mana, level, in_game, flag, atk, txt1, txt2)
        
        self.txt1 = "1-е: Отравление карты"
        self.txt2 = "2-е: Увеличение урон"

    def act1(self, MANA):
        '''все противнихи яд 1\1 -'''
        
        return 'poison'

    def act2(self, MANA):
        '''цель 2 урона х 2'''
        
        return 'proteck'


class Mutant(Vampire):
    def __init__(self, is_poisoned=False, is_afraid=False,
                 is_wet=False, is_burn=False, is_windy=False, is_devastated=False,
                 is_illuminated=False, is_illusion=False, is_bleeding=False, is_vigilant=False,
                 is_protected=False, hp=8, purpose=False, act1_mana=8, act2_mana=3, level=1, in_game=True, flag=True, atk=0, type=0, txt1=None, txt2=None):
        super().__init__(is_poisoned, is_afraid, is_wet, is_burn, is_windy, is_devastated,
                 is_illuminated, is_illusion, is_bleeding, is_vigilant,
                 is_protected, hp, purpose, act1_mana, act2_mana, level, in_game, flag, atk, type, txt1, txt2)

        self.image = load_image('Cards/Card_10.png')
        self.txt1 = "1-е: Отравление карты"
        self.txt2 = "2-е: Увеличение урон"

    def act1(self, MANA):
        '''все противнихи яд 1\1 -'''
        
        return 'poison'

    def act2(self, MANA):
        '''цель 2 урона х 2'''
        
        return 'proteck'


class True_Vamp(Vampire):
    def __init__(self, is_poisoned=False, is_afraid=False,
                 is_wet=False, is_burn=False, is_windy=False, is_devastated=False,
                 is_illuminated=False, is_illusion=False, is_bleeding=False, is_vigilant=False,
                 is_protected=False, hp=10, purpose=False, act1_mana=3, act2_mana=6, level=1, in_game=True, flag=True, atk=0, type=0, txt1=None, txt2=None):
        super().__init__(is_poisoned, is_afraid, is_wet, is_burn, is_windy, is_devastated,
                 is_illuminated, is_illusion, is_bleeding, is_vigilant,
                 is_protected, hp, purpose, act1_mana, act2_mana, level, in_game, flag, atk, type, txt1, txt2)

        self.image = load_image('Cards/Card_12.png')
        self.txt1 = "1-е: Увеличение урона"
        self.txt2 = "2-е: Удар по карте"

    def act1(self, MANA):
        '''все противнихи яд 1\1 -'''
        
        return 'shine'

    def act2(self, MANA):
        '''цель 2 урона х 2'''
        
        return 'bleeding'


class Suicide(Card):
    def __init__(self, is_poisoned=False, is_afraid=False,
                 is_wet=False, is_burn=False, is_windy=False, is_devastated=False,
                 is_illuminated=False, is_illusion=False, is_bleeding=False, is_vigilant=False,
                 is_protected=False, hp=10, purpose=False, act1_mana=0, act2_mana=0, level=1, in_game=True, flag=True, atk=0, type=0, txt1=None, txt2=None):
        super().__init__(is_poisoned, is_afraid, is_wet, is_burn, is_windy, is_devastated,
                 is_illuminated, is_illusion, is_bleeding, is_vigilant,
                 is_protected, hp, purpose, act1_mana, act2_mana, in_game, flag, atk, type, txt1, txt2)


class Stradauschii(Suicide):
    def __init__(self, is_poisoned=False, is_afraid=False,
                 is_wet=False, is_burn=False, is_windy=False, is_devastated=False,
                 is_illuminated=False, is_illusion=False, is_bleeding=False, is_vigilant=False,
                 is_protected=False, hp=10, purpose=False, act1_mana=2, act2_mana=2, level=1, in_game=True, flag=True, atk=0, type=0, txt1=None, txt2=None):
        super().__init__(is_poisoned, is_afraid, is_wet, is_burn, is_windy, is_devastated,
                 is_illuminated, is_illusion, is_bleeding, is_vigilant,
                 is_protected, hp, purpose, act1_mana, act2_mana, level, in_game, flag, atk, type, txt1, txt2)

        self.image = load_image('Cards/Card_2.png')
        self.txt1 = "1-е: Уменьшение урона"
        self.txt2 = "2-е: Защита карты"

    def act1(self, MANA):
        '''все противнихи яд 1\1 -'''
        
        return 'vigilant'

    def act2(self, MANA):
        '''цель 2 урона х 2'''
        
        return 'proteck'

    def death(self):
        self.purpose[0].hp += 2
        self.purpose[1].hp += 2


class Princess(Suicide):
    def __init__(self, is_poisoned=False, is_afraid=False,
                 is_wet=False, is_burn=False, is_windy=False, is_devastated=False,
                 is_illuminated=False, is_illusion=False, is_bleeding=False, is_vigilant=False,
                 is_protected=False, hp=10, purpose=False, act1_mana=4, act2_mana=0, level=1, in_game=True, flag=True, atk=0, txt1=None, txt2=None):
        super().__init__(is_poisoned, is_afraid, is_wet, is_burn, is_windy, is_devastated,
                 is_illuminated, is_illusion, is_bleeding, is_vigilant,
                 is_protected, hp, purpose, act1_mana, act2_mana, level, in_game, flag, atk, txt1, txt2)

    def act1(self, MANA):
        '''все противнихи яд 1\1 -'''
        MANA += 1
        return MANA

    def act2(self, MANA):
        '''цель 2 урона х 2'''
        MANA += 1
        return MANA

    def death(self):
        self.purpose[0].hp += 2
        self.purpose[1].hp += 2