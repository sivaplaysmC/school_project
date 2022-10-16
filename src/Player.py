import pygame


vec = pygame.Vector2

class Player :
    def __init__(self , Game ):

        self.game = Game


        self.image = pygame.Surface((32,32))
        self.image.fill('red')

        self.rect = pygame.Rect((64 , 256, 32 , 32  ))

        self.direction = 1   # 1 for right , 0 for left
        self.position = pygame.Vector2()
        self.delpos = pygame.Vector2(0,0)
        self.alive = True
        self.jumping = False

        self.position = vec(500,500)
        self.delpos = vec(0,0)
        self.velocity = vec(0,0)
        self.acceleration = vec(0,0)
        self.px = float()

    def horizontal_movement(self) :
        if self.direction == 1:
            self.acceleration.x = 0.5
        elif self.direction == 0  :
            self.acceleration.x = -0.5

        self.acceleration.x += self.velocity.x * -.1
        self.velocity.x += self.acceleration.x
        self.delpos.x = self.velocity.x + (0.5 * self.acceleration.x)
        self.px = self.rect.x + self.delpos.x
        self.rect.x = round(self.px)

        for i in self.game.rects :

            if self.rect.colliderect(i) :
                if self.delpos.x > 0 :
                    self.rect.right = i.rect.left
                if self.delpos.x < 0 :
                    self.rect.left = i.rect.right

                i.apply_effects(self.game)

    def vertical_movement(self) :
        if self.game.gravity :
            self.acceleration.y = 0.4
        else :
            self.acceleration.y = -0.4
        self.velocity.y += self.acceleration.y
        self.delpos.y = self.velocity.y + (0.5 * self.acceleration.y)
        self.rect.y += self.delpos.y

        for i in self.game.rects :

            if self.rect.colliderect(i) :
                if self.delpos.y > 0 :
                    self.velocity.y = 0
                    self.rect.bottom = i.rect.top
                if self.delpos.y < 0 :
                    self.velocity.y = 0
                    self.rect.top = i.rect.bottom


    def apply_perks(self , obstacle) :
        if obstacle.collide_action == 'kill' :
            self.alive = False



    def update(self) :
        self.horizontal_movement()
        self.vertical_movement()
