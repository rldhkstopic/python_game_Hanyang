import pygame
import settings

BLACK = (0, 0, 0)

class USER():
    def __init__(self, screen):
        self.screen = screen
        self.init_tick = pygame.time.get_ticks()
        self.image = pygame.image.load('./imgs/main_chrt.png').convert_alpha()

        self.frame = 0
        self.status = 'Left'
        self.direction = pygame.math.Vector2()

        self.attack_time = 0
        self.attack_status = 0
        self.attack_cooldown = 100

        self.step_horizon = 0
        self.step_vertical = 0

        self.animation = {
            'Left':[], 'Right':[],
            'Left_idle':[], 'Right_idle':[],
            'Left_attack':[], 'Right_attack':[]}
        self.animation_list = []
        self.animation_step = [6,6,4,4,8,8]
        self.animation_frame = 100

    def get_image(self, hframe, vframe, width, height, scale, colour):
        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(self.image, (0, 0), ((hframe*width), (vframe*height), width, height))
        image = pygame.transform.scale(image, (width*scale, height*scale))
        image.set_colorkey(colour)

        return image

    def animation_set(self):
        count=0
        for lists in range(len(self.animation)):
            self.animation_list.append(list(self.animation.keys())[lists])

        for steps in self.animation_step:
            temp_img_list = []
            for _ in range(steps):
                temp_img_list.append(self.get_image(self.step_horizon, self.step_vertical, 100, 40, 3, BLACK))
                self.step_horizon += 1
            self.step_horizon = 0
            self.step_vertical += 1
            self.animation[self.animation_list[count]] = temp_img_list
            count += 1
        print(self.animation)

    def get_status(self):
        if self.direction.x == 0 and self.direction.y == 0:
            if not 'idle' in self.status and not 'attack' in self.status:
                self.status = self.status + '_idle'
        if self.attack_status:
            self.direction.x = 0
            self.direction.y = 0
            if not 'attack' in self.status:
                if 'idle' in self.status:
                    self.status = self.status.replace('_idle','_attack')
                else:
                    self.status = self.status + '_attack'
        else:
            if 'attack' in self.status:
                self.status = self.status.replace('_attack','')

    def cooldowns(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.init_tick >= self.animation_frame:
            self.frame += 1
            self.init_tick = current_time
            if self.frame >= len(self.animation[self.status]):
                self.frame = 0

        if self.attack_status:
            if current_time - self.attack_time >= self.attack_cooldown:
                self.attack_status = False

    def keydown(self):
        if not self.attack_status:
            keyPressed = pygame.key.get_pressed()
            if keyPressed[pygame.K_LEFT]:
                self.status = 'Left'
                self.direction.x -= 1
                frame = 0
            elif keyPressed[pygame.K_RIGHT] :
                self.status = 'Right'
                self.direction.x += 1
                frame = 0
            else:
                self.direction.x = 0

            if keyPressed[pygame.K_UP]:
                self.status = 'Up'
                self.direction.y -= 1
                frame = 0
            elif keyPressed[pygame.K_DOWN] :
                self.status = 'Down'
                self.direction.y += 1
                frame = 0
            else:
                self.direction.y = 0

            if keyPressed[pygame.K_SPACE]:
                self.attack_status = True
                self.attack_time = pygame.time.get_ticks()

    def update(self):
        self.keydown()
        self.cooldowns()
        self.get_status()
        self.screen.blit(self.animation[self.status][self.frame], (0, 0))
        print(self.status)
