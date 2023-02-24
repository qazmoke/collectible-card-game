import random


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
                 is_protected=False, hp=10, purpose=False, act1_mana=0, act2_mana=0, in_game=True, flag=True, atk=0, sup_atk=0):
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
        self.atk = atk

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
                 is_protected=False, hp=10, purpose=False, act1_mana=0, act2_mana=0, act3_mana=3, level=1, in_game=True, flag=True, atk=0):
        super().__init__(is_poisoned, is_afraid, is_wet, is_burn, is_windy, is_devastated,
                 is_illuminated, is_illusion, is_bleeding, is_vigilant,
                 is_protected, hp, purpose, act1_mana, act2_mana, in_game, flag, atk)
        self.cost_upgrade = act3_mana
        self.level = level

        def upgrade(self, MANA):
            '''у каждой карты данного класса есть доп функция
                 УЛУЧШЕНИЕ уровня карты(ур + 1)'''
            if MANA >= self.cost_upgrade and self.level < 3:
                MANA -= self.cost_upgrade
                self.level = self.level + 1


class Shadow(Elemental):
    def __init__(self, is_poisoned=False, is_afraid=False,
                 is_wet=False, is_burn=False, is_windy=False, is_devastated=False,
                 is_illuminated=False, is_illusion=False, is_bleeding=False, is_vigilant=False,
                 is_protected=False, hp=10, purpose=False, act1_mana=7, act2_mana=3, act3_mana=3, level=1, in_game=True, flag=True, atk=0):
        super().__init__(is_poisoned, is_afraid, is_wet, is_burn, is_windy, is_devastated,
                 is_illuminated, is_illusion, is_bleeding, is_vigilant,
                 is_protected, hp, purpose, act1_mana, act2_mana, act3_mana, level, in_game, flag, atk)

        def act1(self, MANA):
            '''Цель получает стан 1/2
               Все впажеские карты страх level/2'''
            if MANA >= self.act1_mana and self.flag and in_game == True:
                MANA -= self.act1_mana
                self.flag = 0
                for i in self.purpose:
                    d = self.level
                    if is_illuminated != False:
                        d = self.level - 1
                    i.is_afraid = (i.is_afraid[0] + d, 1)
                purpose[0].in_game = [False, 2]

        def act2(self, MANA):
            '''Все впажеские карты страх level/1(50% шанс)
               и 1 атк'''
            if MANA >= self.act2_mana and self.flag and in_game == True:
                MANA -= self.act2_mana
                self.flag = 0
                for i in self.purpose:
                    i.hp = i.hp - 1
                    f = random.randint(0, 1)
                    if f:
                        d = self.level
                        if self.is_illuminated != False:
                            d = self.level - 1
                        i.is_afraid = (i.is_afraid[0] + d, 1)

        def next_move(self):
            self.is_afraid = False


class Rodia(Elemental):
    def __init__(self, is_poisoned=False, is_afraid=False,
                 is_wet=(1, 10000), is_burn=False, is_windy=False, is_devastated=False,
                 is_illuminated=False, is_illusion=False, is_bleeding=False, is_vigilant=False,
                 is_protected=False, hp=10, purpose=False, act1_mana=4, act2_mana=5, act3_mana=3, level=1, in_game=True, flag=True, atk=0):
        super().__init__(is_poisoned, is_afraid, is_wet, is_burn, is_windy, is_devastated,
                 is_illuminated, is_illusion, is_bleeding, is_vigilant,
                 is_protected, hp, purpose, act1_mana, act2_mana, act3_mana, level, in_game, flag, atk)

        def act1(self, MANA):
            '''Цель получает 3 урона
               2 рандомные карты сырость'''
            if MANA >= self.act1_mana and self.flag and in_game == True:
                MANA -= self.act1_mana
                self.flag = 0
                vill = random.choices(self.purpose, k=2)
                for i in vill:
                    i.is_wet = (i.is_wet[0] + self.level, 1)
                self.purpose[0].hp = self.purpose[0].hp - 3

        def act2(self, MANA):
            '''Все впажеские карты сырость level/1
               и цели 2 HP + 2 HP если сырость '''
            if MANA >= self.act2_mana and self.flag and in_game == True:
                MANA -= self.act2_mana
                self.flag = 0
                for i in purpose[1:]:
                    i.is_wet = (i.is_wet[0] + self.level, 1)
                purpose[0].hp = purpose[0].hp + 2
                if purpose[0].is_wet != False:
                    purpose[0].hp = purpose[0].hp + 2


class Shiny(Elemental):
    def __init__(self, is_poisoned=False, is_afraid=False,
                 is_wet=False, is_burn=False, is_windy=False, is_devastated=False,
                 is_illuminated=False, is_illusion=False, is_bleeding=False, is_vigilant=False,
                 is_protected=False, hp=10, purpose=False, act1_mana=5, act2_mana=2, act3_mana=3, level=1, in_game=True, flag=True, atk=0):
        super().__init__(is_poisoned, is_afraid, is_wet, is_burn, is_windy, is_devastated,
                 is_illuminated, is_illusion, is_bleeding, is_vigilant,
                 is_protected, hp, purpose, act1_mana, act2_mana, act3_mana, level, in_game, flag)

        def act1(self, MANA):
            '''Цель получает свет ур/1 и 2 атк'''
            if MANA >= self.act1_mana and self.flag and in_game == True:
                MANA -= self.act1_mana
                self.flag = 0
                self.purpose[0].is_illuminated = (self.purpose[0].is_illuminated[0] + self.level, 1)
                self.purpose[0].hp = self.purpose[0].hp - 2

        def act2(self, MANA):
            '''Все впажеские карты 1 или 2 урона  и 50% шанс 1 урон каждой своей карье'''
            if MANA >= self.act2_mana and self.flag and in_game == True:
                MANA -= self.act2_mana
                self.flag = 0
                for i in purpose[:3]:
                    f = random.randint(1, 2)
                    i.hp = i.hp - f
                if random.randint(0, 1):
                    for i in purpose[3:]:
                        i.hp = i.hp - 1


class Oilus(Elemental):
    def __init__(self, is_poisoned=False, is_afraid=False,
                 is_wet=False, is_burn=(1, 1000000000), is_windy=False, is_devastated=False,
                 is_illuminated=False, is_illusion=False, is_bleeding=False, is_vigilant=False,
                 is_protected=False, hp=10, purpose=False, act1_mana=1, act2_mana=4, act3_mana=3, level=1, in_game=True, flag=True, atk=0):
        super().__init__(is_poisoned, is_afraid, is_wet, is_burn, is_windy, is_devastated,
                 is_illuminated, is_illusion, is_bleeding, is_vigilant,
                 is_protected, hp, purpose, act1_mana, act2_mana, act3_mana, level, in_game, flag, atk)

        def act1(self, MANA):
            '''Цель получает горение 1/1'''
            if MANA >= self.act1_mana and self.flag and in_game == True:
                MANA -= self.act1_mana
                self.flag = 0
                self.purpose[0].is_burn = (1, 1)

        def act2(self, MANA):
            '''выбранной карте атк + 3'''
            if MANA >= self.act2_mana and self.flag and in_game == True:
                MANA -= self.act2_mana
                self.flag = 0
                self.purpose[0].atk += 3


class Silf(Elemental):
    def __init__(self, is_poisoned=False, is_afraid=False,
                 is_wet=False, is_burn=False, is_windy=False, is_devastated=False,
                 is_illuminated=False, is_illusion=False, is_bleeding=False, is_vigilant=False,
                 is_protected=False, hp=10, purpose=False, act1_mana=3, act2_mana=4, act3_mana=3, level=1, in_game=True, flag=True, atk=0):
        super().__init__(is_poisoned, is_afraid, is_wet, is_burn, is_windy, is_devastated,
                 is_illuminated, is_illusion, is_bleeding, is_vigilant,
                 is_protected, hp, purpose, act1_mana, act2_mana, act3_mana, level, in_game, flag, atk)

        def act1(self, MANA):
            '''на две выбранные карты ветренность 1/1'''
            if MANA >= self.act1_mana and self.flag and in_game == True:
                MANA -= self.act1_mana
                self.flag = 0
                for i in self.purpose:
                    i.is_windy = (1, 1)

        def act2(self, MANA):
            '''2 враж рандомные карты 2 атк и на одну из них ветренность 1/1'''
            if MANA >= self.act2_mana and self.flag and in_game == True:
                MANA -= self.act2_mana
                self.flag = 0
                for i in self.purpose:
                    i.hp -= 2
                self.purpose[random.randint(0,1)].is_windy = (1, 1)


class Nothing(Elemental):
    def __init__(self, is_poisoned=False, is_afraid=False,
                 is_wet=False, is_burn=False, is_windy=False, is_devastated=False,
                 is_illuminated=False, is_illusion=False, is_bleeding=False, is_vigilant=False,
                 is_protected=False, hp=10, purpose=False, act1_mana=1, act2_mana=12, act3_mana=3, level=1, in_game=True, flag=True, atk=0):
        super().__init__(is_poisoned, is_afraid, is_wet, is_burn, is_windy, is_devastated,
                 is_illuminated, is_illusion, is_bleeding, is_vigilant,
                 is_protected, hp, purpose, act1_mana, act2_mana, act3_mana, level, in_game, flag, atk)

        def act1(self, MANA):
            '''все эффекты -'''
            if MANA >= self.act1_mana and self.flag and in_game == True:
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
            if MANA >= self.act2_mana and self.flag and in_game == True:
                MANA -= self.act2_mana
                self.flag = 0
                self.purpose.hp = 0
                self.purpose.in_game = False


class Vampire(Card):
    def __init__(self, is_poisoned=False, is_afraid=False,
                 is_wet=False, is_burn=False, is_windy=False, is_devastated=False,
                 is_illuminated=False, is_illusion=False, is_bleeding=False, is_vigilant=False,
                 is_protected=False, hp=10, purpose=False, act1_mana=0, act2_mana=0, act3_mana=3, level=1, in_game=True, flag=True, atk=0):
        super().__init__(is_poisoned, is_afraid, is_wet, is_burn, is_windy, is_devastated,
                 is_illuminated, is_illusion, is_bleeding, is_vigilant,
                 is_protected, hp, purpose, act1_mana, act2_mana, in_game, flag, atk)


        def ataka(self, MANA, enem, lvl):
            '''у каждой карты данного класса есть доп функция
                 УЛУЧШЕНИЕ уровня карты(ур + 1)'''
            if MANA >= self.cost_upgrade and self.level < 3:
                MANA -= self.cost_upgrade
                enem.hp -= lvl
                self.hp += lvl // 2
                if not random.randint(0, 5):
                    enem.is_poisoned = (enem.is_poisoned[0] + 1, enem.is_poisoned[1] + 1)


class Oboroten(Vampire):
    def __init__(self, is_poisoned=False, is_afraid=False,
                 is_wet=False, is_burn=False, is_windy=False, is_devastated=False,
                 is_illuminated=False, is_illusion=False, is_bleeding=False, is_vigilant=False,
                 is_protected=False, hp=10, purpose=False, act1_mana=4, act2_mana=3, level=1, in_game=True, flag=True, atk=0):
        super().__init__(is_poisoned, is_afraid, is_wet, is_burn, is_windy, is_devastated,
                 is_illuminated, is_illusion, is_bleeding, is_vigilant,
                 is_protected, hp, purpose, act1_mana, act2_mana, level, in_game, flag, atk)

        def act1(self, MANA):
            '''все противнихи яд 1\1 -'''
            if MANA >= self.act1_mana and self.flag and in_game == True:
                MANA -= self.act1_mana
                self.flag = 0
                for i in self.purpose:
                    i.is_poisoned = (i.is_poisoned[0] + 1, i.is_poisoned[1] + 1)

        def act2(self, MANA):
            '''цель 2 урона х 2'''
            if MANA >= self.act2_mana and self.flag and in_game == True:
                MANA -= self.act2_mana
                self.flag = 0
                self.ataka(MANA, self.purpose, 2)
                self.ataka(MANA, self.purpose, 2)


class Red_duet(Vampire):
    def __init__(self, is_poisoned=False, is_afraid=False,
                 is_wet=False, is_burn=False, is_windy=False, is_devastated=False,
                 is_illuminated=False, is_illusion=False, is_bleeding=False, is_vigilant=False,
                 is_protected=False, hp=18, purpose=False, act1_mana=6, act2_mana=6, level=1, in_game=True, flag=True, atk=0):
        super().__init__(is_poisoned, is_afraid, is_wet, is_burn, is_windy, is_devastated,
                 is_illuminated, is_illusion, is_bleeding, is_vigilant,
                 is_protected, hp, purpose, act1_mana, act2_mana, level, in_game, flag, atk)

        def act1(self, MANA):
            '''все противнихи яд 1\1 -'''
            if MANA >= self.act1_mana and self.flag and in_game == True:
                MANA -= self.act1_mana
                self.flag = 0
                self.purpose[0].is_illusion = (self.purpose[0].is_illusion[0] + 2, self.purpose[0].is_illusion[1] + 2)
                self.ataka(MANA, self.purpose[1], 2)
                self.ataka(MANA, self.purpose[2], 2)

        def act2(self, MANA):
            '''цель 2 урона х 2'''
            if MANA >= self.act2_mana and self.flag and in_game == True:
                MANA -= self.act2_mana
                self.flag = 0
                self.ataka(MANA, self.purpose[0], 3)
                self.ataka(MANA, self.purpose[1], 1)
                self.ataka(MANA, self.purpose[2], 1)
                self.purpose[0].is_illusion = (self.purpose[0].is_illusion[0] + 1, self.purpose[0].is_illusion[1] + 1)
                self.purpose[1].is_illusion = (self.purpose[0].is_illusion[0] + 1, self.purpose[0].is_illusion[1] + 1)
                self.purpose[2].is_illusion = (self.purpose[0].is_illusion[0] + 1, self.purpose[0].is_illusion[1] + 1)


class Bobik(Vampire):
    def __init__(self, is_poisoned=False, is_afraid=False,
                 is_wet=False, is_burn=False, is_windy=False, is_devastated=False,
                 is_illuminated=False, is_illusion=False, is_bleeding=False, is_vigilant=False,
                 is_protected=False, hp=10, purpose=False, act1_mana=2, act2_mana=5, level=1, in_game=True, flag=True, atk=0):
        super().__init__(is_poisoned, is_afraid, is_wet, is_burn, is_windy, is_devastated,
                 is_illuminated, is_illusion, is_bleeding, is_vigilant,
                 is_protected, hp, purpose, act1_mana, act2_mana, level, in_game, flag, atk)

        def act1(self, MANA):
            '''все противнихи яд 1\1 -'''
            if MANA >= self.act1_mana and self.flag and in_game == True:
                MANA -= self.act1_mana
                self.flag = 0
                self.ataka(MANA, self.purpose, 2)
                self.purpose.is_bleeding = (self.purpose.is_bleeding[0] + 1, self.purpose.is_bleeding[0] + 1)

        def act2(self, MANA):
            '''цель 2 урона х 2'''
            if MANA >= self.act2_mana and self.flag and in_game == True:
                MANA -= self.act2_mana
                self.flag = 0
                self.purpose.is_vigilant = self.purpose.is_vigilant + 2


class Mishka_Narushka(Vampire):
    def __init__(self, is_poisoned=False, is_afraid=False,
                 is_wet=False, is_burn=False, is_windy=False, is_devastated=False,
                 is_illuminated=False, is_illusion=False, is_bleeding=False, is_vigilant=False,
                 is_protected=False, hp=10, purpose=False, act1_mana=0, act2_mana=1, level=1, in_game=True, flag=True, atk=0):
        super().__init__(is_poisoned, is_afraid, is_wet, is_burn, is_windy, is_devastated,
                 is_illuminated, is_illusion, is_bleeding, is_vigilant,
                 is_protected, hp, purpose, act1_mana, act2_mana, level, in_game, flag, atk)

        def act1(self, MANA):
            '''все противнихи яд 1\1 -'''
            if self.flag and in_game == True:
                MANA += 2
                self.flag = 0
                self.hp -= 1
                if random.randint(0, 3):
                    self.is_blleding = (self.is_blleding[0] + 1, self.is_blleding[1] + 1)

        def act2(self, MANA):
            '''цель 2 урона х 2'''
            if MANA >= self.act2_mana and self.flag and in_game == True:
                MANA -= self.act2_mana
                self.flag = 0
                self.ataka(MANA, self.purpose, 1)
                if not random.randint(0, 2):
                    MANA += 1


class Mutant(Vampire):
    def __init__(self, is_poisoned=False, is_afraid=False,
                 is_wet=False, is_burn=False, is_windy=False, is_devastated=False,
                 is_illuminated=False, is_illusion=False, is_bleeding=False, is_vigilant=False,
                 is_protected=False, hp=8, purpose=False, act1_mana=8, act2_mana=3, level=1, in_game=True, flag=True, atk=0):
        super().__init__(is_poisoned, is_afraid, is_wet, is_burn, is_windy, is_devastated,
                 is_illuminated, is_illusion, is_bleeding, is_vigilant,
                 is_protected, hp, purpose, act1_mana, act2_mana, level, in_game, flag, atk)

        def act1(self, MANA):
            '''все противнихи яд 1\1 -'''
            if MANA >= self.act1_mana and self.flag and in_game == True:
                MANA -= self.act1_mana
                self.flag = 0
                for i in self.purpose:
                    i.hp -= 2

        def act2(self, MANA):
            '''цель 2 урона х 2'''
            if self.flag and in_game == True:
                self.hp -= self.act2_mana
                self.flag = 0
                self.purpose.hp -= 4
                self.purpose.is_bleeding = (self.purpose.is_bleeding[0] + 2, self.purpose.is_bleeding[1] + 2)


class True_Vamp(Vampire):
    def __init__(self, is_poisoned=False, is_afraid=False,
                 is_wet=False, is_burn=False, is_windy=False, is_devastated=False,
                 is_illuminated=False, is_illusion=False, is_bleeding=False, is_vigilant=False,
                 is_protected=False, hp=10, purpose=False, act1_mana=3, act2_mana=6, level=1, in_game=True, flag=True, atk=0):
        super().__init__(is_poisoned, is_afraid, is_wet, is_burn, is_windy, is_devastated,
                 is_illuminated, is_illusion, is_bleeding, is_vigilant,
                 is_protected, hp, purpose, act1_mana, act2_mana, level, in_game, flag, atk)

        def act1(self, MANA):
            '''все противнихи яд 1\1 -'''
            if self.flag and in_game == True:
                MANA += 2
                self.flag = 0
                self.hp += 2
                self.purpose.hp -= 2
                self.purpose.atk += 1

        def act2(self, MANA):
            '''цель 2 урона х 2'''
            if self.flag and in_game == True:
                self.hp -= self.act2_mana
                self.flag = 0
                for i in self.purpose:
                    i.act1_mana += 1
                    i.act2_mana += 1
                self.purpose[0].hp -= 2


class Suicide(Card):
    def __init__(self, is_poisoned=False, is_afraid=False,
                 is_wet=False, is_burn=False, is_windy=False, is_devastated=False,
                 is_illuminated=False, is_illusion=False, is_bleeding=False, is_vigilant=False,
                 is_protected=False, hp=10, purpose=False, act1_mana=0, act2_mana=0, act3_mana=3, level=1, in_game=True, flag=True, atk=0):
        super().__init__(is_poisoned, is_afraid, is_wet, is_burn, is_windy, is_devastated,
                 is_illuminated, is_illusion, is_bleeding, is_vigilant,
                 is_protected, hp, purpose, act1_mana, act2_mana, in_game, flag, atk)


class Stradauschii(Suicide):
    def __init__(self, is_poisoned=False, is_afraid=False,
                 is_wet=False, is_burn=False, is_windy=False, is_devastated=False,
                 is_illuminated=False, is_illusion=False, is_bleeding=False, is_vigilant=False,
                 is_protected=False, hp=10, purpose=False, act1_mana=0, act2_mana=0, level=1, in_game=True, flag=True, atk=0):
        super().__init__(is_poisoned, is_afraid, is_wet, is_burn, is_windy, is_devastated,
                 is_illuminated, is_illusion, is_bleeding, is_vigilant,
                 is_protected, hp, purpose, act1_mana, act2_mana, level, in_game, flag, atk)

        def act1(self, MANA):
            '''все противнихи яд 1\1 -'''
            if MANA >= self.act1_mana and self.flag and in_game == True:
                self.flag = 0
                self.flag = 0
                self.hp -= 2
                self.purpose[0].hp += 1
                self.purpose[1].hp += 1

        def act2(self, MANA):
            '''цель 2 урона х 2'''
            if MANA >= self.act1_mana and self.flag and in_game == True:
                self.flag = 0
                self.hp -= 2
                self.purpose.hp -= 3

        def death(self):
            self.purpose[0].hp += 2
            self.purpose[1].hp += 2


class Princess(Suicide):
    def __init__(self, is_poisoned=False, is_afraid=False,
                 is_wet=False, is_burn=False, is_windy=False, is_devastated=False,
                 is_illuminated=False, is_illusion=False, is_bleeding=False, is_vigilant=False,
                 is_protected=False, hp=10, purpose=False, act1_mana=4, act2_mana=0, level=1, in_game=True, flag=True, atk=0):
        super().__init__(is_poisoned, is_afraid, is_wet, is_burn, is_windy, is_devastated,
                 is_illuminated, is_illusion, is_bleeding, is_vigilant,
                 is_protected, hp, purpose, act1_mana, act2_mana, level, in_game, flag, atk)

        def act1(self, MANA):
            '''все противнихи яд 1\1 -'''
            if MANA >= self.act1_mana and self.flag and in_game == True:
                self.flag = 0
                MANA -= self.act1_mana
                for i in self.purpose:
                    i.hp -= 1

        def act2(self, MANA):
            '''цель 2 урона х 2'''
            if MANA >= self.act1_mana and self.flag and in_game == True:
                self.flag = 0
                self.is_poisoned = (self.is_poisoned[0] + 2, self.is_poisoned[1] + 2)

        def death(self):
            self.purpose[0].hp += 2
            self.purpose[1].hp += 2

class Anciant_Hero(Suicide):
    def __init__(self, is_poisoned=False, is_afraid=False,
                 is_wet=False, is_burn=False, is_windy=False, is_devastated=False,
                 is_illuminated=False, is_illusion=False, is_bleeding=False, is_vigilant=False,
                 is_protected=False, hp=9, purpose=False, act1_mana=7, act2_mana=2, level=1, in_game=True, flag=True, atk=0):
        super().__init__(is_poisoned, is_afraid, is_wet, is_burn, is_windy, is_devastated,
                 is_illuminated, is_illusion, is_bleeding, is_vigilant,
                 is_protected, hp, purpose, act1_mana, act2_mana, level, in_game, flag, atk)

        def act1(self, MANA):
            '''все противнихи яд 1\1 -'''
            if MANA >= self.act1_mana and self.flag and in_game == True:
                MANA -= self.act1_mana
                self.flag = 0
                self.purpose.atk -= 2

        def act2(self, MANA):
            '''цель 2 урона х 2'''
            if MANA >= self.act1_mana and self.flag and in_game == True:
                self.flag = 0
                MANA -= self.act1_mana
                self.purpose.hp -= (1 + random.randint(0, 1) * 2)

        def death(self, MANA):
            MANA += 5


class Naemnik(Suicide):
    def __init__(self, is_poisoned=False, is_afraid=False,
                 is_wet=False, is_burn=False, is_windy=False, is_devastated=False,
                 is_illuminated=False, is_illusion=False, is_bleeding=False, is_vigilant=False,
                 is_protected=False, hp=6, purpose=False, act1_mana=4, act2_mana=0, level=1, in_game=True, flag=True, atk=0):
        super().__init__(is_poisoned, is_afraid, is_wet, is_burn, is_windy, is_devastated,
                 is_illuminated, is_illusion, is_bleeding, is_vigilant,
                 is_protected, hp, purpose, act1_mana, act2_mana, level, in_game, flag, atk)

        def act1(self, MANA):
            '''все противнихи яд 1\1 -'''
            if MANA >= self.act1_mana and self.flag and in_game == True:
                self.flag = 0
                MANA -= self.act1_mana
                for i in self.purpose:
                    i.hp -= 1

        def act2(self, MANA):
            '''цель 2 урона х 2'''
            if MANA >= self.act1_mana and self.flag and in_game == True:
                self.flag = 0
                self.hp -= 2
                self.atk -= 2
                MANA += 1
                self.purpose.is_afraid = (self.purpose.is_afraid + 1, self.purpose.is_afraid + 1)

        def death(self, cards):
            for i in cards:
                i.atk -= 1

class Mermaind(Suicide):
    def __init__(self, is_poisoned=False, is_afraid=False,
                 is_wet=False, is_burn=False, is_windy=False, is_devastated=False,
                 is_illuminated=False, is_illusion=False, is_bleeding=False, is_vigilant=False,
                 is_protected=False, hp=7, purpose=False, act1_mana=2, act2_mana=0, level=1, in_game=True, flag=True, atk=0):
        super().__init__(is_poisoned, is_afraid, is_wet, is_burn, is_windy, is_devastated,
                 is_illuminated, is_illusion, is_bleeding, is_vigilant,
                 is_protected, hp, purpose, act1_mana, act2_mana, level, in_game, flag, atk)

        def act1(self, MANA):
            '''все противнихи яд 1\1 -'''
            if MANA >= self.act1_mana and self.flag and in_game == True:
                self.flag = 0
                self.hp -= 2
                MANA -= act1_mana
                self.purpose.is_protected += (self.purpose.is_protected[0] + 1, self.purpose.is_protected[1] + 2)

        def act2(self, MANA):
            '''цель 2 урона х 2'''
            if MANA >= self.act1_mana and self.flag and in_game == True:
                self.flag = 0
                MANA -= self.act2_mana
                self.is_protected = (self.is_protected[0] + 1, self.is_protected[1] + 1)
                for i in self.purpose[:2]:
                    i.is_protected = (i.is_protected[0] + 1, i.is_protected[1] + 1)
                for i in self.purpose[2:]:
                    i.is_wet = (i.is_protected[0] + 1, i.is_protected[1] + 1)

        def death(self):
            self.purpose.is_wet = (self.purpose.is_wet[0] + 1, 1000000000000000)


class Black_Death(Suicide):
    def __init__(self, is_poisoned=False, is_afraid=False,
                 is_wet=False, is_burn=False, is_windy=False, is_devastated=False,
                 is_illuminated=False, is_illusion=False, is_bleeding=False, is_vigilant=False,
                 is_protected=False, hp=8, purpose=False, act1_mana=3, act2_mana=3, level=1, in_game=True, flag=True, atk=0):
        super().__init__(is_poisoned, is_afraid, is_wet, is_burn, is_windy, is_devastated,
                 is_illuminated, is_illusion, is_bleeding, is_vigilant,
                 is_protected, hp, purpose, act1_mana, act2_mana, level, in_game, flag, atk)

        def act1(self, MANA):
            '''все противнихи яд 1\1 -'''
            if MANA >= self.act1_mana and self.flag and in_game == True:
                self.flag = 0
                MANA -= self.act1_mana
                self.purpose.is_burn = (self.purpose.is_burn[0] + 2, self.purpose.is_burn[1] + 1)
                self.purpose.hp -= 1

        def act2(self, MANA):
            '''цель 2 урона х 2'''
            if MANA >= self.act1_mana and self.flag and in_game == True:
                self.flag = 0
                MANA -= self.act2_mana
                for i in self.purpose:
                    i.is_poisoned = (i.is_poisoned[0] + 1, i.is_poisoned[1] + 1)

        def death(self):
            for i in self.purpose:
                i.is_poisoned = (i.is_poisoned[0] + 2, i.is_poisoned[1] + 2)
                i.is_burn = (i.is_burn[0] + 1, i.is_burn[1] + 1)

class Undead(Card):
    def __init__(self, is_poisoned=False, is_afraid=False,
                 is_wet=False, is_burn=False, is_windy=False, is_devastated=False,
                 is_illuminated=False, is_illusion=False, is_bleeding=False, is_vigilant=False,
                 is_protected=False, hp=13, purpose=False, act1_mana=0, act2_mana=0, act3_mana=3, level=1, in_game=True, flag=True, atk=0):
        super().__init__(is_poisoned, is_afraid, is_wet, is_burn, is_windy, is_devastated,
                 is_illuminated, is_illusion, is_bleeding, is_vigilant,
                 is_protected, hp, purpose, act1_mana, act2_mana, in_game, flag, atk)


class Anciant_Evil(Undead):
    def __init__(self, is_poisoned=False, is_afraid=False,
                 is_wet=False, is_burn=False, is_windy=False, is_devastated=False,
                 is_illuminated=False, is_illusion=False, is_bleeding=False, is_vigilant=False,
                 is_protected=False, hp=12, purpose=False, act1_mana=7, act2_mana=6, level=1, in_game=True, flag=True, atk=0):
        super().__init__(is_poisoned, is_afraid, is_wet, is_burn, is_windy, is_devastated,
                 is_illuminated, is_illusion, is_bleeding, is_vigilant,
                 is_protected, hp, purpose, act1_mana, act2_mana, level, in_game, flag, atk)

        def act1(self, MANA):
            '''все противнихи яд 1\1 -'''
            if MANA >= self.act1_mana and self.flag and in_game == True:
                self.flag = 0
                MANA -= act1_mana
                for i in self.purpose:
                    i.hp -= 3
                    i.is_afraid = (i.is_afraid[0] + 1, i.is_afraid[1] + 1)


        def act2(self, MANA):
            '''цель 2 урона х 2'''
            if MANA >= self.act1_mana and self.flag and in_game == True:
                MANA -= act2_mana
                self.flag = 0
                for i in self.purpose:
                    i.is_afraid = (i.is_afraid[0] + 2, i.is_afraid[1] + 2)
                    i.is_burn = (i.is_burn[0] + 2, i.is_burn[1] + 1)

        def voscresnut(self):
            if self.purpose[0] <= 0 and self.purpose[1] <= 0 and self.purpose[2] <= 0:
                self.hp = 6
                self.purpose[3].atk = 0.2
                self.purpose[4].atk = 0.2
                self.purpose[5].atk = 0.2



class Necromanth(Undead):
    def __init__(self, is_poisoned=False, is_afraid=False,
                 is_wet=False, is_burn=False, is_windy=False, is_devastated=False,
                 is_illuminated=False, is_illusion=False, is_bleeding=False, is_vigilant=False,
                 is_protected=False, hp=12, purpose=False, act1_mana=4, act2_mana=4, level=1, in_game=True, flag=True, atk=0):
        super().__init__(is_poisoned, is_afraid, is_wet, is_burn, is_windy, is_devastated,
                 is_illuminated, is_illusion, is_bleeding, is_vigilant,
                 is_protected, hp, purpose, act1_mana, act2_mana, level, in_game, flag, atk)

        def act1(self, MANA):
            '''все противнихи яд 1\1 -'''
            if MANA >= self.act1_mana and self.flag and in_game == True:
                self.flag = 0
                MANA -= act1_mana
                for i in self.purpose:
                    i.hp -= 3
                    i.is_illuminated = (i.is_illuminated[0] + 2, i.is_illuminated[1] + 2)


        def act2(self, MANA):
            '''цель 2 урона х 2'''
            if MANA >= self.act1_mana and self.flag and in_game == True:
                MANA -= act2_mana
                self.flag = 0
                for i in self.purpose:
                    i.hp -= 1

        def voscresnut(self):
            self.purpose.in_game = False


class Pudg(Undead):
    def __init__(self, is_poisoned=False, is_afraid=False,
                 is_wet=False, is_burn=False, is_windy=False, is_devastated=False,
                 is_illuminated=False, is_illusion=False, is_bleeding=False, is_vigilant=False,
                 is_protected=False, hp=20, purpose=False, act1_mana=4, act2_mana=0, level=1, in_game=True, flag=True, atk=0):
        super().__init__(is_poisoned, is_afraid, is_wet, is_burn, is_windy, is_devastated,
                 is_illuminated, is_illusion, is_bleeding, is_vigilant,
                 is_protected, hp, purpose, act1_mana, act2_mana, level, in_game, flag, atk)

        def act1(self, MANA):
            '''все противнихи яд 1\1 -'''
            if MANA >= self.act1_mana and self.flag and in_game == True:
                MANA -= self.act1_mana
                self.flag = 0
                self.purpose.is_protected = (self.purpose.is_protected[0] + 3, self.purpose.is_protected[1] + 2)

        def act2(self, MANA):
            '''цель 2 урона х 2'''
            if MANA >= self.act1_mana and self.flag and in_game == True:
                self.flag = 0
                self.hp -= 7
                for i in self.purpose:
                    i.is_protected = (i.purpose.is_protected[0] + 3, i.purpose.is_protected[1] + 1000000)

        def voscrestnut(self, MANA):
            self.purpose.hp -= 5


class Naemnik(Suicide):
    def __init__(self, is_poisoned=False, is_afraid=False,
                 is_wet=False, is_burn=False, is_windy=False, is_devastated=False,
                 is_illuminated=False, is_illusion=False, is_bleeding=False, is_vigilant=False,
                 is_protected=False, hp=6, purpose=False, act1_mana=4, act2_mana=0, level=1, in_game=True, flag=True, atk=0):
        super().__init__(is_poisoned, is_afraid, is_wet, is_burn, is_windy, is_devastated,
                 is_illuminated, is_illusion, is_bleeding, is_vigilant,
                 is_protected, hp, purpose, act1_mana, act2_mana, level, in_game, flag, atk)

        def act1(self, MANA):
            '''все противнихи яд 1\1 -'''
            if MANA >= self.act1_mana and self.flag and in_game == True:
                self.flag = 0
                MANA -= self.act1_mana
                for i in self.purpose:
                    i.hp -= 1

        def act2(self, MANA):
            '''цель 2 урона х 2'''
            if MANA >= self.act1_mana and self.flag and in_game == True:
                self.flag = 0
                self.hp -= 2
                self.atk -= 2
                MANA += 1
                self.purpose.is_afraid = (self.purpose.is_afraid + 1, self.purpose.is_afraid + 1)

        def death(self, cards):
            for i in cards:
                i.atk -= 1

class Mermaind(Suicide):
    def __init__(self, is_poisoned=False, is_afraid=False,
                 is_wet=False, is_burn=False, is_windy=False, is_devastated=False,
                 is_illuminated=False, is_illusion=False, is_bleeding=False, is_vigilant=False,
                 is_protected=False, hp=7, purpose=False, act1_mana=2, act2_mana=0, level=1, in_game=True, flag=True, atk=0):
        super().__init__(is_poisoned, is_afraid, is_wet, is_burn, is_windy, is_devastated,
                 is_illuminated, is_illusion, is_bleeding, is_vigilant,
                 is_protected, hp, purpose, act1_mana, act2_mana, level, in_game, flag, atk)

        def act1(self, MANA):
            '''все противнихи яд 1\1 -'''
            if MANA >= self.act1_mana and self.flag and in_game == True:
                self.flag = 0
                self.hp -= 2
                MANA -= act1_mana
                self.purpose.is_protected += (self.purpose.is_protected[0] + 1, self.purpose.is_protected[1] + 2)

        def act2(self, MANA):
            '''цель 2 урона х 2'''
            if MANA >= self.act1_mana and self.flag and in_game == True:
                self.flag = 0
                MANA -= self.act2_mana
                self.is_protected = (self.is_protected[0] + 1, self.is_protected[1] + 1)
                for i in self.purpose[:2]:
                    i.is_protected = (i.is_protected[0] + 1, i.is_protected[1] + 1)
                for i in self.purpose[2:]:
                    i.is_wet = (i.is_protected[0] + 1, i.is_protected[1] + 1)

        def death(self):
            self.purpose.is_wet = (self.purpose.is_wet[0] + 1, 1000000000000000)


class Black_Death(Suicide):
    def __init__(self, is_poisoned=False, is_afraid=False,
                 is_wet=False, is_burn=False, is_windy=False, is_devastated=False,
                 is_illuminated=False, is_illusion=False, is_bleeding=False, is_vigilant=False,
                 is_protected=False, hp=8, purpose=False, act1_mana=3, act2_mana=3, level=1, in_game=True, flag=True, atk=0):
        super().__init__(is_poisoned, is_afraid, is_wet, is_burn, is_windy, is_devastated,
                 is_illuminated, is_illusion, is_bleeding, is_vigilant,
                 is_protected, hp, purpose, act1_mana, act2_mana, level, in_game, flag, atk)

        def act1(self, MANA):
            '''все противнихи яд 1\1 -'''
            if MANA >= self.act1_mana and self.flag and in_game == True:
                self.flag = 0
                MANA -= self.act1_mana
                self.purpose.is_burn = (self.purpose.is_burn[0] + 2, self.purpose.is_burn[1] + 1)
                self.purpose.hp -= 1

        def act2(self, MANA):
            '''цель 2 урона х 2'''
            if MANA >= self.act1_mana and self.flag and in_game == True:
                self.flag = 0
                MANA -= self.act2_mana
                for i in self.purpose:
                    i.is_poisoned = (i.is_poisoned[0] + 1, i.is_poisoned[1] + 1)

        def death(self):
            for i in self.purpose:
                i.is_poisoned = (i.is_poisoned[0] + 2, i.is_poisoned[1] + 2)
                i.is_burn = (i.is_burn[0] + 1, i.is_burn[1] + 1)







