import pygame
import sys
import random
from menu import menu_inicial

pygame.init()

# sons
som_click = pygame.mixer.Sound("assets/mouse-click-sound.mp3")
som_doce = pygame.mixer.Sound("assets/coinmario.mp3")
som_erro = pygame.mixer.Sound("assets/error-notification.mp3")



largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Confeiteiro 🍩")

# fontes
def fonte_emoji(size):
    try:
        return pygame.font.SysFont("Segoe UI Emoji", size)
    except Exception:
        return pygame.font.Font(None, size)

fonte = fonte_emoji(48)
fonte_info = pygame.font.SysFont("Arial", 28)

# jogador
jogador_surface = pygame.image.load("assets/confeiteiro.png")
jogador_surface = pygame.transform.scale(jogador_surface, (100, 100))

PLAYER_W, PLAYER_H = jogador_surface.get_size()
velocidade = 7

# itens
doce1 = pygame.image.load("assets/doce1.png").convert_alpha()
doce1 = pygame.transform.scale(doce1, (80, 80))
doce2 = pygame.image.load("assets/doce2.png").convert_alpha()
doce2 = pygame.transform.scale(doce2, (80, 80))
doce3 = pygame.image.load("assets/doce3.png").convert_alpha()
doce3 = pygame.transform.scale(doce3, (80, 80))
pimenta = pygame.image.load("assets/pimenta.png").convert_alpha()
pimenta = pygame.transform.scale(pimenta, (60, 60))

clock = pygame.time.Clock()

def rodar_menu():
    pygame.mixer.music.load("assets/musica1cortada.wav")
    pygame.mixer.music.play(0)  # toca 1 vez (sem loop)


    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if menu_inicial(tela, som_click):
            pygame.mixer.music.stop()
            return

        pygame.display.update()

def rodar_jogo():
    pygame.mixer.music.load("assets/musica2cortada.wav")
    pygame.mixer.music.play(-1)  # toca em loop infinito


    pontos = 0
    vidas = 5
    itens = []
    jogador_x = largura // 2 - PLAYER_W // 2
    jogador_y = altura - PLAYER_H - 10

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and jogador_x > 0:
            jogador_x -= velocidade
        if keys[pygame.K_RIGHT] and jogador_x < largura - PLAYER_W:
            jogador_x += velocidade

        tela.fill((255, 255, 255))
        tela.blit(jogador_surface, (jogador_x, jogador_y))

        if random.randint(1, 25) == 1:
            tipo = random.choice(["doce", "pimenta"])
            surf = random.choice([doce1, doce2, doce3]) if tipo == "doce" else pimenta
            itens.append([random.randint(0, largura - surf.get_width()), -surf.get_height(), surf, tipo])

        for item in itens:
            tela.blit(item[2], (item[0], item[1]))
            item[1] += 5

        itens = [i for i in itens if i[1] < altura]

        jogador_rect = pygame.Rect(jogador_x, jogador_y, PLAYER_W, PLAYER_H)
        for item in itens[:]:
            IW, IH = item[2].get_size()
            item_rect = pygame.Rect(item[0], item[1], IW, IH)
            if jogador_rect.colliderect(item_rect):
                if item[3] == "doce":
                    pontos += 1
                    som_doce.play()
                else:
                    vidas -= 1
                    som_erro.play()
                itens.remove(item)


        texto = fonte_info.render(f"Pontos: {pontos}   Vidas: {vidas}", True, (0, 0, 0))
        tela.blit(texto, (10, 10))

        if vidas <= 0:
            tela.fill((0, 0, 0))
            game_over = fonte_info.render("GAME OVER", True, (255, 0, 0))
            tela.blit(game_over, (largura // 2 - game_over.get_width() // 2,
                                  altura // 2 - game_over.get_height() // 2))
            pygame.display.update()
            pygame.time.delay(2000)
            return

        pygame.display.update()
        clock.tick(60)

while True:
    rodar_menu()
    rodar_jogo()
