import pygame, sqlite3, sys, os
from random import randint
from EnterMenu import user
import Cards_E

# Screen
pygame.init()
w, h = 950, 750
size = width, height = w, h
screen = pygame.display.set_mode(size)

player_hp = 0
board = ''

# Sprite groups
all_sprites = pygame.sprite.Group()
card_sprites = pygame.sprite.Group()
buttons_sprite = pygame.sprite.Group()
hp_sprites = pygame.sprite.Group()
mana_sprites = pygame.sprite.Group()

# Cards
deck = [Cards_E.Shiny(atk=2, hp=5, type=9), Cards_E.Mutant(atk=3, type=10), Cards_E.Nothing(atk=3, type=13), Cards_E.Oboroten(atk=4, type=6), Cards_E.True_Vamp(atk=4, type=12),
Cards_E.Shadow(atk=1, type=1), Cards_E.Stradauschii(atk=6, type=2), Cards_E.Silf(atk=7, type=7), Cards_E.Oilus(atk=2, type=8), Cards_E.Rodia(atk=8, type=11)]


# Function to close a window
def terminate():
    pygame.quit()
    sys.exit()


# Load Image
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


# Function (animation of closing the window)
def transparency():
    s = pygame.Surface((1000,750))
    s.set_alpha(128)
    s.fill((20, 20, 20))
    screen.blit(s, (0,0))
    pygame.display.flip()


class Button(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, num, group):
        super().__init__(group)
        
        if num == 1:
            self.image = load_image('back_btn.png')
        if num == 2:
            self.image = load_image('button_step.png')
        if num == 3:
            self.image = load_image('Button_clasik.png', -1)
        if num == 4:
            self.image = load_image('Button_fast.png', -1)

        # Number of button and its activity
        self.num = num
        self.action = False

        # Set position
        self.rect = self.image.get_rect().move(pos_x, pos_y)
        self.rect.x = pos_x
        self.rect.y = pos_y
    
    def update(self, *args):
        # Collide button and mouse
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and \
                self.rect.collidepoint(args[0].pos):
            
            # Changing Button image
            if self.num == 1:
                self.image = load_image('back_btn_2.png')
            if self.num == 2:
                self.image = load_image('button_step_2.png')
            if self.num == 3:
                self.image = load_image('Button_clasik_2.png', -1)
            if self.num == 4:
                self.image = load_image('Button_fast_2.png', -1)

            self.action = True


class Card(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, player, id_player, id, card):
        super().__init__(card_sprites, all_sprites)

        if id_player == 1:
            self.image = card.image
        else:
            self.image = load_image('card.jpg', -1)
            self.image = pygame.transform.rotate(self.image, 180)

        # Set position
        self.rect = self.image.get_rect().move(pos_x, pos_y)
        self.rect.x = pos_x
        self.rect.y = pos_y

        # Characteristic
        self.player = player
        self.typeCard = card
        self.played = False
        self.coast = card.act1_mana
        self.id = id

    def collide(self, *args):
        # Collide button and mouse
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and \
                self.rect.collidepoint(args[0].pos):
            
            return True

    def update(self, *args):
        self.rect.x = args[0]
        self.rect.y = args[1]

    def image_update(self):
        pass
        # self.image = load_image('card_played.png', -1)

    def die(self):
        self.kill()

    def hp_show(self):
        font = pygame.font.Font(None, 40)
        screen.blit(font.render(str(self.typeCard.hp), 1, pygame.Color('GreenYellow')), (self.rect.x + 10, self.rect.y + 140))

    def atk_show(self):
        font = pygame.font.Font(None, 40)
        screen.blit(font.render(str(self.typeCard.atk), 1, pygame.Color('red')), (self.rect.x + 45, self.rect.y + 140))

    def mana_show(self):
        font = pygame.font.Font(None, 40)
        screen.blit(font.render(str(self.coast), 1, pygame.Color('DeepSkyBlue')), (self.rect.x + 80, self.rect.y + 140))


class Field:
    def __init__(self, point_1, point_2, color, player):
        self.rect = pygame.Rect(point_1, point_2)
        # Characteristic
        self.x = point_1[0]
        self.y = point_1[-1]
        self.color = color
        self.activate = False
        self.player = player

    def collide(self, *args):
        # Collide button and mouse
        if args and args[0].type == pygame.MOUSEBUTTONUP and \
                self.rect.collidepoint(args[0].pos):
            
            return True


class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, x, y):
        # Copy images for animation
        super().__init__(all_sprites)
        os.chdir('data')
        os.chdir('images')
        s = os.listdir()
        os.chdir('..')
        os.chdir('..')

        # Objects
        self.frames = []
        for i in s:
            self.frames.append(load_image('images/' + i))
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.image.get_rect().move(x, y)
        self.rect.x = x
        self.rect.y = y
        self.action = False

    def update(self):
        if (self.cur_frame + 2) <= len(self.frames):
            self.cur_frame = (self.cur_frame + 1) % len(self.frames)
            self.image = self.frames[self.cur_frame]
        else:
            self.cur_frame = 0
            self.action = False

    def position(self, x, y):
        self.rect.x = x
        self.rect.y = y


class Health(pygame.sprite.Sprite):
    def __init__(self, hp, pos_x, pos_y):
        super().__init__(hp_sprites, all_sprites)
        self.hp = hp
        self.pos_x = pos_x
        self.pos_y = pos_y

        self.image = load_image('red_heart.png')
        self.rect = self.image.get_rect().move(pos_x, pos_y)
    
    def hp_show(self):
        if self.hp > 9:
            font = pygame.font.Font(None, 40)
            screen.blit(font.render(str(self.hp), 1, pygame.Color('black')), (self.pos_x + 35, self.pos_y + 25))
        else:
            font = pygame.font.Font(None, 40)
            screen.blit(font.render(str(self.hp), 1, pygame.Color('black')), (self.pos_x + 40, self.pos_y + 25))


class Mana(pygame.sprite.Sprite):
    def __init__(self, mana, pos_x, pos_y):
        super().__init__(mana_sprites, all_sprites)
        self.mana = mana
        self.pos_x = pos_x
        self.pos_y = pos_y

        self.image = load_image('Blue_Star.png')
        self.rect = self.image.get_rect().move(pos_x, pos_y)

    def mana_show(self):
        if self.mana > 9:
            font = pygame.font.Font(None, 40)
            screen.blit(font.render(str(self.mana), 1, pygame.Color('black')), (self.pos_x + 35, self.pos_y + 40))
        else:
            font = pygame.font.Font(None, 40)
            screen.blit(font.render(str(self.mana), 1, pygame.Color('black')), (self.pos_x + 44, self.pos_y + 40))


class Player:
    def __init__(self, pos_hp, pos_mana, hp, mana, user=None):
        self.hp = hp
        self.mana = mana
        self.deck_type = []
        self.deck_played = ['', '', '', '', '']
        self.deck = []
        self.user = user

        self.hp_ob = Health(hp, pos_hp[0], pos_hp[-1])
        self.mana_ob = Mana(mana, pos_mana[0], pos_mana[-1])


# Выбор режима
def start_screen():
    global player_hp, board

    screen.fill((30, 30, 30))
    fon = pygame.transform.scale(load_image('book.png'), (w, h))
    screen.blit(fon, (0, 0))

    all_sprites = pygame.sprite.Group()
    close_win = False

    # Buttons
    btn_1 = Button(108, 50, 3, all_sprites)
    btn_2 = Button(108, 200, 4, all_sprites)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in all_sprites:
                    all_sprites.update(event)
            if event.type == pygame.MOUSEBUTTONUP:
                if btn_1.action:
                    for i in range(11):
                        pygame.time.delay(50)
                        transparency()
                    btn_1.action = False
                    btn_1.image = load_image('Button_clasik.png', -1)
                    all_sprites = pygame.sprite.Group()
                    board = load_image('hearthstone_desk.jpg')
                    player_hp = 45
                    game()
                    close_win = True
                
                if btn_2.action:
                    for i in range(11):
                        pygame.time.delay(50)
                        transparency()
                    btn_2.action = False
                    btn_2.image = load_image('Button_fast.png', -1)
                    all_sprites = pygame.sprite.Group()
                    board = load_image('Desk.png')
                    player_hp = 25
                    game()

        if close_win:
            break
    
        all_sprites.draw(screen)
        pygame.display.flip()


# Основная игра
def game():
    global player_hp, board

    # Players
    player_1 = Player((w - 130, h - 120), (w - 250, h - 130), player_hp, 10, user)
    player_2 = Player((w - 130, 20), (w - 250, 15), player_hp, 10)

    # Cards
    cards = []

    x = 100
    y = 550
    player_step = player_1
    for j in range(2):
        for i in range(5):
            # No repeating cards
            card = Card(x, y, player_step, j + 1, i, deck[randint(0, 9)])
            while card.typeCard.type in player_step.deck_type:
                card.die()
                card = Card(x, y, player_step, j + 1, i, deck[randint(0, 9)])
            cards.append(card)
            player_step.deck_type.append(card.typeCard.type)
            player_step.deck.append(card)
            x += 100
        y = -80
        x = 100
        player_step = player_2

    # Fields
    fields = []
    x = 70
    y = 125
    player_step = player_2
    for j in range(2):
        for i in range(5):
            fields.append(Field((x, y), (130, 183), (189, 183, 107), player_step))
            x += 150
        y = 325
        x = 70
        player_step = player_1

    # Button
    btn_back = Button(700, 600, 1, buttons_sprite)
    btn_step = Button(w - 130, 275, 2, all_sprites)

    # Timer
    time_count = 45
    font = pygame.font.SysFont(None, 200)
    text_time = font.render(str(time_count), True, (255, 0, 0))

    timer_event = pygame.USEREVENT+1
    pygame.time.set_timer(timer_event, 1000)

    # Animation
    clouds = AnimatedSprite(w, h)

    # Game variables
    game_round = 0
    game_end = False
    close_window = False
    player_step = player_1
    mana = 10

    clock = pygame.time.Clock()
    
    moved = False
    fps = 60
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            # New round
            elif event.type == timer_event:
                time_count -= 1
                if time_count <= 10:
                    text_time = font.render(str(time_count), True, (255, 0, 0))
                if time_count == 0:
                    # Change Player
                    if player_step == player_1:
                        player_step = player_2
                    else:
                        player_step = player_1
                    
                    mana += 1
                    player_step.mana_ob.mana = mana
                    game_round += 1
                    time_count = 45
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in buttons_sprite:
                    buttons_sprite.update(event)
                
                for el in all_sprites:
                    if el.__class__ == Button and player_step == player_1:
                        el.update(event)
                
                for card in cards:
                    # Player choose card (checking)
                    if not card.played:
                        # Not player_2
                        if player_step == player_1:
                            # Right player need
                            if card.player == player_step:
                                if card.collide(event):
                                    old_x = card.rect.x
                                    old_y = card.rect.y
                                    past_x = event.pos[0] - card.rect.x
                                    past_y = event.pos[1] - card.rect.y
                                    moved = True
                                    break
                else:
                    if not moved:
                        card = ''
            if event.type == pygame.MOUSEBUTTONUP:
                # Exit
                if btn_back.action and game_end:
                    for i in range(11):
                        pygame.time.delay(50)
                        transparency()
                    btn_back.action = False
                    btn_back.image = load_image('back_btn.png', -1)
                    close_window = True

                 # New round
                if btn_step.action and player_step == player_1:
                    btn_step.action = False
                    btn_step.image = load_image('button_step.png')

                    # Change Player
                    if player_step == player_1:
                        player_step = player_2
                    else:
                        player_step = player_1
                    
                    mana += 1
                    player_step.mana_ob.mana = mana
                    game_round += 1
                    time_count = 45

                # Player move (checking)
                for field in fields:
                    if field.collide(event):
                        if moved and field.player == player_step:
                            if card and not field.activate:
                                if player_step.mana_ob.mana >= card.coast:
                                    player_step.deck[card.id] = ''
                                    player_step.deck_type[card.id] = ''
                                    player_step.deck_played[card.id] = card
                                    card.update(field.x + 2, field.y + 2)
                                    card.image_update()
                                    card.played = True
                                    field.activate = True
                                    clouds.position(player_step.mana_ob.pos_x, player_step.mana_ob.pos_y + 2)
                                    clouds.action = True
                                    player_step.mana_ob.mana -= card.coast
                                    card = ''
                    else:
                        if card:
                            card.update(old_x, old_y)
                moved = False
            if event.type == pygame.MOUSEMOTION:
                if moved:
                    x = event.pos[0] - past_x
                    y = event.pos[1] - past_y
                    card.update(x, y)

        # Display flip
        screen.fill((20, 20, 20))

        if close_window:
            break
        
        # Attack
        if time_count == 45 and game_round > 1:
            for i in range(len(player_step.deck_played)):
                if player_1 == player_step:
                    p1 = player_2
                else:
                    p1 = player_1
                
                el2 = player_step.deck_played[i]
                if el2 != '':
                    if el2.played:
                        if p1.deck_played[i] == '':
                            p1.hp_ob.hp -= el2.typeCard.atk
                            clouds.position(p1.hp_ob.pos_x, p1.hp_ob.pos_y + 2)
                            clouds.action = True
                        else:
                            p1.deck_played[i].typeCard.hp -= el2.typeCard.atk
                            if p1.deck_played[i].typeCard.hp <= 0:
                                p1.deck_played[i].die()
                                p1.deck_played[i] = ''

            time_count -= 1
        
        # Give cards
        if time_count == 44 and game_round != 0:
            x = 100
            for el in range(len(player_step.deck)):
                if player_step.deck[el] == '':
                    if player_step == player_1:
                        y = 550
                        id = 1
                    else:
                        y = -80
                        id = 2

                    # No repeating cards
                    card = Card(x + (100 * el), y, player_step, id, el, deck[randint(0, 9)])
                    while card in cards:
                        card = Card(x + (100 * el), y, player_step, id, el, deck[randint(0, 9)])

                    cards.append(card)
                    player_step.deck_type[el] = card.typeCard.type
                    player_step.deck[el] = card

                    time_count -= 1
                    break
        
        # New round
        if player_step.mana_ob.mana == 0:
            # Change Player
            if player_step == player_1:
                player_step = player_2
            else:
                player_step = player_1
            
            mana += 1
            player_step.mana_ob.mana = mana
            game_round += 1
            time_count = 45

        # Win or lose
        if player_1.hp_ob.hp <= 0 or player_2.hp_ob.hp <= 0:
            cards = []
            # Draw Screen
            font_end = pygame.font.Font(None, 40)
            if player_1.hp_ob.hp <= 0:
                screen.fill((20, 20, 20))
                fon = pygame.transform.scale(load_image('gameover_screen.png'), (w, h))
                screen.blit(fon, (0, 0))
            else:
                screen.fill((20, 20, 20))
                fon = pygame.transform.scale(load_image('win_screen.png'), (w, h))
                screen.blit(fon, (0, 0))
            
            if not game_end:
                # Connect
                try:
                    con = sqlite3.connect("data/Database/users.db")
                    loses = con.cursor().execute("""SELECT lose FROM users
                    WHERE username = ?""", (user,)).fetchone()[0]
                    wins = con.cursor().execute("""SELECT win FROM users
                    WHERE username = ?""", (user,)).fetchone()[0]
                    level = con.cursor().execute("""SELECT level FROM users
                    WHERE username = ?""", (user,)).fetchone()[0]

                    if player_1.hp_ob.hp == 0:
                        if loses:
                            loses += 1
                        else:
                            loses = 1
                        con.cursor().execute("""UPDATE users
                        SET lose = ?
                        WHERE username = ?""", (loses, user))
                    
                    if player_2.hp_ob.hp == 0:
                        if wins:
                            wins += 1
                        else:
                            wins = 1

                        if level:
                            level += 0.5
                        else:
                            level = 0.5

                        con.cursor().execute("""UPDATE users
                        SET win = ?, level = ?
                        WHERE username = ?""", (wins, level, user))
                    
                    con.commit()
                    con.close()
                except Exception:
                    pass
                
                game_end = True
            
            # Draw objects
            try:
                lable = ['user: ' + str(user), 'level: ' + str(level), 'wins: ' + str(wins), 'loses: ' + str(loses)]
                top = 20
                for i in range(4):
                    font_text = font_end.render(lable[i], 1, pygame.Color('Snow'))
                    font_rect = font_text.get_rect()
                    font_rect.top = top
                    top += 30
                    font_rect.x = 700
                    screen.blit(font_text, font_rect)
            except Exception:
                pass

            buttons_sprite.draw(screen)
        else:
            # Screen
            screen.fill((20, 20, 20))
            fon = pygame.transform.scale(board, (w, h))
            screen.blit(fon, (0, 0))

            # Draw objects
            for field in fields:
                pygame.draw.rect(screen, field.color, field.rect, 5)
            all_sprites.draw(screen)

            # Player
            player_1.hp_ob.hp_show()
            player_1.mana_ob.mana_show()
            player_2.hp_ob.hp_show()
            player_2.mana_ob.mana_show()

            # Cards
            for i in cards:
                if i != '':
                    try:
                        i.hp_show()
                        i.atk_show()
                        i.mana_show()
                    except Exception:
                        pass

            if clouds.action:
                clouds.update()

            if time_count <= 10:
                text_rect = text_time.get_rect(center = screen.get_rect().center)
                screen.blit(text_time, text_rect)

        clock.tick(fps)
        pygame.display.flip()