import pygame, sys, os
from Game import game
from Rules import rules
from Options import option


# Screen
pygame.init()
w, h = 950, 750
size = width, height = w, h
screen = pygame.display.set_mode(size)


# Sprite groups
all_sprites = pygame.sprite.Group()
buttons_sprite = pygame.sprite.Group()


# Function to close a window
def terminate():
    pygame.quit()
    sys.exit()


# Function (animation of closing the window)
def transparency():
    s = pygame.Surface((1000,750))
    s.set_alpha(128)
    s.fill((20, 20, 20))
    screen.blit(s, (0,0))
    pygame.display.flip()


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


class Button(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, num):
        super().__init__(buttons_sprite, all_sprites)
        # Choosing right image
        if num == 1:
            self.image = load_image('Button_start_1.png', -1)
        if num == 2:
            self.image = load_image('Button_options_1.png', -1)
        if num == 3:
            self.image = load_image('Button_exit_1.png', -1)
        if num == 4:
            self.image = load_image('Button_rules_1.png', -1)

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
                self.image = load_image('Button_start_2.png', -1)
            
            if self.num == 2:
                self.image = load_image('Button_options_2.png', -1)
            
            if self.num == 3:
                self.image = load_image('Button_exit_2.png', -1)

            if self.num == 4:
                self.image = load_image('Button_rules_2.png', -1)

            self.action = True
        

def main():
    # Screen
    screen.fill((20, 20, 20))
    fon = pygame.transform.scale(load_image('book.png'), (w, h))
    screen.blit(fon, (0, 0))

    # Buttons
    btn_start = Button(108, 50, 1)
    btn_options = Button(108, 200, 2)
    btn_exit = Button(108, 350, 3)
    btn_rules = Button(550, 50, 4)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.MOUSEBUTTONDOWN: 
                # Button click update
                for button in buttons_sprite:
                    buttons_sprite.update(event)
            
            if event.type == pygame.MOUSEBUTTONUP:
                # Buttons actions
                if btn_start.action:
                    for i in range(11):
                        pygame.time.delay(50)
                        transparency()
                    btn_start.action = False
                    btn_start.image = load_image('Button_start_1.png', -1)
                    game()

                    # Screen
                    screen.fill((20, 20, 20))
                    fon = pygame.transform.scale(load_image('book.png'), (w, h))
                    screen.blit(fon, (0, 0))
                
                if btn_options.action:
                    for i in range(11):
                        pygame.time.delay(50)
                        transparency()
                    btn_options.action = False
                    btn_options.image = load_image('Button_options_1.png', -1)
                    option()

                    # Screen
                    screen.fill((20, 20, 20))
                    fon = pygame.transform.scale(load_image('book.png'), (w, h))
                    screen.blit(fon, (0, 0))

                if btn_rules.action:
                    for i in range(11):
                        pygame.time.delay(50)
                        transparency()
                    btn_rules.action = False
                    btn_rules.image = load_image('Button_rules_1.png', -1)
                    rules()

                    # Screen
                    screen.fill((20, 20, 20))
                    fon = pygame.transform.scale(load_image('book.png'), (w, h))
                    screen.blit(fon, (0, 0))
                
                if btn_exit.action:
                    for i in range(11):
                        pygame.time.delay(50)
                        transparency()
                    btn_exit.action = False
                    btn_exit.image = load_image('Button_exit_1.png', -1)
                    terminate()

        # Display flip
        if pygame.mixer.music.get_busy():
            all_sprites.draw(screen)
            pygame.display.flip()
        else:
            # Music
            file = 'data/Stalker 591 - Rebeca.mp3'
            pygame.init()
            pygame.mixer.init()
            pygame.mixer.music.load(file)
            pygame.mixer.music.set_volume(0.1)
            pygame.mixer.music.play()
            pygame.event.wait()

            all_sprites.draw(screen)
            pygame.display.flip()


main()