import pygame, sys, os

# Screen
pygame.init()
w, h = 750, 550
size = width, height = w, h
screen = pygame.display.set_mode(size)


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
                print('Start game')
            
            if self.num == 2:
                self.image = load_image('Button_options_2.png', -1)
                print('Options')
            
            if self.num == 3:
                self.image = load_image('Button_exit_2.png', -1)
                print('Exit')

            self.action = True
        

if __name__ == '__main__':
    # Sprite groups
    all_sprites = pygame.sprite.Group()
    buttons_sprite = pygame.sprite.Group()

    # Screen
    screen.fill((20, 20, 20))
    fon = pygame.transform.scale(load_image('book.png'), (w, h))
    screen.blit(fon, (0, 0))

    # Buttons
    btn_start = Button(0, 0, 1)
    btn_options = Button(0, 150, 2)
    btn_exit = Button(0, 300, 3)

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
                    btn_start.action = False
                    btn_start.image = load_image('Button_start_1.png', -1)
                
                if btn_options.action:
                    btn_options.action = False
                    btn_options.image = load_image('Button_options_1.png', -1)
                
                if btn_exit.action:
                    btn_exit.action = False
                    btn_exit.image = load_image('Button_exit_1.png', -1)
                    terminate()

        # Display flip
        buttons_sprite.draw(screen)
        pygame.display.flip()