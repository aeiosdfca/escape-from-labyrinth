from pygame import *
from time import sleep

"""Шрифт"""

font.init()
font = font.SysFont("Comic Sans MS", 50)
win = font.render('тебе удалось.', True, (237, 0, 8))
lose = font.render('ты проиграл.', True, (237, 0, 8))
lose_2 = font.render('они нашли тебя.', True, (237, 0, 8))


"""Переменные для картинок"""

img_back = "images/background.png" 
img_hero = "images/crying_boy.png"
img_enemy = "images/doll.png"
img_goal = "images/portal.png"
img_bullet = "images/bullet.png"
img_jumpscare = "images/jumpscare.jpg"


"""Музыка"""

mixer.init()
mixer.music.load("sounds/background_music.ogg")
mixer.music.play(-1)
jumpscare = mixer.Sound("sounds/scream.ogg")


"""Классы"""

class GameSprite(sprite.Sprite):    #Класс - родитель для других классов.
    def __init__(self, player_image, player_x, player_y, width, height, player_speed):
        
        # Вызываем конструктор класса Sprite
        sprite.Sprite.__init__(self)

        # Каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (width, height))
        self.speed = player_speed

        # Каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

        # Метод, отрисовывающий героя на окне
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):              # Метод передвижения
        keys = key.get_pressed()    # Подключаем клавиатуру
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < win_width - 45:
            self.rect.x += self.speed
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 45:
            self.rect.y += self.speed

class Enemy(GameSprite):
    side = "up"
    def update(self):
        if self.rect.y <= win_height * 0.18:
            self.side = "down"
        if self.rect.y >= win_height - 0.12 * win_height:
            self.side = "up"
        if self.side == "up":
            self.rect.y -= self.speed
        else:
            self.rect.y += self.speed

class Enemy2(GameSprite):
    side = "left"
    def update(self):
        if self.rect.x <= 0.228 * win_width:
            self.side = "right"
        if self.rect.x >= win_width - 0.257 * win_width:
            self.side = "left"
        if self.side == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed


class Wall(sprite.Sprite):
    def __init__(self, red, green, blue, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.red = red
        self.green = green
        self.blue = blue
        self.w = wall_width
        self.h = wall_height

        # Каждый спрайт должен хранить свойство image - Surface - прямоугольная подложка.
        self.image = Surface((self.w, self.h))
        self.image.fill((red, green, blue))

        # Каждый спрайт должен иметь свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y

"""Окно игры"""

win_width = 800
win_height = 600
display.set_caption("б̴̗̰͑̉͜͡е̷̧͎͎̮̓̄͠г҈̨̲̳̖̇͞и̷̨̭̞͒͋̿̕.̸̨̯̲̓̋̓͞")
window = display.set_mode((win_width, win_height))
back = transform.scale(image.load(img_back), (win_width, win_height))

speed_multiplyer = 1
if win_width > 800 and speed_multiplyer < 1024:
    speed_multiplyer *= 2
elif win_width >= 1024 and speed_multiplyer < 1280:
    speed_multiplyer *= 3
elif win_width >= 1280 and speed_multiplyer < 1920:
    speed_multiplyer *= 4
elif win_width >= 1920:
    speed_multiplyer *= 5

"""Персонажи"""

hero = Player(img_hero, 0.007 * win_width, win_height - 0.16 * win_height, 0.03 * win_width, 0.07 * win_height, 1 * speed_multiplyer)
monster = Enemy(img_enemy, win_width - 0.193 * win_width, 0.6 * win_height, 0.05 * win_width, 0.11 * win_height, 2 * speed_multiplyer)
final = GameSprite(img_goal, win_width - 0.128 * win_width, win_height - 0.17 * win_height, 0.064* win_width, 0.146 * win_height, 0)
monster2 = Enemy2(img_enemy, win_width - 0.771 * win_width, 0.06 * win_height, 0.053 * win_width, 0.12 * win_height, 2 * speed_multiplyer)


"""Стены"""

w1 = Wall(0, 0, 0, 0, 0, 0.229 * win_width, 0.83 * win_height)
w2 = Wall(0, 0, 0, 0, 0.92 * win_height, 0.286 * win_width, 0.08 * win_height)
w3 = Wall(0, 0, 0, 0.2 * win_width, 0, 0.736 * win_width, 0.056 * win_height)
w4 = Wall(0, 0, 0, 0.286 * win_width, 0.186 * win_height, 0.187 * win_width, 0.814 * win_height)
w5 = Wall(0, 0, 0, 0.472 * win_width, 0.28 * win_height, 0.057 * win_width, 0.72 * win_height)
w6 = Wall(0, 0, 0, 0.513 * win_width, 0.186 * win_height, 0.137 * win_width, 0.9 * win_height)
w7 = Wall(0, 0, 0, 0.649 * win_width, 0.28 * win_height, 0.057 * win_width, 0.72 * win_height)
w8 = Wall(0, 0, 0, 0.693 * win_width, 0.186 * win_height, 0.057 * win_width, 0.9 * win_height)
w9 = Wall(0, 0, 0, 0.721 * win_width, 0.186 * win_height, 0.071 * win_width, 0.16 * win_height)
w10 = Wall(0, 0, 0, 0.735 * win_width, 0.466 * win_height, 0.057 * win_width, 0.22 * win_height)
w11 = Wall(0, 0, 0, 0.735 * win_width, 0.81 * win_height, 0.057 * win_width, 0.19 * win_height)
w12 = Wall(0, 0, 0, 0.864 * win_width, 0, 0.064 * win_width, 0.44 * win_height)
w13 = Wall(0, 0, 0, 0.864 * win_width, 0.58 * win_height, 0.064 * win_width, 0.22 * win_height)
w14 = Wall(0, 0, 0, 0.907 * win_width, 0, 0.093 * win_width, 0.8 * win_height)
w15 = Wall(0, 0, 0, 0.942 * win_width, 0, 0.057 * win_width, win_height)


"""Группы спрайтов"""

monsters = sprite.Group()
walls = sprite.Group()


"""Добавлление спрайтов в игру"""

monsters.add(monster)
monsters.add(monster2)

walls.add(w1)
walls.add(w2)
walls.add(w3)
walls.add(w4)
walls.add(w5)
walls.add(w6)
walls.add(w7)
walls.add(w8)
walls.add(w9)
walls.add(w10)
walls.add(w11)
walls.add(w12)
walls.add(w13)
walls.add(w14)
walls.add(w15)


"""Игровой цикл"""

game = True
finish = False
clock = time.Clock()
FPS = 60
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.blit(back, (0, 0))

        walls.draw(window)
        monsters.update()
        monsters.draw(window)
        hero.reset()
        hero.update()
        final.reset()

        # Поражение
        if sprite.spritecollide(hero, monsters, False):
            finish = True
            jumpscare.play()
            back = transform.scale(image.load(img_jumpscare), (win_width, win_height))
            window.blit(back, (0, 0))
            mixer.music.pause()
            window.blit(lose_2, (175, 300))
        if sprite.spritecollide(hero, walls, False):
            finish = True
            mixer.music.pause()
            window.fill((0, 0, 0))
            window.blit(lose,(200, 200))

        # Победа
        if sprite.collide_rect(hero, final):
            finish = True
            mixer.music.pause()
            window.fill((0, 0, 0))
            window.blit(win, (200, 200))

    display.update()
    clock.tick(FPS)


