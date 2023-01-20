import pygame, sys, os

# Screen
pygame.init()
w, h = 950, 750
size = width, height = w, h
screen = pygame.display.set_mode(size)

# Sprite groups
all_sprites = pygame.sprite.Group()
card_sprites = pygame.sprite.Group()
hp_sprites = pygame.sprite.Group()
mana_sprites = pygame.sprite.Group()


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


class Card(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(card_sprites, all_sprites)

        self.image = load_image('card.jpg', -1)

        # Set position
        self.rect = self.image.get_rect().move(pos_x, pos_y)
        self.rect.x = pos_x
        self.rect.y = pos_y

        # Characteristic
        self.played = False

    def collide(self, *args):
        # Collide button and mouse
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and \
                self.rect.collidepoint(args[0].pos):
            
            return True

    def update(self, *args):
        self.rect.x = args[0]
        self.rect.y = args[1]

    def image_update(self):
        self.image = load_image('card_played.png', -1)


class Field:
    def __init__(self, point_1, point_2, color):
        self.rect = pygame.Rect(point_1, point_2)
        self.x = point_1[0]
        self.y = point_1[-1]
        self.color = color

    def collide(self, *args):
        # Collide button and mouse
        if args and args[0].type == pygame.MOUSEBUTTONUP and \
                self.rect.collidepoint(args[0].pos):
            
            return True


class Health(pygame.sprite.Sprite):
    def __init__(self, hp, pos_x, pos_y):
        super().__init__(hp_sprites, all_sprites)
        self.hp = hp
        self.pos_x = pos_x
        self.pos_y = pos_y

        self.image = load_image('red_heart.png')
        self.rect = self.image.get_rect().move(pos_x, pos_y)
    
    def hp_show(self):
        font = pygame.font.Font(None, 40)
        screen.blit(font.render(str(self.hp), 1, pygame.Color('black')), (self.pos_x + 35, self.pos_y + 25))


class Mana(pygame.sprite.Sprite):
    def __init__(self, mana, pos_x, pos_y):
        super().__init__(mana_sprites, all_sprites)
        self.mana = mana
        self.pos_x = pos_x
        self.pos_y = pos_y

        self.image = load_image('Blue_Star.png')
        self.rect = self.image.get_rect().move(pos_x, pos_y)

    def mana_show(self):
        font = pygame.font.Font(None, 40)
        screen.blit(font.render(str(self.mana), 1, pygame.Color('black')), (self.pos_x + 44, self.pos_y + 40))


class Player:
    def __init__(self, pos_hp, pos_mana, hp, mana):
        self.hp = hp
        self.mana = mana

        self.hp_ob = Health(hp, pos_hp[0], pos_hp[-1])
        self.mana_ob = Mana(mana, pos_mana[0], pos_mana[-1])


def game():
    # Cards
    cards = []

    x = 100
    for i in range(5):
        cards.append(Card(x, 500))
        x += 100

    # Fields
    fields = []
    x = 100
    for i in range(5):
        fields.append(Field((x, 225), (130, 183), (189, 183, 107)))
        x += 150

    # Players
    player_1 = Player((w - 130, h - 120), (w - 250, h - 130), 30, 0)

    # Game variables
    game_round = 0

    clock = pygame.time.Clock()
    
    moved = False
    fps = 60
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for card in cards:
                    if not card.played:
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
                for field in fields:
                    if field.collide(event):
                        if moved:
                            if card:
                                card.update(field.x + 2, field.y + 2)
                                card.image_update()
                                card.played = True
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

        # Screen
        screen.fill((20, 20, 20))
        fon = pygame.transform.scale(load_image('hearthstone_desk.jpg'), (w, h))
        screen.blit(fon, (0, 0))

        # Draw objects
        # pygame.draw.rect(screen, (128, 128, 128), ((299, 99), (130, 183)), 5)

        for field in fields:
            pygame.draw.rect(screen, field.color, field.rect, 5)
        all_sprites.draw(screen)
        player_1.hp_ob.hp_show()
        player_1.mana_ob.mana_show()

        clock.tick(fps)
        pygame.display.flip()