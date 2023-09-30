import pygame
from sys import exit

def animacao_personagem():
    global jogador_index
    # Calcula o movimento do personagem
    jogador_surfaces_rect.x += movimento_personagem

    if movimento_personagem == 0:
        jogador_surfaces = jogador_parado_surfaces
    else:
        jogador_surfaces = jogador_voando_surfaces
    
    # Avança para o proximo frame
    jogador_index += 0.15

    if jogador_index > len(jogador_surfaces) - 1:
        jogador_index = 0
    
    if direcao_personagem == 1:
        jogador_flipando = pygame.transform.flip(jogador_surfaces[int(jogador_index)], True, False)
    else:
        jogador_flipando = jogador_surfaces[int(jogador_index)]

# Desenha o jogador na tela 
    tela.blit(jogador_flipando, jogador_surfaces_rect)

# Inicializa o pygame
pygame.init()

# Cria a tela
tamanho = (960, 540)
tela = pygame.display.set_mode(tamanho)

# Define o Titulo da Janela
pygame.display.set_caption("ChuvaMortal")

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

#----------------------------------------------------------------------------------------
jogador_index = 0
jogador_parado_surfaces = []
jogador_voando_surfaces = []

# Carrega as imagens do personagem parado
for imagem in range(1, 14):
    img = pygame.image.load(f'assets/jogador/parado/Hero Boy Idle{imagem}.png').convert_alpha()
    jogador_parado_surfaces.append(img)

# Carrega as imagens do personagem voando
for imagem in range(1, 9):
    img = pygame.image.load(f'assets/jogador/voar/Hero Boy Fly{imagem}.png').convert_alpha()
    jogador_voando_surfaces.append(img)

jogador_surfaces_rect = jogador_parado_surfaces[jogador_index].get_rect(center = (100, 430))

# Cria um relógico para controlar os FPS
relogio = pygame.time.Clock()

# Controla se o personagem está andando (negativo esquerda, positivo direita)
movimento_personagem = 0
direcao_personagem = 0

#Loop principal do jogo
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()
    
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_RIGHT:
                movimento_personagem = 4
                direcao_personagem = 1

            if evento.key == pygame.K_LEFT:
                movimento_personagem = -4
                direcao_personagem = 0

            if evento.key == pygame.K_DOWN:
                movimento_personagem = 0
        
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_RIGHT:
                movimento_personagem = 0
            
            if evento.key == pygame.K_LEFT:
                movimento_personagem = 0

# Desenha o fundo na tela
    tela.blit(plano_fundo, (0,0))
    tela.blit(brilhoroxo, (0,0))
    tela.blit(brilhomarrom, (0,0))
    tela.blit(estrelamarrom, (0,0))
    tela.blit(chao, (0,0))
    tela.blit(pedrachao, (0,0))
    tela.blit(lua, (0,0))
    tela.blit(pedraflutuante, (0,0))

# Faz a chamada da função animação do personagem
    animacao_personagem()

# Atualiza a tela com o conteudo
    pygame.display.update()

# Define a quantidade de frames por segundo
    relogio.tick(60)

