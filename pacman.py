import pygame
import random
from abc import ABCMeta, abstractmethod
from pygame import mixer 

AMARELO = (255,255,0)
PRETO = (0,0,0)
AZUL = (0,0,255)
VERMELHO = (255,0,0)
VERDE = (0,255,0)
BRANCO = (255,255,255)
ROSA =  (255,15,192)
LARANJA = (255,140,0)
CIANO = (0,255,255)
VELOCIDADE = 1
RAIO = 30

ACIMA = 1
ABAIXO = 2
DIREITA = 3
ESQUERDA = 4


pygame.init()

screen = pygame.display.set_mode((800,600),0)
pygame.display.set_caption('P A C M A N - DOUGLAS AMARAL')
img = pygame.image.load('pacman.png')
pygame.display.set_icon(img)
fonte = pygame.font.SysFont("arial", 24, True, False)
pygame.mixer.pre_init(44100, -16, 1, 512)
mixer.init()
mixer.music.load("pacman_chomp.wav") 
#mixer.music.load("pacman_death.wav") 
mixer.music.set_volume(0.7)

#classe para desenhar o cenario

#*****************************************************************************************************************
# ELEMENTO JOGO - CLASSE GENERALISTA
#*****************************************************************************************************************
class ElementoJogo(metaclass=ABCMeta):
    @abstractmethod
    def pintar(self, tela):
        pass

    @abstractmethod
    def calcular_regras(self):
        pass
    
    @abstractmethod
    def processar_eventos(self, eventos):
        pass

#*****************************************************************************************************************
# MOVIVEL
#*****************************************************************************************************************
class Movivel(metaclass=ABCMeta):
    @abstractmethod
    def aceitar_movimento(self):
        pass

    @abstractmethod
    def recusar_movimento(self, direcoes):
        pass

    @abstractmethod
    def aceitar_movimento(self, direcoes):
        pass

#*****************************************************************************************************************
# CENARIO
#*****************************************************************************************************************

class Cenario(ElementoJogo):
    def __init__(self, tamanho, pac):
        self.pacman = pac
        self.moviveis = []
        self.tamanho = tamanho
        self.estado = 0
        #Estados: 0 - JOGANDO | 1 - PAUSADO | 2 - GAMEOVER | 3 - GANHOU
        self.vidas = 5
        self.pontos = 0

        self.matriz = [
            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
            [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2],
            [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2],
            [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2],
            [2, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 0, 0, 0, 0, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 0, 0, 0, 0, 0, 0, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 2, 0, 0, 0, 0, 0, 0, 2, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 0, 0, 0, 0, 0, 0, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 2],
            [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2],
            [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2],
            [2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
        ]

    def adicionar_movivel(self, obj):
        self.moviveis.append(obj)


    def pintar_score(self, tela):
        pontos_x = 30 * self.tamanho
        pontos_img = fonte.render("Score: {}".format(self.pontos), True, AMARELO)
        tela.blit(pontos_img, (pontos_x, 50))
        vidas_img =  fonte.render("Vidas: {}".format(self.vidas), True, AMARELO)
        tela.blit(vidas_img, (pontos_x, 100))


    def pintar_linha(self, tela, numero_linha, linha):
        for numero_coluna, coluna in enumerate(linha):
            x = numero_coluna * self.tamanho
            y = numero_linha * self.tamanho
            cor = PRETO
            half = self.tamanho // 2
            if coluna == 2:
                cor = AZUL 
            pygame.draw.rect(tela,cor,(x, y , self.tamanho, self.tamanho),0)
            if coluna == 1:
                cor = AMARELO 
            pygame.draw.circle(tela,cor,(x + half, y + half) , self.tamanho//10,0)            

    def pintar(self, tela):
        if self.estado ==0:
            self.pintar_jogando(tela)
        elif self.estado == 1:
            self.pintar_jogando(tela)
            self.pintar_pausado(tela)
        elif self.estado == 2:
            self.pintar_jogando(tela)
            self.pintar_gameover(tela)        
        elif self.estado == 3:
            self.pintar_jogando(tela)
            self.pintar_vitoria(tela)                    
    
    def pintar_vitoria(self, tela):
        self.pintar_texto_centro(tela, "P A R A B E N S  V O C E   V E N C E U") 

    def pintar_texto_centro(self, tela, texto):
        texto_img = fonte.render(texto, True, AMARELO)
        texto_x = (tela.get_width() - texto_img.get_width()) // 2
        texto_y = (tela.get_height() - texto_img.get_height()) // 2
        tela.blit(texto_img,(texto_x,texto_y))


    def pintar_pausado(self, tela):
        self.pintar_texto_centro(tela, "P A U S A D O") 

    def pintar_jogando(self, tela):
        for numero_linha, linha in enumerate(self.matriz):
            self.pintar_linha(tela, numero_linha, linha)
        self.pintar_score(tela)

    def pintar_gameover(self, tela):
        self.pintar_texto_centro(tela, "G A M E   O V E R")


    def get_direcoes(self, linha, coluna):
        direcoes = []
        if self.matriz[int(linha - 1)][int(coluna)] != 2:
            direcoes.append(ACIMA)

        if self.matriz[int(linha + 1)][int(coluna)] != 2:
            direcoes.append(ABAIXO)

        if self.matriz[int(linha)][int(coluna - 1)] != 2:
            direcoes.append(ESQUERDA)       

        if self.matriz[int(linha)][int(coluna + 1)] != 2:
            direcoes.append(DIREITA)
        return direcoes

    def calcular_regras(self):
        if self.estado  == 0:
            self.calcular_regras_jogando()
        elif self.estado == 1:
            self.calcular_regras_pausado()
        elif self.estado == 2:
            self.calcular_regras_gameover()            
    
    def calcular_regras_pausado(self):
        pass

    def calcular_regras_gameover(self):
        pass

    def calcular_regras_jogando(self):
        for movivel in self.moviveis:
            lin = int(movivel.linha)
            col = int(movivel.coluna)
            lin_intencao = int(movivel.linha_intencao)
            col_intencao = int(movivel.coluna_intencao)
            direcoes = self.get_direcoes(lin, col)
            if len(direcoes) >= 3:
                movivel.esquina(direcoes)
                if isinstance(movivel, Pacman):
                    mixer.music.play()                
            if isinstance(movivel, Fantasma) and movivel.linha == self.pacman.linha and movivel.coluna == self.pacman.coluna:
                self.vidas -= 1
                if self.vidas <=0:
                    self.estado = 2
                else:
                    self.pacman.linha = 1
                    self.pacman.coluna = 1

            else:
                if 0 <= col_intencao <28 and 0 <= lin_intencao < 29 and self.matriz[lin_intencao][col_intencao] != 2:
                    movivel.aceitar_movimento()

                    if isinstance(movivel, Pacman) and self.matriz[lin][col] == 1:
                        self.pontos += 1
                        self.matriz[lin][col] = 0
                        if self.pontos >= 306:
                            self.estado = 3
                else:
                    movivel.recusar_movimento(direcoes)




    
    def processar_eventos(self,evt):
        for e in evt:
            if e.type == pygame.QUIT:
                exit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_p:
                    if self.estado ==0:
                        self.estado = 1
                    else:
                        self.estado = 0
  

    #processar eventos com o mouse
    def processar_eventos_mouse(self,eventos):
        delay = 100
        for e in eventos: 
            if e.type == pygame.MOUSEMOTION:
                mouse_x, mouse_y = e.pos
                self.coluna = (mouse_x - self.centro_x)/delay
                self.linha = (mouse_y - self.centro_y)/delay
                
         

#*****************************************************************************************************************
# PACMAN
#*****************************************************************************************************************
class Pacman(ElementoJogo, Movivel):
    #criação
    def __init__(self, tamanho):
        self.centro_x = 400
        self.centro_y = 300
        self.tamanho = tamanho
        self.raio = int(self.tamanho/2)
        self.vel_x = 0
        self.vel_y = 0
        self.coluna = 1
        self.linha = 1
        self.coluna_intencao = self.coluna
        self.linha_intencao = self.linha
        self.abertura = 0
        self.velocidade_abertura = 1

    #metodo calcular regras

    def calcular_regras(self):
        self.coluna_intencao = self.coluna + self.vel_x
        self.linha_intencao = self.linha + self.vel_y
        self.centro_x = int(self.coluna * self.tamanho + self.raio)
        self.centro_y = int(self.linha * self.tamanho + self.raio)
          

    #metodo pintar
    def pintar(self, tela):
        self.abertura += self.velocidade_abertura
        if self.abertura > self.raio:
            self.velocidade_abertura = -1
        if self.abertura <= 0:
            self.velocidade_abertura = 1

        #desenhar corpo do pacman   
        pygame.draw.circle(tela,AMARELO,(self.centro_x,self.centro_y),self.raio,0)

        #desenhar boca
        canto_boca = (self.centro_x,self.centro_y)
        labio_superior = (self.centro_x + self.raio,self.centro_y - self.abertura)
        labio_inferior = (self.centro_x + self.raio,self.centro_y + self.abertura)
        pontos = [canto_boca, labio_superior, labio_inferior]
        pygame.draw.polygon(tela,PRETO, pontos,0)

        #desenhar olho
        olho_x = int(self.centro_x + self.raio/3)
        olho_y = int(self.centro_y - self.raio*0.70)
        olho_raio = int(self.raio / 10)
        pygame.draw.circle(tela,PRETO,(olho_x,olho_y),olho_raio,0)
    
    #processar eventos com o teclado
    def processar_eventos(self,eventos):
        for e in eventos:         
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RIGHT:
                    self.vel_x = VELOCIDADE
                elif e.key == pygame.K_LEFT:
                    self.vel_x = -VELOCIDADE    
                elif e.key == pygame.K_DOWN:
                    self.vel_y = VELOCIDADE                                      
                elif e.key == pygame.K_UP:
                    self.vel_y = -VELOCIDADE                                                          
            if e.type == pygame.KEYUP:
                if e.key == pygame.K_RIGHT:
                    self.vel_x = 0       
                elif e.key == pygame.K_LEFT:
                    self.vel_x = 0 
                elif e.key == pygame.K_DOWN:
                    self.vel_y = 0   
                elif e.key == pygame.K_UP:
                    self.vel_y = 0      
   
    def aceitar_movimento(self):
        self.linha = self.linha_intencao
        self.coluna = self.coluna_intencao
    
    def recusar_movimento(self, direcoes):
        self.linha_intencao = self.linha
        self.coluna_intencao = self.coluna
    
    def esquina(self, direcoes):
        pass
    
#*****************************************************************************************************************
# FANTASMA
#*****************************************************************************************************************
class Fantasma(ElementoJogo):
    def __init__(self,cor,tamanho):
        self.coluna = 13.0
        self.linha = 15.0
        self.linha_intencao = self.linha
        self.coluna_intencao = self.coluna
        self.velocidade = 1
        self.direcao = ABAIXO
        self.tamanho = tamanho
        self.cor = cor

    def pintar(self, tela):
        fatia = self.tamanho // 8
        px = int(self.coluna * self.tamanho)
        py = int(self.linha * self.tamanho)
        contorno = [(px, py + self.tamanho),
                    (px + fatia * 1, py + fatia * 2),
                    (px + fatia * 2, py + fatia // 2),
                    (px + fatia * 3, py),
                    (px + fatia * 5, py),
                    (px + fatia * 6, py + fatia // 2),
                    (px + fatia * 7, py + fatia * 2),
                    (px + self.tamanho, py + self.tamanho)
                    ]
        pygame.draw.polygon(tela,self.cor, contorno,0)

        olho_raio_ext = fatia
        olho_raio_int = fatia //2

        olho_e_x = int(px + fatia * 2.5)
        olho_e_y = int(py + fatia * 2.5)

        olho_d_x = int(px + fatia * 5.5)
        olho_d_y = int(py + fatia * 2.5)        

        pygame.draw.circle(tela,BRANCO,(olho_e_x,olho_e_y),olho_raio_ext,0)
        pygame.draw.circle(tela,PRETO,(olho_e_x,olho_e_y),olho_raio_int,0)

        pygame.draw.circle(tela,BRANCO,(olho_d_x,olho_d_y),olho_raio_ext,0)
        pygame.draw.circle(tela,PRETO,(olho_d_x,olho_d_y),olho_raio_int,0)        

    def calcular_regras(self):
        if self.direcao == ACIMA:
            self.linha_intencao =  self.linha - self.velocidade
        elif self.direcao == ABAIXO:
            self.linha_intencao =  self.linha + self.velocidade
        elif self.direcao == ESQUERDA:
            self.coluna_intencao =  self.coluna - self.velocidade
        elif self.direcao == DIREITA:
            self.coluna_intencao =  self.coluna + self.velocidade 
            
    def mudar_direcao(self, direcoes):
        self.direcao = random.choice(direcoes)

    def esquina(self,direcoes):
        self.mudar_direcao(direcoes)

    
    def aceitar_movimento(self):
        self.linha = self.linha_intencao
        self.coluna = self.coluna_intencao

    def recusar_movimento(self,direcoes):
        self.linha_intencao = self.linha
        self.coluna_intencao = self.coluna
        self.mudar_direcao(direcoes)

    def processar_eventos(self):
        pass
        
#*****************************************************************************************************************
# codigo principal
#*****************************************************************************************************************

if __name__ == "__main__":
    size = (600// 30)
    pacman = Pacman(size)
    blinky = Fantasma(VERMELHO, size)
    inky = Fantasma(CIANO, size)
    clyde = Fantasma(LARANJA, size)
    pinky = Fantasma(ROSA, size)
    cenario = Cenario(size, pacman)
    cenario.adicionar_movivel(pacman)
    cenario.adicionar_movivel(blinky)
    cenario.adicionar_movivel(inky)
    cenario.adicionar_movivel(clyde)
    cenario.adicionar_movivel(pinky)

    

    while True:
        #calcular as regras
        pacman.calcular_regras()
        blinky.calcular_regras()
        inky.calcular_regras()
        clyde.calcular_regras()
        pinky.calcular_regras()
        cenario.calcular_regras()

        #pintar a tela
        screen.fill(PRETO)
        cenario.pintar(screen)
        blinky.pintar(screen)
        inky.pintar(screen)
        pinky.pintar(screen)
        clyde.pintar(screen)
        pacman.pintar(screen)
        pygame.display.update()
        pygame.time.delay(100)
        

        #capturar eventos
        eventos = pygame.event.get()
        pacman.processar_eventos(eventos)
        cenario.processar_eventos(eventos)
        #pacman.processar_eventos_mouse(eventos)