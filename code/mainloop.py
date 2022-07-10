
    dt = (clock.tick(60) /1000) * 60
    dt = dt - pause_time
    pause_time = 0 
    # Player1.debug()

    # pause()
    Player1.move(dt) ; Player2.move(dt)
    # platform6.move(700, 1100, 1)

    win.fill((255,255,255))
    platform_group.draw(win)
    player_group.draw(win)
    pygame.transform.scale(win , (1200,700))
    hoho.blit( pygame.transform.scale(win , (hoho.get_width() , hoho.get_height())), (0,0))
    pygame.display.flip()
    for event in pygame.event.get() :
        
        if event.type == pygame.QUIT :
            pygame.quit()
            raise SystemExit(0)
       
        
        if event.type == pygame.KEYDOWN  :
            if event.key == pygame.K_BACKQUOTE :
                command_console(hoho,Player1,Player2)
            if event.key == pygame.K_ESCAPE :
                pause_time = pause(hoho)
                print("pause_time = ",pause_time)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_b :

#the holy line 
            print("Player1",Player1.color)
            print(Player1.rect.topleft , Player1.position , Player1.velocity , Player1.acceleration , sep = "\t")
            print("Player2",Player2.color)
            print(Player2.rect.topleft , Player2.position , Player2.velocity , Player2.acceleration , sep = "\t")
        if event.type == pygame.MOUSEBUTTONDOWN :
            print(pygame.mouse.get_pos())
