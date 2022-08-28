import pygame
import player

pygame.init()

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('SpriteTest')

user_image = pygame.image.load('main_chrt.png').convert_alpha()
users = player.USER(user_image)

BackGround = (50, 50, 50)
BLACK = (0, 0, 0)

animation_list = []
animation_steps = [6,6,4,4,8,8]   # leftside, rightside step is 6
animation_perms = 100  # animation per milisecond
animation_status = 0
update_last = pygame.time.get_ticks()
frame = 0
action = 0
step_counter = 0
step_counter_vertical = 0



for animation in animation_steps:
    temp_img_list = []
    for _ in range(animation):
        temp_img_list.append(users.get_image(step_counter, step_counter_vertical, 100, 40, 3, BLACK))
        step_counter += 1
    step_counter=0
    step_counter_vertical += 1 #
    animation_list.append(temp_img_list)

run = True
while run:
    #update Background
    screen.fill(BackGround)

    #update Animation
    current_time = pygame.time.get_ticks()
    if current_time - update_last >= animation_perms:
        frame += 1
        update_last = current_time
        if frame >= len(animation_list[action]):
            frame = 0

    screen.blit(animation_list[action][frame], (0, 0)) #show frame image

    keyPressed = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if keyPressed[pygame.K_LEFT] :
                action = 0
                frame = 0
            # else:
            #     action = 3
            #     frame = 0

            elif keyPressed[pygame.K_RIGHT] :
                action = 1
                frame = 0
            else:
                action = 3
                frame = 0

            if keyPressed[pygame.K_LCTRL] :
                action = 4
                frame = 0


    print(action)
    pygame.display.update()

pygame.quit()
