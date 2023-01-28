import pygame, sys, os

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
        

def rules():
    # Screen
    fon = pygame.transform.scale(load_image('papyrus.jpg'), (w, h))
    screen.blit(fon, (0, 0))
    font_main = pygame.font.Font(None, 60)
    font = pygame.font.Font(None, 30)
    text_coord = 50

    close_window = False

    # Button
    btn_exit = Button(550, 600, 1)

    rule_text = ["Правила", "",
                  "Это коллекционно карточная игра, где тебе надо составить",
                  "конкуренцию для других игроков", "",
                  "Для игры нужно выбрать режим:",
                  "1) Быстрый режим - здоровье игроков 25",
                  "2) Классический режим - здоровье игроков 45",
                  "",
                  "В начале игры у вас будет 5 карт, с разными характеристиками.",
                  "Каждая карта имеет свою цену, силу и особое умение",
                  "Обязательно посмотрите атаку, ману и здоровье карты!",
                  "Если вы сыграете карту, то в следующем раунде получите 1 новую.",
                  "Ваша сыгранная карта аттакует через 1 раунд по соседней карте,",
                  "или по игроку, если в соседнем поле нет карты.",
                  "",
                  "В игре выиграет тот, кто первый убьёт своего противника."]
    
    for line in rule_text:
        if text_coord == 50:
            string_rendered = font_main.render(line, 1, pygame.Color('black'))
            intro_rect = string_rendered.get_rect()
            text_coord += 10
            intro_rect.top = text_coord
            intro_rect.x = 400
            text_coord += intro_rect.height
            screen.blit(string_rendered, intro_rect)
        else:
            string_rendered = font.render(line, 1, pygame.Color('black'))
            intro_rect = string_rendered.get_rect()
            text_coord += 10
            intro_rect.top = text_coord
            intro_rect.x = 110
            text_coord += intro_rect.height
            screen.blit(string_rendered, intro_rect)

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
                if btn_exit.action:
                    for i in range(11):
                        pygame.time.delay(50)
                        transparency()
                    btn_exit.action = False
                    btn_exit.image = load_image('Exit_rules.png', -1)
                    close_window = True

        if close_window:
            break
                    
        all_sprites.draw(screen)
        pygame.display.flip()