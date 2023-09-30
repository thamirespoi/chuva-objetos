import pygame
from sys import exit

# Inicializa o pygame
pygame.init()

# Cria a tela
tamanho = (960, 540)
tela = pygame.display.set_mode(tamanho)

##
## Importa os arquivos necessários
##

# Carrega o plano de fundo
plano_fundo = pygame.image.load('assets/fundo/Night-Background8.png').convert()
brilhoroxo = pygame.image.load('assets/fundo/Night-Background7.png').convert_alpha()
brilhomarrom = pygame.image.load('assets/fundo/Night-Background6.png').convert_alpha()
estrelamarrom = pygame.image.load('assets/fundo/Night-Background5.png').convert_alpha()
chao = pygame.image.load('assets/fundo/Night-Background3.png').convert_alpha()
pedrachao = pygame.image.load('assets/fundo/Night-Background4.png').convert_alpha()
lua = pygame.image.load('assets/fundo/Night-Background2.png').convert_alpha()
pedraflutuante = pygame.image.load('assets/fundo/Night-Background1.png').convert_alpha()

# Transforma o tamanho da imagem de fundo
plano_fundo = pygame.transform.scale(plano_fundo, tamanho)
brilhoroxo = pygame.transform.scale(brilhoroxo, tamanho)
brilhomarrom = pygame.transform.scale(brilhomarrom, tamanho)
estrelamarrom = pygame.transform.scale(estrelamarrom, tamanho)
chao = pygame.transform.scale(chao, tamanho)
pedrachao = pygame.transform.scale(pedrachao, tamanho)
lua = pygame.transform.scale(lua, tamanho)
pedraflutuante = pygame.transform.scale(pedraflutuante, tamanho)

# Importa o personagem 
jogador_parado_surf = pygame.image.load('assets/jogador/parado/Hero Boy Idle1.png').convert_alpha()
jogador_parado_rect = jogador_parado_surf.get_rect(midbottom = (100, 530))

# Define o Titulo da Janela
pygame.display.set_caption("ChuvaMortal")

# Cria um relógico para controlar os FPS
relogio = pygame.time.Clock()

movimento_personagem = 0

#Loop priincipal do jogo
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    if evento.type == pygame.KEYDOWN:
        if evento.key == pygame.K_RIGHT:
            movimento_personagem = 5

        if evento.key == pygame.K_LEFT:
            movimento_personagem = -5

# Desenha o fundo na tela
    tela.blit(plano_fundo, (0,0))
    tela.blit(brilhoroxo, (0,0))
    tela.blit(brilhomarrom, (0,0))
    tela.blit(estrelamarrom, (0,0))
    tela.blit(chao, (0,0))
    tela.blit(pedrachao, (0,0))
    tela.blit(lua, (0,0))
    tela.blit(pedraflutuante, (0,0))

# Desenha o jogador na tela
    jogador_parado_rect.x += movimento_personagem
    tela.blit(jogador_parado_surf,jogador_parado_rect)
    
    # Atualiza a tela com o conteudo
    pygame.display.update()

    # Define a quantidade de frames por segundo
    relogio.tick(60)

