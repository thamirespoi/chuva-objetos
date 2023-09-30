import pygame
from sys import exit
import random 
from random import randint, choice

def animacao_rochas():
    global movimento_rochas

    if pedraflutuante_rect.y <= -20:
        movimento_rochas = 1
    elif pedraflutuante_rect.y >= 20:
        movimento_rochas = -1
    
    pedraflutuante_rect.y += movimento_rochas

    tela.blit(pedraflutuante, pedraflutuante_rect)

def animacao_estrelas():
    global index_estrelas
    index_estrelas += 0.03

    if (index_estrelas >= 4):
        index_estrelas = 0
    
    if (int(index_estrelas) == 0):
        tela.blit(brilhoroxo, (0, 0))
    elif (int(index_estrelas) == 1):
        tela.blit(brilhomarrom, (0, 0))
    else:
        tela.blit(estrelamarrom, (0, 0))

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

def adicionar_objeto():
    global lista_chuva_objeto

    objetos_lista_aleatoria = ['Coracao'] * 10 + ['Moeda'] * 10 + ['Projetil'] * 80
    tipo_objeto = choice(objetos_lista_aleatoria)

    posicao = (randint(10,950), randint(-100,0))
    velocidade = randint(5,10)

    if tipo_objeto == 'Projetil':
        objeto_rect = projetil_surfaces[0].get_rect(center = posicao)
    elif tipo_objeto == 'Coracao':
        objeto_rect = coracao_surfaces[0].get_rect(center = posicao)
    elif tipo_objeto == 'Moeda':
        objeto_rect = moeda_surfaces[0].get_rect(center = posicao)

    lista_chuva_objeto.append({
        'tipo': tipo_objeto,
        'retangulo': objeto_rect,
        'velocidade': velocidade
    })

def movimento_objetos_chuva():
    global lista_chuva_objeto

    for objeto in lista_chuva_objeto:

        objeto['retangulo'].y += objeto['velocidade']

        if objeto['tipo'] == 'Projetil':
            tela.blit(projetil_surfaces[projetil_index], objeto['retangulo'])
        elif objeto['tipo'] == 'Coracao':
            tela.blit(coracao_surfaces[coracao_index], objeto['retangulo'])
        elif objeto['tipo'] == 'Moeda':
            tela.blit(moeda_surfaces[moeda_index], objeto['retangulo'])
        
        if objeto['retangulo'].y > 540:
            lista_chuva_objeto.remove(objeto)



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
pedraflutuante_rect = pedraflutuante.get_rect(topleft = (0, 0))

index_estrelas = 0
movimento_rochas = 1

## Personagem

jogador_index = 0
# Carrega as imagens do personagem parado
jogador_parado_surfaces = []
for imagem in range(1, 14):
    img = pygame.image.load(f'assets/jogador/parado/Hero Boy Idle{imagem}.png').convert_alpha()
    jogador_parado_surfaces.append(img)

# Carrega as imagens do personagem voando
jogador_voando_surfaces = []
for imagem in range(1, 9):
    img = pygame.image.load(f'assets/jogador/voar/Hero Boy Fly{imagem}.png').convert_alpha()
    jogador_voando_surfaces.append(img)

jogador_surfaces_rect = jogador_parado_surfaces[jogador_index].get_rect(center = (100, 430))

## Objetos 

lista_chuva_objeto = []
# Carrega as imagens do projetil
projetil_surfaces = []
projetil_index = 0
for imagem in range(1, 4):
    img = pygame.image.load(f'assets/objetos/projetil/Hero Bullet{imagem}.png').convert_alpha()
    projetil_surfaces.append(img)

# Carrega as imagens do coração
coracao_surfaces = []
coracao_index = 0
for imagem in range(1, 4):
    img = pygame.image.load(f'assets/objetos/coracao/Heart{imagem}.png').convert_alpha()
    img = pygame.transform.scale(img, (80,80))
    coracao_surfaces.append(img)

# Carrega as imagens do moeda
moeda_surfaces = []
moeda_index = 0
for imagem in range(1, 5):
    img = pygame.image.load(f'assets/objetos/moeda/Coin-A{imagem}.png').convert_alpha()
    img = pygame.transform.scale(img, (80,80))
    moeda_surfaces.append(img)


# Cria um relógico para controlar os FPS
relogio = pygame.time.Clock()

# Controla se o personagem está andando (negativo esquerda, positivo direita)
movimento_personagem = 0
direcao_personagem = 0
movimento_objeto = 0

# Cria um evento para adicionar um objeto na tela
novo_objeto_timer = pygame.USEREVENT + 1
pygame.time.set_timer(novo_objeto_timer, 500)

#Loop principal do jogo
while True:
    ## EVENTOS
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()
    
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_RIGHT:
                movimento_personagem = 5
                direcao_personagem = 1

            if evento.key == pygame.K_LEFT:
                movimento_personagem = -5
                direcao_personagem = 0

            if evento.key == pygame.K_DOWN:
                movimento_personagem = 0
        
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_RIGHT:
                movimento_personagem = 0
            
            if evento.key == pygame.K_LEFT:
                movimento_personagem = 0

        if evento.type == novo_objeto_timer:
            adicionar_objeto()


# Desenha o fundo na tela
    tela.blit(plano_fundo, (0,0))

    animacao_estrelas()

    tela.blit(chao, (0,0))
    tela.blit(pedrachao, (0,0))
    tela.blit(lua, (0,0))

    animacao_rochas()
    

# Faz a chamada da função animação do personagem
    animacao_personagem()

    movimento_objetos_chuva()

# Atualiza a tela com o conteudo
    pygame.display.update()

# Define a quantidade de frames por segundo
    relogio.tick(60)

