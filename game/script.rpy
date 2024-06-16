screen pic():
    default pic = Game()
    add pic

init python:
    import pygame
    SCREEN_WIDTH = 1280
    SCREEN_HEIGHT = 720

    class Game(renpy.Displayable):
        def __init__(self, *args, **kwargs):
            super(Game, self).__init__(*args, **kwargs)
            self.player_frame_down = ["images/player/down/down_0.png", "images/player/down/down_1.png", "images/player/down/down_2.png", "images/player/down/down_3.png"]
            self.player_frame_up = ["images/player/up/up_0.png", "images/player/up/up_1.png", "images/player/up/up_2.png", "images/player/up/up_3.png"]
            self.player_frame_left = ["images/player/left/left_0.png", "images/player/left/left_1.png", "images/player/left/left_2.png", "images/player/left/left_3.png"]
            self.player_frame_right = ["images/player/right/right_0.png", "images/player/right/right_1.png", "images/player/right/right_2.png", "images/player/right/right_3.png"]
            self.x_screen = -800
            self.y_screen = -1000
            self.x_player = 250
            self.y_player = 400
            self.clock = pygame.time.Clock()
            self.animation_speed = 0.1
            self.frame_index = 0
            self.speed = 5
            self.quiti=0
            self.text = renpy.load_image('images/text.png')
            self.bg = renpy.load_image('images/ground.png')
            self.player = renpy.load_image(self.player_frame_down[0])

        def render(self, width, height, st, at):
            ren = renpy.Render(SCREEN_WIDTH, SCREEN_HEIGHT)
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                self.y_screen += self.speed
                self.frame_index += self.animation_speed
                if self.frame_index>4:
                    self.frame_index = 0
                self.player = renpy.load_image(self.player_frame_up[int(self.frame_index)])
            elif keys[pygame.K_DOWN]:
                self.y_screen -= self.speed
                self.frame_index += self.animation_speed
                if self.frame_index>4:
                    self.frame_index = 0
                self.player = renpy.load_image(self.player_frame_down[int(self.frame_index)])
            elif keys[pygame.K_LEFT]:
                self.x_screen += self.speed
                self.frame_index += self.animation_speed
                if self.frame_index>4:
                    self.frame_index = 0
                self.player = renpy.load_image(self.player_frame_left[int(self.frame_index)])
            elif keys[pygame.K_RIGHT]:
                self.x_screen -= self.speed
                self.frame_index += self.animation_speed
                if self.frame_index>4:
                    self.frame_index = 0
                self.player = renpy.load_image(self.player_frame_right[int(self.frame_index)])
            ren.blit(self.bg, (self.x_screen, self.y_screen))
            ren.blit(self.player, (self.x_player, self.y_player))
            if self.x_screen <=-2100 and self.y_screen >=-500:
                ren.blit(self.text, (300, 600))
            if (self.x_screen <=-600 and self.y_screen <=-800) and (self.x_screen >=-1050 and self.y_screen >=-1100):
                self.quiti=0
            elif (self.x_screen <=-1050 and self.y_screen <=-940) and (self.x_screen >=-1180 and self.y_screen >=-1050):
                self.quiti=0
            elif (self.x_screen <=-1180 and self.y_screen <=-850) and (self.x_screen >=-1300 and self.y_screen >=-1000):
                self.quiti=0
            elif (self.x_screen <=-1300 and self.y_screen <=-900) and (self.x_screen >=-1400 and self.y_screen >=-1150):
                self.quiti=0
            elif (self.x_screen <=-1400 and self.y_screen <=-1000) and (self.x_screen >=-1800 and self.y_screen >=-1200):
                self.quiti=0
            elif (self.x_screen <=-1700 and self.y_screen <=-500) and (self.x_screen >=-1900 and self.y_screen >=-1100):
                self.quiti=0
            elif (self.x_screen <=-1750 and self.y_screen <=-300) and (self.x_screen >=-2200 and self.y_screen >=-500):
                self.quiti=0
            else:
                self.quiti=1
            renpy.redraw(self, 0)
            self.clock.tick(60)
            return ren

        def event(self, ev, x, y, st):
            keys = pygame.key.get_pressed()
            globals() ['quit'] = self.quiti
            if keys[pygame.K_q] or self.quiti == 1:
                return keys
            else:
                raise renpy.IgnoreEvent()


screen pic1():
    default pic1 = Game1()
    add pic1

init python:
    import pygame
    SCREEN_WIDTH = 1280
    SCREEN_HEIGHT = 720

    class Game1(renpy.Displayable):
        def __init__(self, *args, **kwargs):
            super(Game1, self).__init__(*args, **kwargs)
            self.player_frame_down = ["images/player/down/down_0.png", "images/player/down/down_1.png", "images/player/down/down_2.png", "images/player/down/down_3.png"]
            self.player_frame_up = ["images/player/up/up_0.png", "images/player/up/up_1.png", "images/player/up/up_2.png", "images/player/up/up_3.png"]
            self.player_frame_left = ["images/player/left/left_0.png", "images/player/left/left_1.png", "images/player/left/left_2.png", "images/player/left/left_3.png"]
            self.player_frame_right = ["images/player/right/right_0.png", "images/player/right/right_1.png", "images/player/right/right_2.png", "images/player/right/right_3.png"]
            globals() ['xs']
            globals() ['ys']
            self.x_screen = xs 
            self.y_screen = ys
            self.x_player = 250
            self.y_player = 400
            self.clock = pygame.time.Clock()
            self.animation_speed = 0.1
            self.frame_index = 0
            self.speed = 8
            self.quiti=0
            self.text = renpy.load_image('images/text1.png')
            self.joke = renpy.load_image('images/text2.png')
            self.bg = renpy.load_image('images/ground1.png')
            self.player = renpy.load_image(self.player_frame_down[0])

        def render(self, width, height, st, at):
            ren = renpy.Render(SCREEN_WIDTH, SCREEN_HEIGHT)
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                self.y_screen += self.speed
                self.frame_index += self.animation_speed
                if self.frame_index>4:
                    self.frame_index = 0
                self.player = renpy.load_image(self.player_frame_up[int(self.frame_index)])
            elif keys[pygame.K_DOWN]:
                self.y_screen -= self.speed
                self.frame_index += self.animation_speed
                if self.frame_index>4:
                    self.frame_index = 0
                self.player = renpy.load_image(self.player_frame_down[int(self.frame_index)])
            elif keys[pygame.K_LEFT]:
                self.x_screen += self.speed
                self.frame_index += self.animation_speed
                if self.frame_index>4:
                    self.frame_index = 0
                self.player = renpy.load_image(self.player_frame_left[int(self.frame_index)])
            elif keys[pygame.K_RIGHT]:
                self.x_screen -= self.speed
                self.frame_index += self.animation_speed
                if self.frame_index>4:
                    self.frame_index = 0
                self.player = renpy.load_image(self.player_frame_right[int(self.frame_index)])
            ren.blit(self.bg, (self.x_screen, self.y_screen))
            ren.blit(self.player, (self.x_player, self.y_player))
            if (self.x_screen <=200 and self.y_screen <=-600) and (self.x_screen >=-100 and self.y_screen >=-1300):#1
                self.quiti = 0
            elif (self.x_screen <=-100 and self.y_screen <=-920) and (self.x_screen >=-880 and self.y_screen >=-1030):#2
                self.quiti = 0
            elif (self.x_screen <=-750 and self.y_screen <=50) and (self.x_screen >=-880 and self.y_screen >=-920):#3
                self.quiti = 0
            elif (self.x_screen <=-100 and self.y_screen <=50) and (self.x_screen >=-750 and self.y_screen >=-90):#4
                self.quiti = 0
            elif (self.x_screen <=-100 and self.y_screen <=350) and (self.x_screen >=-230 and self.y_screen >=0):#5
                self.quiti = 0
            elif (self.x_screen <=-230 and self.y_screen <=350) and (self.x_screen >=-1750 and self.y_screen >=220):#6
                self.quiti = 0
            elif (self.x_screen <=-1650 and self.y_screen <=230) and (self.x_screen >=-1750 and self.y_screen >=-1180):#7
                self.quiti = 0
            elif (self.x_screen <=-1000 and self.y_screen <=-1050) and (self.x_screen >=-1650 and self.y_screen >=-1180):#8
                self.quiti = 0
            elif (self.x_screen <=-1000 and self.y_screen <=-1180) and (self.x_screen >=-1130 and self.y_screen >=-2070):#9
                self.quiti = 0
            elif (self.x_screen <=-1130 and self.y_screen <=-1940) and (self.x_screen >=-2270 and self.y_screen >=-2070):#10
                self.quiti = 0
            elif (self.x_screen <=-2150 and self.y_screen <=-1050) and (self.x_screen >=-2270 and self.y_screen >=-1940):#11
                self.quiti = 0
            elif (self.x_screen <=-1920 and self.y_screen <=-400) and (self.x_screen >=-2520 and self.y_screen >=-1050):#12
                self.quiti = 0
            else:
                self.quiti = 1
            if (self.x_screen <=-2120 and self.y_screen <=-620) and (self.x_screen >=-2320 and self.y_screen >=-840):#12
                ren.blit(self.text, (400, 600))
            if (self.x_screen <=-1920 and self.y_screen <=-400) and (self.x_screen >=-2000 and self.y_screen >=-500):#12
                ren.blit(self.joke, (400, 600))
                self.quiti = 2

            renpy.redraw(self, 0)
            self.clock.tick(60)
            return ren

        def event(self, ev, x, y, st):
            keys = pygame.key.get_pressed()
            globals() ['quit'] = self.quiti
            if keys[pygame.K_q] or self.quiti == 1:
                return keys
            else:
                raise renpy.IgnoreEvent()

screen pic2():
    default pic2 = Game2()
    add pic2

init python:
    import pygame
    SCREEN_WIDTH = 1280
    SCREEN_HEIGHT = 720

    class Game2(renpy.Displayable):
        def __init__(self, *args, **kwargs):
            super(Game2, self).__init__(*args, **kwargs)
            self.player_frame_down = ["images/player/down/down_0.png", "images/player/down/down_1.png", "images/player/down/down_2.png", "images/player/down/down_3.png"]
            self.player_frame_up = ["images/player/up/up_0.png", "images/player/up/up_1.png", "images/player/up/up_2.png", "images/player/up/up_3.png"]
            self.player_frame_left = ["images/player/left/left_0.png", "images/player/left/left_1.png", "images/player/left/left_2.png", "images/player/left/left_3.png"]
            self.player_frame_right = ["images/player/right/right_0.png", "images/player/right/right_1.png", "images/player/right/right_2.png", "images/player/right/right_3.png"]
            globals() ['xs']
            globals() ['ys']
            self.x_screen = xs 
            self.y_screen = ys
            globals() ['background']
            self.x_player = 250
            self.y_player = 400
            self.clock = pygame.time.Clock()
            self.animation_speed = 0.1
            self.frame_index = 0
            self.speed = 5
            self.quiti=0
            self.table = renpy.load_image('images/text3.png')
            self.wat = renpy.load_image('images/text4.png')
            self.bg = globals() ['background']
            self.player = renpy.load_image(self.player_frame_down[0])

        def render(self, width, height, st, at):
            ren = renpy.Render(SCREEN_WIDTH, SCREEN_HEIGHT)
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                self.y_screen += self.speed
                self.frame_index += self.animation_speed
                if self.frame_index>4:
                    self.frame_index = 0
                self.player = renpy.load_image(self.player_frame_up[int(self.frame_index)])
            elif keys[pygame.K_DOWN]:
                self.y_screen -= self.speed
                self.frame_index += self.animation_speed
                if self.frame_index>4:
                    self.frame_index = 0
                self.player = renpy.load_image(self.player_frame_down[int(self.frame_index)])
            elif keys[pygame.K_LEFT]:
                self.x_screen += self.speed
                self.frame_index += self.animation_speed
                if self.frame_index>4:
                    self.frame_index = 0
                self.player = renpy.load_image(self.player_frame_left[int(self.frame_index)])
            elif keys[pygame.K_RIGHT]:
                self.x_screen -= self.speed
                self.frame_index += self.animation_speed
                if self.frame_index>4:
                    self.frame_index = 0
                self.player = renpy.load_image(self.player_frame_right[int(self.frame_index)])
            ren.blit(self.bg, (self.x_screen, self.y_screen))
            ren.blit(self.player, (self.x_player, self.y_player))
            if (self.x_screen <=-370 and self.y_screen <=-370) and (self.x_screen >=-600 and self.y_screen >=-650):#1
                self.quiti=0
            elif (self.x_screen <=-440 and self.y_screen <=-150) and (self.x_screen >=-550 and self.y_screen >=-370):#2
                self.quiti=0
            elif (self.x_screen <=-300 and self.y_screen <=-20) and (self.x_screen >=-670 and self.y_screen >=-150):#3
                self.quiti=0
            elif (self.x_screen <=-180 and self.y_screen <=40) and (self.x_screen >=-370 and self.y_screen >=-80):#4
                self.quiti=0
            elif (self.x_screen <=200 and self.y_screen <=300) and (self.x_screen >=-180 and self.y_screen >=-150):#5
                self.quiti=0
            elif (self.x_screen <=-560 and self.y_screen <=230) and (self.x_screen >=-690 and self.y_screen >=-20):#6
                self.quiti=0
            elif (self.x_screen <=-690 and self.y_screen <=100) and (self.x_screen >=-950 and self.y_screen >=50):#7
                self.quiti=0 #выход в никуда
            elif (self.x_screen <=-300 and self.y_screen <=430) and (self.x_screen >=-940 and self.y_screen >=230):#8
                self.quiti=0
            else:
                self.quiti = 1
            globals() ['xs1'] = self.x_screen
            globals() ['ys1'] = self.y_screen
            if (self.x_screen <=200 and self.y_screen <=300) and (self.x_screen >=-100 and self.y_screen >=0):#5
                ren.blit(self.table, (280, 600)) #сесть за стол
                globals() ['xs1'] = self.x_screen
                globals() ['ys1'] = self.y_screen
                self.quiti=2
            elif (self.x_screen <=-300 and self.y_screen <=430) and (self.x_screen >=-940 and self.y_screen >=380):#8
                ren.blit(self.wat, (280, 600)) #комната
                globals() ['xs1'] = self.x_screen
                globals() ['ys1'] = self.y_screen
                self.quiti=3
            elif (self.x_screen <=-370 and self.y_screen <=-370) and (self.x_screen >=-600 and self.y_screen >=-420):
                ren.blit(self.wat, (280, 600)) #коридор
                globals() ['xs1'] = self.x_screen
                globals() ['ys1'] = self.y_screen
                self.quiti=4

            renpy.redraw(self, 0)
            self.clock.tick(60)
            return ren

        def event(self, ev, x, y, st):
            keys = pygame.key.get_pressed()
            globals() ['quit'] = self.quiti
            if keys[pygame.K_q] or self.quiti == 1 or self.quiti == 5:
                return keys
            else:
                raise renpy.IgnoreEvent()

init:
    $ import time

screen pic3():
    default pic3 = Game3()
    add pic3

init python:
    import pygame
    SCREEN_WIDTH = 1280
    SCREEN_HEIGHT = 720
    class Game3(renpy.Displayable):
        def __init__(self, *args, **kwargs):
            super(Game3, self).__init__(*args, **kwargs)
            self.player_frame_left = ["images/player/left/left_0.png", "images/player/left/left_1.png", "images/player/left/left_2.png", "images/player/left/left_3.png"]
            self.player_frame_right = ["images/player/right/right_0.png", "images/player/right/right_1.png", "images/player/right/right_2.png", "images/player/right/right_3.png"]
            globals() ['xs']
            self.x_screen = xs 
            self.y_screen = 120
            self.x_player = 250
            self.y_player = 400
            self.clock = pygame.time.Clock()
            self.animation_speed = 0.1
            self.frame_index = 0
            self.speed = 5
            self.quiti=0
            self.text = renpy.load_image('images/text_cor.png')
            self.bg = renpy.load_image('images/ground3.png')
            self.player = renpy.load_image('images/player/right/right_0.png')

        def render(self, width, height, st, at):
            self.quiti = 0
            ren = renpy.Render(SCREEN_WIDTH, SCREEN_HEIGHT)
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RIGHT]:
                self.x_screen -= self.speed
                self.frame_index += self.animation_speed
                if self.frame_index>4:
                    self.frame_index = 0
                self.player = renpy.load_image(self.player_frame_right[int(self.frame_index)])
            ren.blit(self.bg, (self.x_screen, self.y_screen))
            ren.blit(self.player, (self.x_player, self.y_player))
            globals() ['xs1'] = self.x_screen
            if self.x_screen <= -650 and self.x_screen >= -750:
                ren.blit(self.text, (400,600))
                globals() ['xs1'] = self.x_screen
                self.quiti = 1
            if self.x_screen <= -1600 and self.x_screen >= -1700:
                ren.blit(self.text, (400,600))
                globals() ['xs1'] = self.x_screen
                self.quiti = 2
            if self.x_screen <= -2550 and self.x_screen >= -2650:
                ren.blit(self.text, (400,600))
                globals() ['xs1'] = self.x_screen
                self.quiti = 3
            if self.x_screen <= -3600 and self.x_screen >= -3700:
                ren.blit(self.text, (400,600))
                globals() ['xs1'] = self.x_screen
                self.quiti = 4

            renpy.redraw(self, 0)
            self.clock.tick(60)
            return ren

        def event(self, ev, x, y, st):
            keys = pygame.key.get_pressed()
            globals() ['quit'] = self.quiti
            if keys[pygame.K_q]:
                return keys
            else:
                raise renpy.IgnoreEvent()

init python:
    import random, pygame
    TOTAL_STARS = 1000
    SCREEN_WIDTH = 1280
    SCREEN_HEIGHT = 720
    class Star(object):
        color = (0,0,0)
        position = [0,0]
        speed = 1

        def __init__(self):
            self.generateStartPosition(xrandom=True)

        def generateStartPosition(self, xrandom=False):
            if xrandom:
                xpos = random.randint(1, SCREEN_WIDTH - 1)
            else:
                xpos = SCREEN_WIDTH - 1
            self.position = [xpos, random.randint(1, SCREEN_HEIGHT - 1)]
            brightness = random.randint(5, 255)
            self.color = (brightness, brightness, brightness)
            self.speed = float(brightness / 400.0)*3

        def update(self):
            self.position[0] -= self.speed
            if(self.position[0] < 0):
                self.generateStartPosition()

        def draw(self, canvas):
            xpos = int(self.position[0])
            ypos = int(self.position[1])
            canvas.rect(self.color, pygame.Rect(xpos, ypos, 1, 1))

    class StarDisplay(renpy.Displayable):
        def __init__(self, *args, **kwargs):
            super(StarDisplay, self).__init__(*args, **kwargs)
            self.stars = [Star() for x in range(TOTAL_STARS)]

        def render(self, width, height, st, at):
            screen = renpy.Render(SCREEN_WIDTH, SCREEN_HEIGHT)
            canvas = screen.canvas()
            canvas.rect((0,0,0), pygame.Rect(1, 1, SCREEN_WIDTH, SCREEN_HEIGHT))
            for star in self.stars:
                star.draw(canvas)
                star.update()
            renpy.redraw(self, 0)
            return screen


screen star_screen:
    add StarDisplay()




define lin = Character('Лин', color="#69C9FC")

define narrator = Character(None, color="#c1ffc1")

define horse = Character('???', color="#bd64d4")

define spider = Character('???', color="#fb3f51")

define amme = Character('Мама', color="#856fd7")

define father = Character('???', color="#ff9b40")

define god = Character(None, color="#ffffff",what_font="Ustroke.ttf")

define ending = 0



label start:

    play music ochko fadein 0.5

    show bg_ochko_dial at center with dissolve

    "... Первое, что я увидела, когда снова открыла глаза, была воронка."

    "Она будто висела перед моими глазами огромным неоновым колесом, облаком звездной пыли, бездонный сверкающим океаном посреди зияющей пустоты космоса."

    "Слышно не было ничего – как в вакууме – но я ясно чувствовала, как она зовет меня."
    
    "Точно, пошла в папашу. Начинаю слышать зов «горлышка бутылки»."


    show bg_ochko_end at center with dissolve:
        blur 16
        
    lin "..."

    show linstart with dissolve
    
    "Интересно, бутылка «беленькой» казалась отцу такой же красивой?"

    "Кажется, теперь я могу понять. Такое чувство, что я совсем не хочу ей сопротивляться. Посреди холодного безжизненного пространства только воронка обещает тепло. "

    "Не могу сопротивляться."

    show linstart_eyesclosed with dissolve
    hide linstart with dissolve

    lin "... И не хочу."

    hide linstart_eyesclosed with dissolve

    menu:
        "Воронка приглашает вас дальше."

        "Будто у меня есть выбор..." :
            "Так и нужно."
            jump beauty

        "Что? Ну уж нет..." :
            "..."
            jump fail_one

    label fail_one:
        
        hide bg_ochko_end with dissolve

        narrator "Вы остаетесь созерцать воронку."

        narrator "Кажется, выбор уже не изменить."

        $ ending = 1

        jump endgame

    return

    label beauty:

        play music krasota fadein 0.1

        hide bg_ochko_dial
        hide bg_ochko_end

        window hide

        show part1 at center with Dissolve(1.0)
        show name1 at center with Dissolve(1.0)

        hide part1 
        hide name1 with dissolve

        window show

        lin "... Прохладно!"

        show beauty at center with dissolve
            #blur 10

        show lin sad b with dissolve

        lin "Вообще не жарко!"

        show lin normal b with dissolve

        narrator "Холод заставляет меня поежиться, и я оглядываюсь по сторонам."

        lin "... Лес. Супер."

        show lin unamused b with dissolve

        lin "Клещи, сороконожки... "

        lin "Не дай Боже пауки."

        lin "Ненавижу пауков."

        show lin normal b with dissolve

        narrator "Однако, показалось мне, тут совсем неплохо. "

        narrator "Тут тихо и спокойно, и несмотря на прохладу, мне совсем не тревожно."

        narrator "Я уже и не помню, когда не чувствовала беспокойства – такое ощущение, что я избавилась от паразита, без которого мне пусто, но по которому я не скучаю."

        show lin unamused b with dissolve

        lin "... Так."

        show lin normal b with dissolve

        lin "Что это там впереди?.. "
        jump beauty_expl

    return

    label beauty_expl:

        menu:

            "Исследовать лес?"

            "Будто у меня есть выбор...":
                "Идем!"
                window hide
                call screen pic

                if quit == 1:
                    jump fireexit
                else: 
                    jump beauty1

                window show
    return

    return

    label beauty1:   
        hide lin normal b

        narrator "..."  

        show lin normal b with dissolve

        lin "Какая большая... Собака. "

        lin "Нет, лошадь. "

        show lin unamused b with dissolve

        lin "Какая разница? И те, и те кусаются..."

        hide lin unamused b with dissolve

        show horsey at right with dissolve

        horse "... Дитя."

        hide horsey

        show lin normal b with dissolve

        lin "Я."

        show lin unamused b with dissolve

        lin "Но мне 16."

        hide lin unamused b with dissolve

        show horsey at right with dissolve

        horse "По меркам этого места каждый из вас - дитя."

        horse "Ты... Так мала."

        horse "Ты еще росток."

        horse "Интересно, в какое растение ты превратишься?.."

        hide horsey with dissolve

        show lin sad b with dissolve

        lin "Я – будущее растение?"

        lin "А Вы?"

        lin "Вы собака или лошадь, или..."

        show lin sad b at left with dissolve

        show horsey at right with dissolve

        horse "Для тебя, дитя, мое имя – Красота."

        show lin unamused b at left with dissolve

        lin "... Вы его сами себе придумали?"

        lin "Очень... скромно."

        $ horse = Character('Я не буду ее так называть!', color="bd64d4")

        horse "Не дерзи, дитя. Человек придумал слово."

        horse "Я была здесь еще до того, как человечество научилось ходить. "

        horse "У всего живого есть понятие красоты. Скажи мне... "

        horse "Как тебя зовут?"

        show lin startled b at left with dissolve

        lin "..."

        narrator "Сказать ей правду? Сказать ей..."

        show lin thinking b at left with dissolve

        narrator "Вот черт..."


        $ liname = renpy.input("Как мы представимся Красоте?",length = 12,default="").strip()

        narrator "Скажу ей, что меня зовут [liname]."

        lin "... Лин."

        show lin startled b at left with dissolve

        narrator "... Стоп! Почему я это сказала?!"

        narrator "Это ведь тоже не мое настоящее..."

        narrator "Но Красота смотрит так, как будто видит меня насквозь."

        $ horse = Character('Красота', color="#bd64d4")

        horse "..."

        horse "... Тебе здесь нравится?"


        lin "..."

        show lin sad b at left with dissolve

        lin "..."

        lin "... Здесь очень спокойно. "

        lin "И рядом с вами гораздо теплее. Мне здесь очень нравится, если честно, я бы даже сказала, что здесь... "

        lin "... Красиво."

        hide lin sad b with dissolve

        narrator "Красота удовлетворительно кивает."

        show horsey full at center with dissolve

        horse "Ты уже догадалась, дитя? "

        horse "..."

        horse "Конечно нет."

        horse "Не переживай. Воспоминания вернутся, если ты захочешь вспомнить."

        horse "Если же не захочешь... В любом случае, ты всегда сможешь остаться здесь. "

        horse "В моем лесу еще очень много места."

        horse "Иди, дитя. Не пугайся. "

        horse "Каждое живое существо пройдет этот путь рано или поздно."

        horse "..."

        horse "... Возьми это."

        hide horsey full with dissolve

        narrator "В своих руках я обнаруживаю клочок бумаги."

        show sp1 with dissolve 

        narrator "Я пробегаюсь по нему глазами, но совсем ничего не понимаю."

        narrator "Какая чушь!"

        narrator "..."

        hide sp1 with dissolve


        hide beauty with dissolve

        stop music fadeout 1.0

        jump knowledge

    label knowledge:

        window hide

        show part2 at center with Dissolve(1.0)
        show name2 at center with Dissolve(1.0)

        play music pauchihap fadein 1.0

        scene knowl with dissolve

        show lin lyba k with dissolve

        window show

        lin "...Библиотека! "

        lin "Библиотека - это замечательно... Мне кажется, я много времени проводила в библиотеке раньше. Вот только...  "

        show lin fi k with dissolve

        lin "Пауки."

        lin "..."

        show lin eyesclosed k with dissolve

        narrator "Меня пробила дрожь. Нужно идти аккуратно – не хочу наткнуться на паутину..."

        hide lin eyesclosed k with dissolve

    label knowledge_expl:

        menu:

            "Пройти по библиотеке?"

            "Будто у меня есть выбор...":
                "Идем!"

                scene blackbg
                window hide

                $ xs = 50
                $ ys = -1000

                if quit == 2:
                    $ xs = -1950
                    $ ys = -450
                    
                call screen pic1
                if quit == 1:
                    jump fireexit1
                elif quit == 2:
                    jump aneki
                else:
                    jump knowledge1

                window show

    label knowledge1:

        scene knowl with dissolve
        stop music fadeout 0.1


        show lin fi k with dissolve



        lin "... А-а-а! Паук! Паук!"

        hide lin fi k with dissolve

        show spidey mad with dissolve 

        play sound alert

        spider "А-а-а! Примат! Примат!"

        hide spidey mad with dissolve

        show lin mad k with dissolve

        play music pauchiha 

        lin "Примат?!"

        hide lin mad k

        show spidey mad 

        spider "Паук?!"

        show spidey mad at right with dissolve

        show lin mad k at left with dissolve

        lin "Я не примат! "

        lin "Меня зовут Лин! Лин! "

        spider "Грубиянка – вот твое имя! Я не паук! "

        show spidey norm at right with dissolve

        spider "Я – Президент Ассоциации Ученых-членистоногих Института Хронологического архивирования!"

        show spidey heh at right with dissolve

        lin "Президент Ассоциации Ученых-Членистоногих... П, А, У, Ч... Стой подожди..."

        show spidey norm at right with dissolve

        $ spider = Character('П.А.У.Ч.И.Х.А.', color="#fb3f51")

        spider "Ближе к делу! Что ты хочешь узнать?! "

        lin "Что? Узнать что?.. Я не знаю!"

        hide lin mad k

        show spidey norm at center with dissolve

        spider "Прекрасно! Тогда ты узнаешь все!"

        show spidey norm:
            linear 0.8 xpos 0.75

        spider "Вблизи земной орбиты температура составляет +4 градуса по Цельсию!"

        spider "Но я не советю проверять, хотя это даже теплее, чем в земном океане – самая низкая температура воды в Северном Ледовитом океане не превышает +1 градуса по Цельсию!"

        show spidey norm:
            linear 0.8 xpos 0.5

        spider "На океаническом дне киты разлагаются от 70 до 100 лет!"

        spider "Не бойся, им там совсем не одиноко – они образуют вокруг себя устойчивую экосистему!"

        show spidey norm:
            linear 0.8 xpos 0.25

        spider "Утопление делится на три основных вида – истинное, асфиктическое и синкопальное!"

        spider "Сможешь отличить? "

        show spidey norm:
            linear 1.6 xpos 0.8

        spider "Возраст отдельных особей вида Сосна остистая межгорная может достигать 5000 лет!"

        spider "Представь, каково это - жить так долго? Жуть! "

        show spidey norm with dissolve:
            xpos 0.8
            blur 10

        stop music fadeout 3.0

        show lin startled k at left with dissolve  

        play music pauchihamad fadein 1.0

        narrator "Я затихаю. "

        narrator "По какой-то причине, мое сердце заходится, как будто бы предчувствуя опастность, как будто бы мне понуждая меня убежать. "

        narrator "Вот только... Вокруг ни намека на угрозу."

        narrator "Эти факты - простой мусор, даже никак друг с другом не связанный! "

        narrator "Разлагающиеся киты, деревья-долгожители, холодные воды, асфиксия... "

        narrator "Я чувствую, как меня начинает легко потряхивать. "

        narrator "Я не хочу об этом думать. "

        narrator "Я не хочу об этом думать! "

        show lin sad k at left with dissolve

        lin "Стоп!"

        hide spidey norm

        show spidey heh at right with dissolve 

        lin "Стой, пожалуйста, не говори больше ничего!"

        lin "..."

        show spidey norm at right with dissolve 

        spider "Ага! Ты боишься! "

        show lin defeated k at left with dissolve

        spider "Ты боишься знать, боишься думать об этом слишком долго! "

        spider "Твой мозг водит тебя кругами, не подпуская к чему-то страшному!"

        spider "Думай, маленький примат, думай!"

        spider "Может, это подтолкнет твой крошечный мозг к каким-то выводам?.."

        hide lin with dissolve

        hide spidey with dissolve

        show sp2 with dissolve

        narrator "Своими цепкими, пушистыми лапками Паучиха протягивает мне клочок бумаги, похожий на предыдущий."

        narrator "Но руки трясутся от накатившей паники. Такое ощущение, что если буду вчитываться в слова, то точно лишусь рассудка."

        narrator "Я прячу проклятый клочок в карман, подальше от глаз."

        hide sp2 with dissolve

        show spidey norm at right with dissolve 

        show lin defeated k at left with dissolve

        lin "Я... Мне это не нужно!"

        lin "Ты давишь на меня! Ты... "

        show spidey mad at right with dissolve

        spider "А чего ты ожидала, маленькая упрямая обезьянка? "

        hide lin

        show spidey mad:
            linear 1.6 xpos 0.7

        spider "Что сможешь просто пройти дальше, не прилагая усилий? "

        spider "О, Небеса, да такие как ты нечасто здесь бывают!"

        spider "{i}Нин-хили{/i} этажом выше вас всех балует своим теплым приемом, своими расслабляющими речами, а мне разбираться! "

        spider "Делать всю работу! Заставлять вас, оболтусов, думать!"

        spider "Не хотите вспоминать! Не хотите разбираться!"

        spider "Или ты что, решила послушать старую дуру {i}Нин-хили{/i} и остаться у нее на поляне?!"

        lin "Заткнись!"

        show spidey what at center with dissolve        

        lin "Не хочу тебя слушать, насекомое!"

        show spidey mad at center with dissolve

        spider "Эй! Я не насекомое, я – членистоногое!.."

        play sound running

        show spidey what at center with dissolve

        spider "..."

        show spidey heh at center with dissolve

        spider "Ладно, ладно, хорошо, хорошо. "

        spider "... Пусть с ней разбираются дальше. Кстати говоря, об этом..."

        narrator "{i}Нин-пагду{/i} берет в свои лапы тяжелую книгу, перелистывая хрупкие, пыльные страницы."

        show spidey norm at center with dissolve

        spider "... Ха-ха-ха. Ха-ха-ха-ха-ха! {i}Нин-амме{/i}?! Очевидно, очевидно же! Ха-ха, классика."

        show spidey heh at center with dissolve

        spider "Ну... Удачи, {i}Нин-амме{/i}."

        scene blackbg with Dissolve(1.0)

        jump wish

    return


    label wish:

        show part3 at center with Dissolve(1.0)
        show name3 at center with Dissolve(1.0)
        hide part3

        hide name3 with Dissolve(1.0)

        play music home

        $ year, month, day, hour, minute, second, dow, doy, dst = time.localtime()
        $ myes = ["января","февраля","марта","апреля","мая","июня","июля","августа","сентября","октября","ноября","декабря"]





        father "... Гулечка? Чего бледная вся? И носишься как погорелец..."

        lin "А?.."

        $ father = Character('Папа', color="#ff9b40")

        show home with dissolve

        show lin startled with dissolve

        lin "А?!"

        narrator "О нет, нет, нет!"

        narrator "Странная космическая воронка, загадочная лошадь в холодном лесу, пугающее разумное членистоногое – все на свете меркло по сравнению с этим местом."

        narrator "Дом родной."

        narrator "Мысль развиться не успевает – из размышлений меня вырвает знакомый голос."

        show lin startled at left with dissolve

        show dilf say at right with dissolve

        father "... Галя! Прием!"

        show dilf norm at right with dissolve

        narrator "Папа? Трезвый, не ругается..."

        show lin sad at left with dissolve

        narrator "Не плачет?.."

        show dilf say at right with dissolve

        father "Марш за стол! Мама индигирку нарубила, ждет тебя, дурочку, плачет... "

        father "Ой, где же Галя, кто же съест весь этот салат..."

        show dilf norm at right with dissolve

        show lin startled at left with dissolve

        narrator "Мама?.. "

        narrator "Мама тоже здесь?.. "

        show lin thinking at left with dissolve

        narrator "Что это за время? Что за место?"

        narrator "Папа же, с самозабвенной улыбкой на лице, продолжает пародировать маму."

        show dilf say at right with dissolve

        father "Ой, кому же, кому же достанутся все эти «мартышки»..."

        hide dilf with dissolve

        show lin startled at center

        lin "«Мартышки»?!"

        narrator "При упоминании «мартышек» мое критическое мышление отключается, и вся странность ситуации меркнет."

        show lin happy at center with dissolve

        lin "Я бегу! Бегу!"

        hide lin with dissolve 

        hide home with dissolve

    label wish_expl:

        menu:

            "Пройти по дому?"

            "Будто у меня есть выбор...":
                "Идем!"
                window hide
                $background = renpy.load_image('images/ground2.png')
                screen blackbg
                
                $ xs = -470
                $ ys = -590

                if quit == 2 or quit == 3 or quit == 4:
                    $ xs = xs1
                    $ ys = ys1

                call screen pic2

                if quit == 1:
                    jump fireexit2
                elif quit == 2:
                    jump wish1
                elif quit == 3:
                    jump room
                elif quit == 4:
                    jump corr



                window show
    return

    label wish1:

        hide lin

        hide home with Dissolve(1.0)

        show blackbg with Dissolve(0.5)

        play sound silverware

        show kitchen with dissolve

        show lin wsmile at center with dissolve 

        narrator "Поверить не могу. "

        narrator "Стол, уставленный едой. "

        narrator "Старая скатерть, которая лежит обратной стороной, потому что верхнюю я изрисовала маркером. "

        narrator "«Мартышки» с брусничным вареньем, Индигирка, лепешки, деревянный ытык, который сломался, но все равно лежал в дальнем ящике, недовольный папа, который хотел рассольник, и... "

        narrator "...И мама."

        narrator "Обнаруживаю под рукой клочок бумаги."

        hide lin with dissolve

        show sp3 with dissolve

        narrator "Мое имя, наше село... Все эти странные существа пытались мне вручить клочки какой-то справки?"

        narrator "Странное дело - каких-то серьезных болезней у меня никогда не было. Даже и не помню, когда в последний раз была в больнице не на простой консультации..."

        narrator "В любом случае, к этим бумажкам у меня нет никакого интереса. Прячу ее в карман, поднимаю глаза на маму."

        hide sp3 with dissolve

        narrator "Мама тепло улыбается мне."

        show lin wsmile at left with dissolve 

        show amme at right with dissolve

        amme "Галя, доченька... Такая взрослая. "

        amme "С каждым днем все выше и выше, все больше похожа на маму... "

        amme "Как и мама твоя была похожа на ее маму."

        amme "Помнишь бабушку Кундуунэ? У вас..."

        show lin happy at left with dissolve

        lin "Конечно помню! У нас был день рождения в один день. [day]-го [myes[month - 1]]! Так ведь?" 

        amme "Так и есть. Совсем... Совсем скоро, да? "

        amme "Гулечка, милая, что бы ты хотела получить на день рождения?"

        show lin thinking at left with dissolve

        lin "Я... Не знаю."

        narrator "Как-то слишком часто я стала это повторять..."

        narrator "Но я не хочу сейчас думать. "

        narrator "Просто хочу остаться здесь, хочу говорить с мамой и есть «мартышки»."

        show lin happy at left with dissolve

        lin "Не важно."

        amme " Ну как же так... Все чего-то хотят."

        amme "Ну же, «Лин». Ты не исключение. Думаешь, нам здесь это не известно? "

        stop music fadeout 3.0

        show lin startled at left with dissolve

        play music home_2 fadein 1.5

        stop sound

        lin "..."

        amme "Я уже знаю, как видишь. Ты тоже знаешь, только почему-то не говоришь, даже себе."

        amme "Скажи же мне, «Лин». Какое твое самое сильное желание?"

        show lin thinking at left with dissolve

        lin "..."

        narrator "Черт возьми, одно и то же, в этом проклятом месте все одно и то же!.."

        narrator "Стоит мне только расслабиться, стоит только почувствовать себя счастливо и спокойно, как у меня выбивают почву из-под ног. "

        narrator "Сначала эта противная паучиха, теперь... Она, кем бы она ни была. "

        narrator "Чего они все от меня хотят?!"

        show lin eyesclosed at left with dissolve

        narrator "Она знает. Очевидно, что она знает."

        narrator "Какой уже смысл?"

        lin "Хочу..."

        lin "Хочу, чтобы мама вернулась."

        lin "..."

        amme "Ну вот же. "

        amme "Дорогая, позволь спросить еще кое-что... Помнишь ли ты, как мама выглядела?"

        show lin sad at left with dissolve

        narrator "Я смотрю на лицо напротив и не могу его разглядеть. Как будто все плывет перед глазами - да и важно ли это?.."

        narrator "Помню ли я ее лицо? Ее глаза? Ее голос?"

        narrator "Когда она ушла? Как давно это случилось, если в голове ни следа от нее не осталось?"

        narrator "Эта женщина передо мной - похожа ли она на мою маму хотя бы на капельку?"

        narrator "..."

        lin "... Не очень. Папа выбросил все ее фотографии, и всю ее одежду, кроме..."

        show lin thinking at left with dissolve

        narrator "Я смотрю на свое платье - помятое, старое, явно из другой эпохи. Выцветший галстук, пыльный фартук."

        narrator "Наверное, я всегда надеялась, что однажды, надев его, смогу увидеть ее хотя бы в отражении."

        show lin sad at left with dissolve

        amme "Умница, гулечка."

        amme "Наконец-то решила перестать убегать? Хорошо."

        amme "Помнишь, как ее звали?"

        lin "... Айталина."

        lin "Как-то так вышло, что дома ее имя сократилось просто до... «Лин»."

        lin "Я не знаю, зачем я так представилась."

        lin "Я не знаю, почему ношу ее заколки, не знаю, почему надела ее платье... "

        show lin cry at left with dissolve

        lin "Иногда мне кажется, что эта пыльная тряпка все еще пахнет ей – но я даже не помню, какие духи она использовала!"

        lin "Я не помню ее лица, не помню ее голоса!"

        lin "..."

        show lin sadcry at left with dissolve

        amme "Вот незадача... Хочешь, чтобы она вернулась, но даже не помнишь, как она выглядела и каким человеком она была?"

        amme "Точно ли ты хочешь чтобы {i}твоя{/i} мама вернулась?"

        amme "Или та мама, которую ты себе придумала?"

        show lin cry at left with dissolve

        lin "Это... Это не важно! Не важно, какой она была!"

        lin "Все, что я помню, это то, что с ней все было лучше! "

        lin "Я была счастлива, мне было тепло и радостно, где бы я ни находилась, мне всегда хотелось домой! "

        lin "Я ее не помню, но она точно была лучшей на свете, наверное, поэтому и продолжаю цепляться за все, что от нее осталось! "

        lin "Ты, кем бы ты ни была, скажи мне... "

        lin "Почему ее не стало?.."

        show lin sadcry at left with dissolve

        $ amme = Character('Мама?..', color="#856fd7")

        narrator "«Мама» смотрит на меня все с той же неизменной улыбкой на лице. "

        narrator "У мамы была такая же? Не помню..."

        amme "..."

        amme "И почему же ты так уверена, что она умерла?"

        narrator "Я чувствую, как бледнеет мое лицо."

        show lin startled cry at left with dissolve

        lin "Просто потому что... Потому что по другому никак!"

        lin "На что ты намекаешь?! Что она жива и просто... Оставила нас с папой?.."

        amme "Я не знаю. И ты не знаешь, однако... "

        amme "Ты тоже об этом думала."

        show lin angry cry at left with dissolve

        lin "Нет! Она никогда бы так не сделала!"

        amme "Откуда тебе знать, что сделала бы эта незнакомка?"

        lin "Хватит! Не называй ее так! "

        lin "Ты, подделка, обманщица, какое право ты имеешь так говорить про нее?!"

        lin "Чего вы все от меня хотите?! Почему продолжаете меня мучить?!"

        lin "Я не сделала ничего плохого! Я всего лишь..."

        lin "Всего лишь..."

        show lin startled cry at left with dissolve

        amme "Да, Галя? Ты хочешь что-то сказать?"

        lin "Молчи... Молчи, я не хочу слушать тебя..."

        lin "Я ухожу.. Ухожу... Понятно?.."

        hide lin with dissolve

        amme "..."

        show amme at center with dissolve

        narrator "Нин-амме усмехается."

        narrator "Она возвращается за стол и окидывает взглядом теперь уже пустое помещение, которое, кусочек за кусочком, начинает распадаться, растворяться, исчезать, возвращаясь к своему первоначальному облику."

        hide amme with dissolve
        
        hide kitchen with dissolve

        jump patience



    return


    label patience:

        show part4 at center with Dissolve(1.0)
        show name4 at center with Dissolve(1.0)

        show corr with dissolve

        hide part4
        hide name4

        play music patience fadein 1.5
        show lin eyesclosed with dissolve 

        lin "..."

        show lin irr with dissolve

        lin "..."

        show lin fu with dissolve

        lin "..."

        show lin mad with dissolve

        lin "... Да сколько можно! По-моему, я иду по этому коридору уже целую вечность..."

        show lin fu with dissolve

        lin "..."

        show lin eyesclosed with dissolve

        lin "Ну ничего. С каждым шагом я все дальше и дальше от этих чудаков. "

        show lin norm with dissolve

        lin "Ну, я надеюсь..."

        "В этом коридоре ничего нет. Я шагаю и шагаю и шагаю, и совсем ничего не меняется... "

        "И, к сожалению, мне нечем заняться, поэтому я рассуждаю. Наконец-то. Надеюсь, они все довольны..."

        "Ничего больше мне не остается – все эти существа, как один, пытаются меня заставить вспомнить что-то, что я вспоминать не хочу. "

        "Такое уж у меня ощущение. Однако, меня мучают сомнения... "

        "Если я не буду ничего вспоминать, я могу застрять здесь навечно... "

        show lin thinking with dissolve

        "В этом монотонном коридоре, шагая вперед целую вечность и не двигаясь никуда ни на шаг... \n Топ топ... \n  Ужасно."

        "Как только в моей голове поселяются сомнения, я замечаю что-то на полу. "

        show lin norm with dissolve

        "Коридор, как будто чувствуя мое смятение, изменяется, подкидывая мне... "

        hide lin with dissolve

        show screen star_screen

        $ xs = 260
        call screen pic3

        hide screen star_screen

        lin "Растение?"

        show klukva with dissolve

        lin "Это цветок клюквы? Красивый... Как на маминых заколках."

        lin "Я надевала их, потому что думала, что они отвлекут внимание от моих проплешин, но увы. "

        lin "Видимо, это уже никакой бижутерией не скрыть."

        lin "Хмм... Еще тогда, Красота задумалась - какое растение из меня бы получилось? Я думаю что была бы, все-таки, кустом с клюквой..."

        lin "Стелилась бы себе по заболоченным берегам..."

        lin "Помню, Красота тогда сказала, что я смогу вернуться к ней на поляну, если захочу..."

        lin "Получается, в крайнем случае у меня будет шанс сбежать к ней, да?.."

        lin "Значит, наверняка, ничего страшного не случится, если я попробую разобраться."

        hide klukva with dissolve

        show lin norm with dissolve

        lin "..."

        "Кажется, я начинаю понимать, как здесь все работает. Очень ожидаемо - коридор видоизменяется, как только я отвлекаюсь от веточки и иду дальше."

        hide lin with dissolve

        show screen star_screen

        $ xs = xs1
        call screen pic3

        hide screen star_screen

        show diary with dissolve

        "... Старый дневник."

        "Толстый и дешевый, весь в пыли и какой-то помятый... Это мой?"

        lin "Обложка кажется такой... Знакомой. Очень интересно..."

        define dflag = 1 

        while dflag != 0:
            menu:
                "Даты не разглядеть, но могу почитать отрывки."

                "Были в городе...":
                    "... Были в городе. Доктор сказал, что у меня очаговая алопеция на нервной почве."
                    "Рыдала весь день, а папа сказал только, что это семейное наверное, потому что он начал лысеть в 25. "
                    "Придурок!"

                "Когда-нибудь я стану...":
                    "Когда-нибудь я стану директором этой школы и запрещу подавать гречку в столовой..."
                    "По двум основным причинам: первая – она какая-то недовареная и пресная, вторая – я хочу макароны в масле."

                "Геля позавчера сказала...":
                    "Геля позавчера сказала, что меня исключат, потому что я не сдала книгу в библиотеку, а еще придется платить штраф. "
                    "Пришла домой и сказала папе, что меня выгонят из школы и что я вся в долгах, а он сказал: Ага, угу... "
                    "Потом оказалось, что это неправда, но все равно неприятно."

                "Лето началось...":
                    "Лето началось! Прощай школа, здравствуй, свобода! "
                    "Правда, придется терпеть жуков..."
                    "И папа уже три месяца не хочет ставить москитную сетку – все время сидит у себя в комнате, если не работает."

                "Папа обещал ...":
                    "Папа обещал сводить меня на речку, но в итоге, как обычно, никуда не пошел."
                    "Сходила одна и кидала туда камни."
                    "Потом надо будет проверить, насколько там глубоко."

                "Отложить дневник.":
                    "Больше ничего нет."
                    $ dflag = 0

        hide diary with dissolve

        show lin eyesclosed with dissolve

        "Я вздыхаю. Если честно, картинка не может не складываться. Я не дурочка какая-то, все-таки... Просто трусиха."

        "И я понимаю к чему все идет, и знаю что увижу дальше."

        "Мне страшно, но здесь есть плюсы - в этом темном коридоре я, по крайней мере, одна... Я надеюсь."

        show lin norm with dissolve

        lin "Ну давай, коридор. Что там у тебя дальше?"

        hide lin with dissolve

        show screen star_screen

        $ xs = xs1
        call screen pic3

        hide screen star_screen

        "Пройдя чуть дальше, я подбираю с пола знакомые заколки, отряхивая их от пыли."

        show zklk with dissolve 

        lin "Мои заколки... Мамины заколки. Из того немногого, что осталось после нее, к ним я привязалась больше всего."

        "..."

        "Мама... Вот тогда все, кажется, и начало идти коту под хвост."

        "Теперь я даже не уверена, что вообще с ней случилось... Я ведь никогда не видела ее могилу, не была на ее похоронах. "

        "Я думала, что я это просто забыла, но откуда мне знать? Уже и не знаю, что думать..."

        "Главное, что когда мама ушла, дома стало пусто, папа закрылся, а у меня начались проблемы со здоровьем. "

        "Как-то и с друзьями перестала общаться, и больше не ходила в библиотеку..."

        "..."

        hide zklk with dissolve

        show lin eyesclosed with dissolve

        "На самом деле, я понимаю что это за место. Тут, по сути, вся моя жизнь; каждое место и каждая деталь - это все мои радости и печали... "

        "Все, что со мной случилось. "

        show lin thinking with dissolve

        "И они хотят чтобы я... Вспомнила? Приняла? Как-то так, что-то вроде ритуала... "

        show lin norm with dissolve 

        "Ну, я не могу сказать точно – такими книжками я не интересовалась. "

        "И если это место создано для того, чтобы помочь мне вспомнить мою жизнь..."

        show lin thinking with dissolve

        "Я осторожно прохожу дальше. Три кусочка какого-то документа лежат в кармане, и я уже знаю, что мне придется подобрать дальше."

        hide lin with dissolve

        show screen star_screen

        $ xs = xs1
        call screen pic3

        hide screen star_screen

        show sp4 blur with dissolve

        "Это последний обрывок справки. "

        "Где-то на подсознательном уровне я понимаю, что я там увижу, но... Действительно ли я этого хочу? Все-таки... "

        "Красота сказала, что я смогу вернутся к ней. "

        "Я знаю, что если я пойду дальше, то меня ожидает что-то неприятное, а если останусь здесь, то это... навсегда."

        menu:
            "Кажется, у меня все-таки есть выбор..."

            "Вернуться в Лес...":
                jump badendingbeauty

            "Посмотреть последний фрагмент документа...":
                "Подбираю последний кусочек, уже зная, что я там увижу."

        
        "Справка говорит сама за себя."

        show sp4 with dissolve

        "Неужели это действительно произошло?.. "

        hide sp4 with dissolve

        show spall with dissolve 

        "Конечно, я не особо удивлена – все-таки, сейчас я здесь, и это совсем не похоже на что-то, что можно увидеть при жизни..."

        show spall fin with dissolve 

        "..."

        "Видимо, придется вспомнить самое страшное – что произошло... Тогда. "

        "Это была случайность? Может, помог кто-то из знакомых? Папа?.. Нет, не думаю..."

        "В любом случае, теперь пути назад уже нет."

        hide spall

        hide corr

        window hide

        jump fear




    
    label fear:

        show part5 at center with Dissolve(1.0)
        show name5 at center with Dissolve(1.0)

        play music home_2 fadein 1.5

        show home5 with dissolve

        hide part5
        hide name5

        window show

        show lin norm with dissolve

        lin "Все происходит так, как я и ожидала. "

        lin "Я снова в нашем «доме», только теперь он выглядит так, как я его запомнила – ковры давно никто не чистил, и бутылки никто не выносил. "

        lin "Везде пыль, хотя я и убиралась недавно, кажется."

        show lin s with dissolve

        lin "Я слышу, как работает радио на кухне. Кажется, «папа» там."

        hide lin with dissolve

    label fear_expl:

        menu:

            "Пройти по дому?"

            "Придется.": 
                "Идем!"
                window hide
                $background = renpy.load_image('images/ground4.png')
                show blackbg
                
                $ xs = -470
                $ ys = -590

                if quit == 2 or quit == 3 or quit == 4:
                    $ xs = xs1
                    $ ys = ys1

                call screen pic2

                if quit == 1:
                    jump fireexit5
                elif quit == 2:
                    jump fear1
                elif quit == 3:
                    jump room1
                elif quit == 4:
                    jump corr1



                window show
    return

    label fear1:

        show kitchen5 with dissolve 

        $ father = Character('«Папа»', color="#ff9b40")

        "«Папа», или скорее то, что так на него похоже, стоит спиной ко мне, а потом поворачивается. "

        "Все, как я помню – он больше не улыбается, и от него пахнет алкоголем."

        show dni op at right with dissolve 

        father "Гуля... Ты уже вернулась..."

        show dni at right with dissolve 

        show lin s at left with dissolve 

        "Тяжело снова это видеть, но я напомнимаю себе – это совсем не мой отец."

        show lin sop at left with dissolve 

        lin "Слушай, понятия не имею кто ты... "

        lin "Может быть, просто скажешь мне, что со мной случилось? "

        show lin s at left with dissolve 

        "«Папа» не меняется в лице, но я вижу, как мелькает недовольство в его глазах."

        show dni op at right with dissolve 

        father "А может {i}ты{/i} мне скажешь, что с тобой случилось? "

        show lin mad at left with dissolve 

        show dni at right with dissolve 

        lin "Ну я-то не помню! Разве не легче просто мне рассказать, а не пытать меня этими непонятными намеками и сценками?!"

        show dni mad at right with dissolve 

        show lin mad cl at left with dissolve 

        father "Легче?!"

        father "Да легче было бы выдавать вам все брошюрки, путеводители, и краткий пересказ вашей жизни со схемами, списками и фотографиями.  Однако мы этого не делаем!"

        father "Откуда вы такие ленивые беретесь?!"

        father "Вот раньше люди приходили, днями о стены бились, но сами хотели все узнать, даже помогать почти не надо было... А сейчас – тьфу. "

        father "Остаются все в саду Нин-хили, и дело с концом, а остальным все подавай на блюдечке с голубой каемочкой! "

        show lin irr at left with dissolve 

        father "Да что за поколение!"

        father "Что там с вами вообще наверху делают, что вы такие пожеванные приходите?.."

        show lin mad at left with dissolve 

        lin "Ну пап!"

        show dni at right with dissolve 

        show lin mad cl at left with dissolve 

        "Говорю я почти на автомате. Это, конечно же, не мой папа, но ведет он себя как классический отец."

        lin "..."

        show lin eyesclosed at left with dissolve 

        lin "..."

        show lin sop at left with dissolve 

        lin "Ну серьезно... "

        lin "Дома, ну, то есть, на прошлом этаже, та... Женщина сказала мне - вам известно все, что знаю я... Даже если я этого не помню."

        lin "Почему бы тебе просто не рассказать?"

        show lin s at left with dissolve 

        show dni eyesclosed at right with dissolve

        "«Папа» молчит и недовольно хмурится, после чего вздыхает - видимо, сдается."

        father "... Премия."

        show lin mad at left with dissolve 

        lin "Чего?"

        show dni mad at right with dissolve

        father "Тогда моя премия ну уж точно уйдет Нин-пагду! Таковы правила."        

        show lin s at left with dissolve

        show dni at right with dissolve

        lin "Нин-пагду? Кто-то из ваших? Ну, местных?.."

        show dni unamused at right with dissolve

        "«Папа» смотрит на меня, приподняв бровь, будто бы я – самое глупое существо на всем белом свете."

        father "Нин-пагду. Президент Ассоциации Членистоногих-"

        show lin unamused at left with dissolve

        lin "Все, все, поняла. Паучиха."

        show dni smile at right with dissolve

        "«Папа» ухмыляется."

        father "Паучиха, хаха... Именно. "

        father "Как этому насекомому повезло – облик она не меняет, да и нюансов в работе никаких... Встречай да рассказывай, а меня от перевоплощений уже тошнит..."

        show dni mad at right with dissolve

        father "То школьная учительница, то начальник, то агент спецслужб... И ладно бы люди или дикие животные – нет ничего такого в том, чтобы бояться льва-людоеда, но..."

        father "Тебе когда-нибудь приходилось превращаться в комнату, полную воздушных шаров?"

        show lin mad at left with dissolve 

        lin "Чего? А ты-то сам как думаешь?! Нет конечно! Ты идиот?"

        show dni mad at right with dissolve 

        show lin mad cl at left with dissolve 

        father "Иногда бываю! Некоторые боятся идиотов. Может, я веду себя так, потому что {i}он{/i} был идиотом?.."

        show dni at right with dissolve 

        "«Папа» указывает на себя."

        show dni op at right with dissolve 

        father "Твой отец, я так полагаю? Просто догадываюсь. Популярный образ, все-таки... "

        father "Слушай, пляши от этого – я не могу сказать тебе напрямую, могу лишь помочь. И раз уж ты разрушила очарование моего представления... Остается только думать. "
        
        father "Твой страх напрямую связан с этим человеком. Почему?"

        show dni at right with dissolve 

        show lin thinking at left with dissolve 

        "Я задумываюсь. Действительно, почему?"

        "Мой папа никогда не был агрессивным, и даже когда ушла мама, он стал просто... Никаким."

        show lin norm at left with dissolve 

        lin "Папа никогда не поднимал на меня руку. Конечно, он очень изменился после того, как мамы не стало, но он не срывался на меня... "

        lin "И ни на кого другого тоже. Он не ругался, не кричал, да и вообще очень редко со мной разговаривал. "

        lin "Вряд ли он как-то причастен к моей смерти."

        show dni op at right with dissolve 

        father "Тем не менее, вот он я здесь. Вспоминай все, что можешь."

        show dni at right with dissolve

        show lin thinking at left with dissolve 

        "Ну чушь какая-то... "

        lin "Говорю же, он просто стал очень тихим. Даже слишком..."

        lin "Кажется, с каждым днем он тоже становился все дальше и дальше... "

        lin "Я тогда еще думала, что такими темпами останусь совсем одна, и... О..."

        show lin surpr at left with dissolve 

        lin "Погодите-ка..."

        show dni smile at right with dissolve

        "«Папа», кажется, понимает, что я догадалась. "

        "Я все думала, что после того, как я вспомню, у меня начнется истерика, что весь тот ужас, который копился в этом месте, как снежный ком, погребет меня под собой и не отпустит, но... "

        "На удивление, мне становится так легко."

        show lin wsmile at left with dissolve 

        lin "А-а-а, так вот что... "

        "Я не боялась папу. "

        "Я боялась что он исчезнет, как исчезла мама, и подумала... Что я скорее умру, чем потеряю последнего близкого человека. "

        "Так странно... Я смотрю на свои руки, как будто бы только осознавая, что действительно произошло."

        "Пазло складывается кусочек за кусочком - глупые факты Паучихи, расспросы «мамы»... Видимо, тогда я все-таки проверила глубину речки."

        lin "Выходит, никто не виноват... "

        lin "Я думала, раз уж я такая трусиха, что этот вариант даже и рассматривать не стоит... "

        show lin lyba at left with dissolve 

        lin "Вот уж действительно, глупый примат."

        "«Папа» кивает, его выражение лица не разобрать – мне совсем не понятно, о чем он думает сейчас. Может быть, о премии..."

        show lin wsmile at left with dissolve 

        lin "Слушай, а чем вам выплачивают премию? Не рублями же?"

        show dni eyesclosed at right with dissolve

        father "А этого лучше тебе не знать... Ну все, иди уже, не трать мое время. "

        show lin s at left with dissolve 

        lin "Идти? Хмм... А куда дальше-то?.."

        "«Папа» пожимает плечами, отмахиваясь от меня как от назойливой мухи."

        father "Понятия не имею... Куда? Не знаю. Как? Предполагаю, что как обычно. Через дверь."

        hide dni with dissolve

        hide lin with dissolve

        show lin wsmile at center with dissolve 

        lin "Я качаю головой с легкой улыбкой, разворачиваюсь и иду к двери, в моем сердце больше ни страха, ни тревоги."

        hide lin with dissolve 

        hide kitchen5 with Dissolve(3.0)

        jump goodending



    label goodending:

        stop music fadeout 2.0

        show ge with Dissolve(3.0)

        play music ochko fadein 1.0

        "Я открываю дверь, и вижу перед собой чудо из чудес - безграничный, бесконечный простор облаков, окрашенных мягким светом."

        "Мое сердце замирает, когда я гляжу вниз - там, подо мной, бездна звезд. Далекие планеты и мерцающие солнца неизвестных миров."

        "Мне так легко... Порыв теплого ветра расплетает мои несчастные косички на три волоска - я так давно не носила распущенные волосы, стеснялась и стыдилась..."

        "Теперь мне некого стыдиться."

        "Кажется, никто не собирается карать меня за мои деяния; быть может, причина в том, что я искупила себя в этом месте..."

        "... А может быть, в моей жизни и не было ничего, за что стоило бы меня наказывать."

        $ ending = 3

        hide ge with dissolve

        jump endgame

        
        


    label fireexit:
        show bg_ochko_end at center with dissolve:
            blur 16

        show linstart with dissolve

        god "ВЫ ВЫШЛИ ЗА ГРАНИЦЫ И ТЕРЯЕТЕ СИЛУ"

        lin "А?.."

        god "ВЫ НЕ МОЖЕТЕ СБЕЖАТЬ ИЗ БОЖЕСТВЕННОГО САДА"

        lin "Чего..."

        god "ДАЖЕ НЕ ПЫТАЙТЕСЬ"

        god "МЫ ВОЗВРАЩАЕМ ВАС В НАЧАЛО"

        god "НЕ ПОВТОРЯЙТЕ СВОИХ ОШИБОК"

        hide linstart with dissolve

        hide bg_ochko_end with dissolve  
        
        jump beauty_expl

    return

    label fireexit2:
        scene blackbg
        show home at center with dissolve

        show lin sad with dissolve

        god "КАК ТОЛЬКО ВЫ ДЕЛАЕТЕ ШАГ ЗА ГРАНИЦУ, ПРОСТРАНСТВО ВОКРУГ ВАС НАЧИНАЕТ РАЗРУШАТЬСЯ"

        lin "..."

        god "КИРПИЧИК ЗА КИРПИЧИКОМ, ВАШ ЛЮБИМЫЙ ДОМ РАСПАДАЕТСЯ"

        lin "Эй, куда..."

        god "ЕСЛИ НЕ ХОТИТЕ БРАТЬ ОТВЕТСТВЕННОСТЬ ЗА ЕГО РАЗРУШЕНИЕ..."

        god "ЛУЧШЕ НЕ ОСТУПАЙТЕСЬ"

        hide lin sad with dissolve

        hide home with dissolve  
        
        jump wish_expl

    return


    label fireexit5:
        scene blackbg
        show home5 at center with dissolve

        show lin s with dissolve

        god "КАК ТОЛЬКО ВЫ ДЕЛАЕТЕ ШАГ ЗА ГРАНИЦУ, ПРОСТРАНСТВО ВОКРУГ ВАС НАЧИНАЕТ РАЗРУШАТЬСЯ"

        show lin irr with dissolve

        lin "..."

        god "КИРПИЧИК ЗА КИРПИЧИКОМ..."

        show lin mad with dissolve

        lin "Эй!"

        lin "Надоедаешь. Захочу - зайду еще раз! У меня дела. Все. До связи."

        god "..."

        hide lin with dissolve

        hide home5 with dissolve  
        
        jump fear_expl

    return


    label room:
        scene blackbg
        show home at center with dissolve:
            blur 16

        show lin wsmile with dissolve

        lin "Все мои книжки... На месте."

        lin "Истории про Алису Селезневу и про Галактическую полицию..."

        lin "Моя полная коллеция книг про кошек, воюющих в лесу..."

        lin "Энциклопедии, атласы, путеводители..."

        lin "Комиксы и альбомы."

        lin "Все как и раньше."

        hide lin wsmile with dissolve

        hide home with dissolve

        jump wish_expl

    label corr:
        scene blackbg
        show home at center with dissolve:
            blur 16

        show lin wsmile with dissolve
        
        lin "Мамины туфли стоят в шкафу, вместе с папиными шлепанцами."

        lin "Мамина обувь начищена, а шлепанцы такие старые, что скоро распадутся на атомы."

        lin "Но папа всегда говорит, что новые ему не нужны - у него все есть."

        show lin unamused with dissolve

        lin "... Ничего не изменилось."

        hide lin wsmile with dissolve

        hide home with dissolve

        jump wish_expl


    label room1:
        scene blackbg
        show home5 at center with dissolve:
            blur 16

        show lin s with dissolve

        lin "Все на месте, все очень пыльное."

        lin "Очень давно к этим полкам никто не подходил..."

        hide lin with dissolve

        hide home5 with dissolve

        jump fear_expl

    label corr1:
        scene blackbg
        show home5 at center with dissolve

        show lin s with dissolve
        
        lin "Верхняя полка пустует."

        lin "А на нижней - шлепанцы."

        hide lin with dissolve

        hide home5 with dissolve

        jump fear_expl

    label fireexit1:
        show bg_ochko_end at center with dissolve:
            blur 16

        show linstart with dissolve

        god "ВЫ ВЫШЛИ ЗА ГРАНИЦЫ И ТЕРЯЕТЕ УВАЖЕНИЕ"

        lin "Да что же такое!.."

        god "ВЫ НЕ МОЖЕТЕ СБЕЖАТЬ ИЗ БИБЛИОТЕКИ ПЫЛАЮЩЕЙ НИНЕВИИ"

        lin "Из чего?.."

        god "К ТОМУ ЖЕ, СМОТРИТЕЛЬНИЦА УСТАЛА ВАС ЛОВИТЬ"

        god "ВАС МНОГО, А ОНА ОДНА"

        god "ПОЖАЛЕЙТЕ СМОТРИТЕЛЬНИЦУ"

        hide linstart with dissolve

        hide bg_ochko_end with dissolve 
        jump knowledge_expl


    label aneki:
        scene knowl with dissolve

        narrator "КНИГА КОМЕДИЙНЫХ ИСТОРИЙ КЛАССИФИКАЦИИ 'Б' "

        narrator "KОМЕДИЙНАЯ ИСТОРИЯ №1"

        narrator "У мужчины пропала дочь. Через несколько дней ему звонят из полиции:"

        narrator "- Здравствуйте! У нас для Вас три новости - плохая, хорошая и просто великолепная!"

        narrator "- Начнем с плохой."

        narrator "- Мы нашли Вашу дочь - она утонула."

        narrator "- А какая хорошая?"

        narrator "- Мы с нее собрали ведро здоровенных раков."

        narrator "- Какая же тогда великолепная?"

        narrator "- Завтра мы ее снова вытащим и приглашаем Вас на пиво!"
      
        jump knowledge_expl
        


    label badendingbeauty:

        hide sp4 blur with dissolve

        play sound walking    

        "Я оставляю все клочки бумаги на полу, и, сжимая в руке сухую веточку с цветком клюквы, попешно разворачиваюсь и иду назад. "

        "И достигаю двери в считаные минуты – странно, учитывая, что путь в ту сторону занял часы. "

        hide corr

        show homest1 with dissolve
        
        "Я иду по мрачному, темному помещению – видимо, когда-то здесь был мой «дом»? "

        "Из темноты я чувствую, как смотря на меня Ее глаза, однако я не обращаю на нее внимание."

        hide homest1 with dissolve

        show knowl with dissolve

        "Снова прохожу по библиотеке. "

        "Паучиха смотрит на меня поверх своей записной книжки и разочарованно вздыхает, бормоча что-то про премию, но я не смотрю ей в глаза. "

        hide knowl with dissolve

        stop music fadeout 1.0

        "Я иду, иду, иду, и, наконец... Возвращаюсь в Лес."

        stop sound

        play music krasota fadein 1.5

        show beb1 with Dissolve(3.0)

        "Трава здесь такая мягкая... Рядом с Красотой очень тепло, и я не хочу подниматься с земли."

        "Наверное, было бы замечательно стать частью этого леса..."

        "Красота смотрит на меня сверху вниз, ее глаза лучатся теплом."

        horse "Ты вернулась, Дитя."

        horse "Не захотела вспоминать?"

        lin "Я вспомнила... Местами. Просто не захотела идти дальше. Знаешь... "

        lin "Я устала. Папа на мои жалобы всегда отвечал, что на том свете отдохнем... "

        lin "Ха-ха-ха. "

        lin "Не хочу подниматься... "

        lin "Ты не против, если я немного посплю?"

        horse "Совсем нет. Но, ты же понимаешь..."

        lin "... Я знаю."

        lin "Красота, а остальные деревья здесь, они тоже..?"

        "Красота кивает головой, и ее грива волнами падает на траву."

        horse "... Да."

        horse "Тех, кто идет дальше, очень много, но и таких как ты тоже достаточно. "

        horse "Я не в праве винить людей за то, что они ищут покой."

        "Я слабо вздыхаю, закрывая глаза. "

        show beb with dissolve 

        hide beb1

        "Наверное, и правда, нет ничего плохого в том, чтобы здесь остаться, порасти мхом и превратиться во что-то красивое."

        horse "..."

        horse "Интересно... В какое растение ты превратишься?.."      

        $ ending = 2

        hide beb with dissolve

        jump endgame




    label endgame:
        
        if ending == 1:
            "Незнаю что тут сказать ! Вы чето ваще обалдели ! Мы делоли эту игру пять месяцев ! А вы взяле и не по играли .."  
            "А там между в конце деньги выдоют ! И машину ! И квортиру .."
        elif ending == 2:
            "Вы вернулись в Божественный Сад и получили концовку «Нет силы бежать от могилы»."
            "Нет ничего плохого в том, чтобы испугаться. Нет ничего плохого в том, чтобы остаться."
        elif ending == 3:
            "Это путь самых смелых. Вы столкнулись с Дигнир-Ни и получили концовку «Monkey Gone to Heaven». Интересно, куда судьба заведет вас дальше?.."

        "канец!"
        return


    return
