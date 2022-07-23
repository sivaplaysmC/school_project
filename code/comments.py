## from rewrite.py
        # self.Player1 = Entity("blue")
        # self.Player1.name = "Player1"
        #
        # self.Player1.jump_key = pygame.K_UP
        # self.Player1.other_player_name = "Player2"
        # self.Player2 = Entity("red")
        # self.Player2.name = "Player2"
        # self.Player2.move_right_key = pygame.K_d
        # self.Player2.move_left_key = pygame.K_a
        # self.Player2.jump_key = pygame.K_w
        # self.Player2.other_player_name = "Player1"
        # self.players = pygame.sprite.Group()
        # self.platforms = pygame.sprite.Group()
        # self.players.add(self.Player1 , self.Player2)
        # self.rect_list = rect_list
        # for i in self.rect_list :
        #     self.platforms.add(Platform(i.x, i.y, i.w, i.h, "black"))
        # self.Player1.collidelist.add(self.Player2 , *self.platforms.sprites())
        # self.Player2.collidelist.add(self.Player1 , *self.platforms.sprites())



            #     if self.event.key == self.Player1.move_left_key :
            #         self.Player1.actions["left"] = True
            #         self.Player1.actions["idle"] = False
            #     elif self.event.key == self.Player1.move_left_key :
            #         self.Player1.actions["right"] = True
            #         self.Player1.actions["idle"] = False
            #     elif self.event.key == self.Player1.jump_key :
            #         self.Player1.actions["left"] = True
            #         self.Player1.actions["idle"] = False
            #     elif self.event.key == self.Player2.move_left_key :
            #         self.Player1.actions["left"] = True
            #         self.Player2.actions["idle"] = False
            #     elif self.event.key == self.Player2.move_left_key :
            #         self.Player1.actions["right"] = True
            #         self.Player2.actions["idle"] = False
            #     elif self.event.key == self.Player2.jump_key :
            #         self.Player1.actions["left"] = True
            #         self.Player2.actions["idle"] = False
            # if self.event.type == pygame.KEYUP :
            #     if self.event.key == self.Player1.move_left_key :
            #         self.Player1.actions["left"] = False
            #         self.Player1.actions["idle"] = True
            #     elif self.event.key == self.Player1.move_left_key :
            #         self.Player1.actions["right"] = False
            #         self.Player1.actions["idle"] = True
            #     elif self.event.key == self.Player1.jump_key :
            #         self.Player1.actions["left"] = False
            #         self.Player1.actions["idle"] = True
            #     elif self.event.key == self.Player2.move_left_key :
            #         self.Player1.actions["left"] = False
            #         self.Player2.actions["idle"] = True
            #     elif self.event.key == self.Player2.move_left_key :
            #         self.Player1.actions["right"] = False
            #         self.Player2.actions["idle"] = True
            #     elif self.event.key == self.Player2.jump_key :
            #         self.Player1.actions["left"] = False
            #         self.Player2.actions["idle"] = True
############################## ### 
