import pygame

from settings import *
from snake import Snake
from food import Food
from profile import Profile


pygame.init()


screen = pygame.display.set_mode(
    (WIDTH, HEIGHT)
)

pygame.display.set_caption(
    "🎀 Strawberry Snake"
)


clock = pygame.time.Clock()


font = pygame.font.SysFont(
    "georgia",
    45
)

small_font = pygame.font.SysFont(
    "georgia",
    28
)



# -----------------------------
# Bow 🎀
# -----------------------------

def draw_bow():

    pygame.draw.ellipse(
        screen,
        (255,120,170),
        (500,20,45,35)
    )

    pygame.draw.ellipse(
        screen,
        (255,120,170),
        (550,20,45,35)
    )

    pygame.draw.circle(
        screen,
        (220,70,130),
        (548,38),
        10
    )



# -----------------------------
# Brick Border 🧱
# -----------------------------

def draw_border():

    brick = (210,140,120)
    mortar = (255,200,200)


    pygame.draw.rect(
        screen,
        brick,
        (5,90,WIDTH-10,HEIGHT-95),
        20
    )


    pygame.draw.rect(
        screen,
        BACKGROUND,
        (25,110,WIDTH-50,HEIGHT-135),
        5
    )


    for y in range(120, HEIGHT-50, 40):

        pygame.draw.line(
            screen,
            mortar,
            (5,y),
            (25,y),
            3
        )


        pygame.draw.line(
            screen,
            mortar,
            (WIDTH-25,y),
            (WIDTH-5,y),
            3
        )


    for x in range(40, WIDTH-40, 40):

        pygame.draw.line(
            screen,
            mortar,
            (x,90),
            (x,110),
            3
        )


        pygame.draw.line(
            screen,
            mortar,
            (x,HEIGHT-25),
            (x,HEIGHT-5),
            3
        )



# -----------------------------
# Button
# -----------------------------

def draw_button(rect,text):

    pygame.draw.rect(
        screen,
        BUTTON,
        rect,
        border_radius=25
    )


    label = font.render(
        text,
        True,
        WHITE
    )


    screen.blit(
        label,
        (
            rect.x+35,
            rect.y+10
        )
    )



# -----------------------------
# Name Screen 👤
# -----------------------------

player_name=""

name_screen=True


while name_screen:


    screen.fill(BACKGROUND)

    draw_bow()


    title = font.render(
        "🎀 Enter Your Name",
        True,
        TEXT
    )

    screen.blit(
        title,
        (120,150)
    )


    name = font.render(
        player_name,
        True,
        TEXT
    )


    screen.blit(
        name,
        (220,250)
    )


    info = small_font.render(
        "Press ENTER",
        True,
        TEXT
    )


    screen.blit(
        info,
        (220,350)
    )


    pygame.display.update()



    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            pygame.quit()
            exit()


        if event.type == pygame.KEYDOWN:


            if event.key == pygame.K_RETURN:

                if player_name:

                    name_screen=False



            elif event.key == pygame.K_BACKSPACE:

                player_name = player_name[:-1]


            else:

                player_name += event.unicode




profile = Profile(player_name)



# -----------------------------
# Level Menu
# -----------------------------

easy = pygame.Rect(
    170,220,260,60
)

hard = pygame.Rect(
    170,310,260,60
)

difficult = pygame.Rect(
    170,400,260,60
)


level=None
speed=None


menu=True



while menu:


    screen.fill(BACKGROUND)

    draw_bow()


    title = font.render(
        "Choose Level 🎀",
        True,
        TEXT
    )


    screen.blit(
        title,
        (130,100)
    )


    draw_button(
        easy,
        "Easy 🌸"
    )


    draw_button(
        hard,
        "Hard 💗"
    )


    draw_button(
        difficult,
        "Difficult 🔥"
    )


    pygame.display.update()



    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            pygame.quit()
            exit()



        if event.type == pygame.MOUSEBUTTONDOWN:


            mouse = pygame.mouse.get_pos()



            if easy.collidepoint(mouse):

                level="Easy"
                speed=EASY
                menu=False



            elif hard.collidepoint(mouse):

                level="Hard"
                speed=HARD
                menu=False



            elif difficult.collidepoint(mouse):

                level="Difficult"
                speed=DIFFICULT
                menu=False





# -----------------------------
# Game
# -----------------------------

snake = Snake()

food = Food()


game_over=False



while True:


    for event in pygame.event.get():


        if event.type == pygame.QUIT:

            pygame.quit()
            exit()



        if event.type == pygame.KEYDOWN:


            if event.key == pygame.K_UP and snake.direction!="DOWN":

                snake.direction="UP"


            elif event.key == pygame.K_DOWN and snake.direction!="UP":

                snake.direction="DOWN"


            elif event.key == pygame.K_LEFT and snake.direction!="RIGHT":

                snake.direction="LEFT"


            elif event.key == pygame.K_RIGHT and snake.direction!="LEFT":

                snake.direction="RIGHT"



            if game_over and event.key==pygame.K_SPACE:

                snake.reset()

                food.random_position()

                profile.reset_score()

                game_over=False





    if not game_over:


        snake.move()



        if (
            snake.body[0][0] == food.x
            and
            snake.body[0][1] == food.y
        ):


            snake.grow()

            food.random_position()

            profile.increase_score()



        if snake.collision():

            game_over=True





    # DRAW

    screen.fill(BACKGROUND)


    draw_bow()

    draw_border()



    food.draw(screen)

    snake.draw(screen)



    # Dashboard

    name_text = small_font.render(
        f"🎀 {profile.name}",
        True,
        TEXT
    )


    score_text = small_font.render(
        f"Score: {profile.score}",
        True,
        TEXT
    )


    best_text = small_font.render(
        f"Best: {profile.best_score}",
        True,
        TEXT
    )


    level_text = small_font.render(
        level,
        True,
        TEXT
    )


    screen.blit(
        name_text,
        (40,30)
    )


    screen.blit(
        score_text,
        (230,30)
    )


    screen.blit(
        best_text,
        (380,30)
    )


    screen.blit(
        level_text,
        (250,65)
    )



    if game_over:


        over = font.render(
            "Game Over 🎀",
            True,
            TEXT
        )


        restart = small_font.render(
            "Press SPACE",
            True,
            TEXT
        )


        screen.blit(
            over,
            (160,350)
        )


        screen.blit(
            restart,
            (220,410)
        )



    pygame.display.update()


    clock.tick(speed)