import pygame, sys, os
from pygame.locals import *

# Screen
pygame.init()
w, h = 950, 750
size = width, height = w, h
screen = pygame.display.set_mode(size)

# Sprites
all_sprites = pygame.sprite.Group()


# Function to close a window
def terminate():
    pygame.quit()
    sys.exit()


def transparency():
    s = pygame.Surface((1000,750))
    s.set_alpha(128)
    s.fill((20, 20, 20))
    screen.blit(s, (0,0))
    pygame.display.flip()


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


class Slider:
    def __init__(self, x, y, w, h):
        self.x = x + 50
        self.y = y
        self.activate = False
        self.rect = pygame.Rect(x, y, w, h)
        self.color = 'black'


class Button(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, num):
        super().__init__(all_sprites)
        # Choosing right image
        if num == 1:
            self.image = load_image('Exit_rules.png', -1)

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
                self.image = load_image('Exit_rules2.png', -1)

            self.action = True


def option():
    slider = Slider(120, 150, 300, 10)
    btn_exit = Button(700, 550, 1)
    close_window = False
    
    font = pygame.font.Font(None, 60)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.MOUSEBUTTONDOWN:
                all_sprites.update(event)

                if slider.rect.collidepoint(event.pos):
                    slider.activate = True
                    slider.x = event.pos[0]
                    pygame.draw.circle(screen, pygame.Color('Chocolate'), (slider.x, slider.y + 5), 15)

            if event.type == pygame.MOUSEMOTION:
                if slider.activate and 420 > event.pos[0] > 120:
                    slider.x = event.pos[0]
                    volume = (100 * (event.pos[0] - 120)) / 300 / 100
                    pygame.mixer.music.set_volume(volume)

            if event.type == pygame.MOUSEBUTTONUP:
                slider.activate = False
                if btn_exit.action:
                    for i in range(11):
                        pygame.time.delay(50)
                        transparency()
                    btn_exit.action = False
                    btn_exit.image = load_image('Exit_rules.png', -1)
                    close_window = True

        if close_window:
            break

        # Screen
        screen.fill((20, 20, 20))
        fon = pygame.transform.scale(load_image('book.png'), (w, h))
        screen.blit(fon, (0, 0))

        text = font.render('Громкость', 1, pygame.Color('black'))
        screen.blit(text, (150, 40))

        pygame.draw.rect(screen, slider.color, slider.rect)
        pygame.draw.circle(screen, pygame.Color('Chocolate'), (slider.x, slider.y + 5), 15)

        all_sprites.draw(screen)

        pygame.display.flip()