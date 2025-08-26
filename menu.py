import pygame

def menu_inicial(tela, som_click):
    largura, altura = tela.get_size()
    tela.fill((200, 200, 255))

    fonte_titulo = pygame.font.SysFont('arial', 64)
    titulo = fonte_titulo.render('Confeiteiro', True, (0, 0, 0))
    tela.blit(titulo, (largura // 2 - titulo.get_width() // 2, 100))

    botao_largura, botao_altura = 200, 60
    botao_x = largura // 2 - botao_largura // 2
    botao_y = altura // 2 - botao_altura // 2
    botao_rect = pygame.Rect(botao_x, botao_y, botao_largura, botao_altura)
    pygame.draw.rect(tela, (100, 200, 100), botao_rect)

    fonte_botao = pygame.font.SysFont('arial', 40)
    texto = fonte_botao.render("INICIAR", True, (0, 0, 0))
    tela.blit(texto, (botao_x + botao_largura // 2 - texto.get_width() // 2,
                       botao_y + botao_altura // 2 - texto.get_height() // 2))

    mouse_pos = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()

    if botao_rect.collidepoint(mouse_pos) and mouse_click[0]:
        return True

    return False

