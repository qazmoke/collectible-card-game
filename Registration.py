import pygame
import sqlite3
import sys, os

pygame.init()
size = w, h = 400, 400
screen = pygame.display.set_mode(size)

# Function to close a window
def terminate():
    pygame.quit()
    sys.exit()


class Text_Box():
    def __init__(self, x, y, w, h):
        self.box = pygame.Rect(x, y, w, h)
        self.activate = False
        self.text = ''


class Button():
    def __init__(self, x, y, w, h):
        self.btn = pygame.Rect(x, y, w, h)
        self.activate = False
        self.color = 'DodgerBlue'


def registr():
    # Text
    font = pygame.font.Font(None, 30)
    font_rule = pygame.font.Font(None, 22)
    font_logo = pygame.font.Font(None, 50)

    box_login = Text_Box(120, 100, 200, 40)
    box_password_1 = Text_Box(120, 160, 200, 40)
    box_password_2 = Text_Box(120, 220, 200, 40)

    # Buttons
    btn_back = Button(20, 330, 150, 40)
    btn_confirm = Button(230, 330, 150, 40)

    fps = 60
    error = False
    close_window = False
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if btn_back.btn.collidepoint(event.pos):
                    btn_back.activate = True
                    btn_back.color = 'RoyalBlue'
                if btn_confirm.btn.collidepoint(event.pos):
                    btn_confirm.activate = True
                    btn_confirm.color = 'RoyalBlue'
                
                if box_login.box.collidepoint(event.pos):
                    box_login.activate = not box_login.activate
                    box_password_1.activate = False
                    box_password_2.activate = False
                if box_password_1.box.collidepoint(event.pos):
                    box_password_1.activate = not box_password_1.activate
                    box_login.activate = False
                    box_password_2.activate = False
                if box_password_2.box.collidepoint(event.pos):
                    box_password_2.activate = not box_password_2.activate
                    box_login.activate = False
                    box_password_1.activate = False
            
            if event.type == pygame.MOUSEBUTTONUP:
                if btn_back.activate:
                    btn_back.activate = False
                    btn_back.color = 'DodgerBlue'
                    close_window = True
                
                if btn_confirm.activate:
                    btn_confirm.activate = False
                    btn_confirm.color = 'DodgerBlue'

                    if box_login.text and box_password_1.text and box_password_2.text:
                        if len(box_login.text) >= 5:
                            if not box_login.text.isdigit():
                                
                                if box_password_1.text == box_password_2.text:
                                    if len(box_password_1.text) >= 5:
                                        if not box_password_1.text.isdigit():
                                            if not box_password_1.text.isalpha():
                                                if not box_password_1.text.isupper():
                                                    if not box_password_1.text.islower():
                                                        con = sqlite3.connect("data/Database/users.db")
                                                        con.cursor().execute("""INSERT INTO users(username, password) 
                                                        VALUES(?, ?)""", (box_login.text, box_password_1.text))

                                                        con.commit()
                                                        con.close()

                                                        close_window = True
                                                    else:
                                                        error = 'Буквы пароля должны быть не только нижнего регистра'
                                                else:
                                                    error = 'Буквы пароля должны быть не только верхнкего регистра'
                                            else:
                                                error = 'Пароль не может состоять только из букв'
                                        else:
                                            error = 'Пароль не может состоять только из цифр'
                                    else:
                                        error = 'Слишком короткий пароль'
                                else:
                                    error = 'Пароли не совпадают'
                            else:
                                error = 'Логин не может состоять только из цифр'
                        else:
                            error = 'Слишком короткое имя'
                    
                    if error:
                        print(error)
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    if box_login.activate:
                        box_login.text = box_login.text[:-1]
                    
                    if box_password_1.activate:
                        box_password_1.text = box_password_1.text[:-1]

                    if box_password_2.activate:
                        box_password_2.text = box_password_2.text[:-1]
                
                elif event.key == pygame.K_RETURN:
                    if box_login.activate:
                        box_login.activate = False
                    
                    if box_password_1.activate:
                        box_password_1.activate = False
                    
                    if box_password_2.activate:
                        box_password_2.activate = False
                
                else:
                    if box_login.activate:
                        box_login.text += event.unicode
                    
                    if box_password_1.activate:
                        box_password_1.text += event.unicode

                    if box_password_2.activate:
                        box_password_2.text += event.unicode
        
        if close_window:
            break
        
        screen.fill((30, 30, 30))

        # Game name
        password_text = font_logo.render('Регистрация', 1, pygame.Color('white'))
        screen.blit(password_text, (90, 20))

        # Text
        text = font_rule.render('Имя должно быть больше 4 символов', 1, pygame.Color('PowderBlue'))
        screen.blit(text, (50, 60))
        text = font_rule.render('не только из цифр', 1, pygame.Color('PowderBlue'))
        screen.blit(text, (50, 72))

        text = font_rule.render('Пароль должно быть больше 4 символов', 1, pygame.Color('PowderBlue'))
        screen.blit(text, (30, 278))
        text = font_rule.render('из цифр и буквб в верхнем и нижнем регистре', 1, pygame.Color('PowderBlue'))
        screen.blit(text, (30, 290))

        # Buttons
        pygame.draw.rect(screen, pygame.Color(btn_back.color), btn_back.btn)
        pygame.draw.rect(screen, pygame.Color(btn_confirm.color), btn_confirm.btn)

        password_text = font.render('Назад', 1, pygame.Color('white'))
        screen.blit(password_text, (60, 340))
        password_text = font.render('Создать', 1, pygame.Color('white'))
        screen.blit(password_text, (265, 340))

        # Login
        login_text = font.render('Имя:', 1, pygame.Color('PowderBlue'))
        login_font = font.render(box_login.text, True, pygame.Color('SteelBlue'))
        screen.blit(login_text, (45, 120))
        screen.blit(login_font, (box_login.box.x + 10, box_login.box.y + 10))

        box_login.box.w = max(200, login_font.get_width() + 20)

        if not box_login.activate:
            pygame.draw.rect(screen, pygame.Color('PowderBlue'), box_login.box, 2)
        else:
            pygame.draw.rect(screen, pygame.Color('DeepSkyBlue'), box_login.box, 2)

        # Password_1
        password_text = font.render('Пароль:', 1, pygame.Color('PowderBlue'))
        password_font = font.render(box_password_1.text, True, pygame.Color('SteelBlue'))
        screen.blit(password_text, (10, 180))
        screen.blit(password_font, (box_password_1.box.x + 10, box_password_1.box.y + 10))

        box_password_1.box.w = max(200, password_font.get_width() + 20)

        if not box_password_1.activate:
            pygame.draw.rect(screen, pygame.Color('PowderBlue'), box_password_1.box, 2)
        else:
            pygame.draw.rect(screen, pygame.Color('DeepSkyBlue'), box_password_1.box, 2)

        # Password_2
        password_text = font.render('Повторите', 1, pygame.Color('PowderBlue'))
        password_font = font.render(box_password_2.text, True, pygame.Color('SteelBlue'))
        screen.blit(password_text, (10, 220))
        screen.blit(password_font, (box_password_2.box.x + 10, box_password_2.box.y + 10))

        password_text = font.render('пароль:', 1, pygame.Color('PowderBlue'))
        screen.blit(password_text, (10, 240))

        box_password_2.box.w = max(200, password_font.get_width() + 20)

        if not box_password_2.activate:
            pygame.draw.rect(screen, pygame.Color('PowderBlue'), box_password_2.box, 2)
        else:
            pygame.draw.rect(screen, pygame.Color('DeepSkyBlue'), box_password_2.box, 2)
        
        clock.tick(fps)
        pygame.display.flip()