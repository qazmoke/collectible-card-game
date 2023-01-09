import pygame, sys, os

# Screen
pygame.init()
w, h = 750, 550
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
        print(self.rect.width, self.rect.height)

    def update(self, *args):
        self.rect.x = args[0]
        self.rect.y = args[1]

    def image_update(self):
        self.image = load_image('card_played.png', -1)


def game():
    # Cards
    card = Card(100, 100)

    clock = pygame.time.Clock()
    
    moved = False
    played = False
    x = 100
    y = 100
    fps = 60
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if not played:
                    if x + 126 >= event.pos[0] >= x and y + 179 >= event.pos[1] >= y:
                        past_x = event.pos[0] - x
                        past_y = event.pos[1] - y
                        moved = True
            if event.type == pygame.MOUSEBUTTONUP:
                if 300 < event.pos[0] < 428 and 100 < event.pos[1] < 281:
                    card.update(301, 101)
                    card.image_update()
                    played = True
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