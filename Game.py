import pygame, sys, os

# Screen
pygame.init()
w, h = 950, 750
size = width, height = w, h
screen = pygame.display.set_mode(size)

# Sprite groups
all_sprites = pygame.sprite.Group()
card_sprites = pygame.sprite.Group()


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


def game():
    # Cards
    cards = []

    card_1 = Card(100, 500)
    card_2 = Card(200, 500)
    card_3 = Card(300, 500)

    cards.append(card_1)
    cards.append(card_2)
    cards.append(card_3)

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
                            past_x = event.pos[0] - card.rect.x
                            past_y = event.pos[1] - card.rect.y
                            moved = True
                            break
                else:
                    if not moved:
                        card = ''
            if event.type == pygame.MOUSEBUTTONUP:
                if 300 < event.pos[0] < 428 and 100 < event.pos[1] < 281:
                    if card:
                        card.update(301, 101)
                        card.image_update()
                        card.played = True
                        card = ''
                moved = False
            if event.type == pygame.MOUSEMOTION:
                if moved:
                    x = event.pos[0] - past_x
                    y = event.pos[1] - past_y
                    card.update(x, y)

        # Display flip
        screen.fill((20, 20, 20))

        # Draw square
        pygame.draw.rect(screen, (128, 128, 128), ((299, 99), (130, 183)), 5)

        all_sprites.draw(screen)

        clock.tick(fps)
        pygame.display.flip()