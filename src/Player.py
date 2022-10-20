import pygame


vec = pygame.Vector2
pygame.init()

class Player :
    def __init__(self , Game , speed ):

        self.game = Game


        self.image = pygame.Surface((32,32))
        self.image.fill('red')

        self.rect = pygame.Rect((64 , 832, 32 , 32  ))

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
        self.points = 0
        self.del_acc = speed

    def horizontal_movement(self) :
        if self.direction == 1:
            self.acceleration.x =  self.del_acc
        elif self.direction == 0  :
            self.acceleration.x = -self.del_acc

        self.acceleration.x += self.velocity.x * -.1
        self.velocity.x += self.acceleration.x
        self.delpos.x = self.velocity.x + (0.5 * self.acceleration.x)
        self.px = self.rect.x + self.delpos.x
        self.rect.x = round(self.px)

        for i in self.game.GameStateStack[-1].rects :
            if self.rect.colliderect(i) :
                if self.delpos.x > 0 :
                    self.rect.right = i.rect.left
                if self.delpos.x < 0 :
                    self.rect.left = i.rect.right
                # self.direction = not self.direction
                i.apply_effects(self.game)



    def vertical_movement(self) :
        if self.game.gravity :
            self.acceleration.y =  0.3
        else :
            self.acceleration.y = -0.3
        self.velocity.y += self.acceleration.y
        self.delpos.y = self.velocity.y + (0.5 * self.acceleration.y)
        self.rect.y += self.delpos.y

        for i in self.game.GameStateStack[-1].rects :

            if self.rect.colliderect(i) :
                if self.delpos.y > 0 :
                    self.velocity.y = 0
                    self.rect.bottom = i.rect.top
                if self.delpos.y < 0 :
                    self.velocity.y = 0
                    self.rect.top = i.rect.bottom


    def set_speed(self , speed) :
        self.del_acc = speed

    def check_coins(self) :
        for i in self.game.GameStateStack[-1].coins :
            if self.rect.colliderect(i.rect) :
                # print("Cool")
                self.points += 1
                self.game.GameStateStack[-1].coins.remove(i)


    def update(self) :
        self.del_acc = self.game.GameStateStack[-1].speed
        self.horizontal_movement()
        self.vertical_movement()
        self.check_coins()
