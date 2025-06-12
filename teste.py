
# #Loop principal
# while running:
#     #Eventos de interação do usuário
#     for event in pygame.event.get(): 
#         #Interrupção da execução do jogo
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             exit()

#         #Interações com o teclado
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_ESCAPE:
#                 pygame.quit()

#     screen.fill(Tool.rgb(color['background']))
    
#     #Atualização dos quadros de física (pymunk)
#     space.step(1 / 60)
#     space.debug_draw(draw_options)
    
#     canvas.fill((Tool.rgb(color['background']))) # Fills the entire screen with light blue
#     map.draw_map(canvas)
#     canvas.blit(player_img, player_rect)
#     screen.blit(canvas, (0,0))
    
#     #Display e Taxa de quadros (pygame)
#     pygame.display.flip()
#     #pygame.display.update()
#     clock.tick(60)