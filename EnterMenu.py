import pygame
import sys, os
import sqlite3
from Registration import registr

pygame.init()
size = w, h = 400, 400
screen = pygame.display.set_mode(size)

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


def main():
    font = pygame.font.Font(None, 30)
    font_logo = pygame.font.Font(None, 50)

    box_login = Text_Box(120, 100, 200, 40)
    box_password = Text_Box(120, 200, 200, 40)

    btn_enter = Button(20, 330, 150, 40)
    btn_registr = Button(230, 330, 150, 40)

    fps = 60
    clock = pygame.time.Clock()
    close_window = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if btn_enter.btn.collidepoint(event.pos):
                    btn_enter.activate = True
                    btn_enter.color = 'RoyalBlue'
                if btn_registr.btn.collidepoint(event.pos):
                    btn_registr.activate = True
                    btn_registr.color = 'RoyalBlue'
                
                if box_login.box.collidepoint(event.pos):
                    box_login.activate = not box_login.activate
                    box_password.activate = False
                if box_password.box.collidepoint(event.pos):
                    box_password.activate = not box_password.activate
                    box_login.activate = False
            
            if event.type == pygame.MOUSEBUTTONUP:
                if btn_enter.activate:
                    btn_enter.activate = False
                    btn_enter.color = 'DodgerBlue'

                    con = sqlite3.connect("data/registration.db")
                    res = [i[0] for i in con.cursor().execute("""SELECT name FROM users""").fetchall()]

                    if box_login.text and box_password.text:
                        if box_login.text in res:
                            res = con.cursor().execute("""SELECT password FROM users
                            WHERE name=?""", (box_login.text,)).fetchone()[0]

                            if box_password.text == res:
                                close_window = True
                
                if btn_registr.activate:
                    btn_registr.activate = False
                    btn_registr.color = 'DodgerBlue'
                    registr()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    if box_login.activate:
                        box_login.text = box_login.text[:-1]
                    
                    if box_password.activate:
                        box_password.text = box_password.text[:-1]
                
                elif event.key == pygame.K_RETURN:
                    if box_login.activate:
                        box_login.activate = False
                    
                    if box_password.activate:
                        box_password.activate = False
                
                else:
                    if box_login.activate:
                        box_login.text += event.unicode
                    
                    if box_password.activate:
                        box_password.text += event.unicode

        if close_window:
            for i in range(11):
                pygame.time.delay(50)
                transparency()
            
            import MainMenu
            break
        
        screen.fill((30, 30, 30))

        # Game name

        password_text = font_logo.render('Magic Star Heart', 1, pygame.Color('white'))
        screen.blit(password_text, (80, 20))

        # Buttons
        pygame.draw.rect(screen, pygame.Color(btn_enter.color), btn_enter.btn)
        pygame.draw.rect(screen, pygame.Color(btn_registr.color), btn_registr.btn)

        password_text = font.render('Войти', 1, pygame.Color('white'))
        screen.blit(password_text, (65, 340))
        password_text = font.render('Регистрация', 1, pygame.Color('white'))
        screen.blit(password_text, (245, 340))

        # Login
        login_text = font.render('Имя:', 1, pygame.Color('PowderBlue'))
        login_font = font.render(box_login.text, True, pygame.Color('SteelBlue'))
        screen.blit(login_text, (50, 120))
        screen.blit(login_font, (box_login.box.x + 10, box_login.box.y + 10))

        box_login.box.w = max(200, login_font.get_width() + 20)

        if not box_login.activate:
            pygame.draw.rect(screen, pygame.Color('PowderBlue'), box_login.box, 2)
        else:
            pygame.draw.rect(screen, pygame.Color('DeepSkyBlue'), box_login.box, 2)

        # Password
        password_text = font.render('Пароль:', 1, pygame.Color('PowderBlue'))
        password_font = font.render(box_password.text, True, pygame.Color('SteelBlue'))
        screen.blit(password_text, (15, 220))
        screen.blit(password_font, (box_password.box.x + 10, box_password.box.y + 10))

        box_password.box.w = max(200, password_font.get_width() + 20)

        if not box_password.activate:
            pygame.draw.rect(screen, pygame.Color('PowderBlue'), box_password.box, 2)
        else:
            pygame.draw.rect(screen, pygame.Color('DeepSkyBlue'), box_password.box, 2)
        
        clock.tick(fps)
        pygame.display.flip()

main()