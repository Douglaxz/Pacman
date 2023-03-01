import pygame


AMARELO = (255,255,0)
PRETO = (0,0,0)
AZUL = (0,0,255)
VELOCIDADE = 1
RAIO = 30

pygame.init()

screen = pygame.display.set_mode((800,600),0)

#classe para desenhar o cenario

class Cenario:
    def __init__(self, tamanho, pac):
        self.pacman = pac
        self.tamanho = tamanho
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
        for numero_linha, linha in enumerate(self.matriz):
            self.pintar_linha(tela, numero_linha, linha)

    def calcular_regras(self):
        col = self.pacman.coluna_intencao
        lin = self.pacman.linha_intencao
        if 0 <= col <= 28 and 0 <= lin <=29:
            if self.matriz[lin][col] != 2:
                self.pacman.aceitar_movimento()
                if self.matriz[lin][col] == 1:
                    self.pontos +=1
                    self.matriz[lin][col] = 0
                    print(self.pontos)


#classe para desenhar o pacman
class Pacman:
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

    #metodo calcular regras

    def calcular_regras(self):
        self.coluna_intencao = self.coluna + self.vel_x
        self.linha_intencao = self.linha + self.vel_y
        self.centro_x = int(self.coluna * self.tamanho + self.raio)
        self.centro_y = int(self.linha * self.tamanho + self.raio)
          

    #metodo pintar
    def pintar(self, tela):
        #desenhar corpo do pacman   
        pygame.draw.circle(tela,AMARELO,(self.centro_x,self.centro_y),self.raio,0)

        #desenhar boca
        canto_boca = (self.centro_x,self.centro_y)
        labio_superior = (self.centro_x + self.raio,self.centro_y - self.raio)
        labio_inferior = (self.centro_x + self.raio,self.centro_y)
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

    #processar eventos com o mouse
    def processar_eventos_mouse(self,eventos):
        delay = 100
        for e in eventos: 
            if e.type == pygame.MOUSEMOTION:
                mouse_x, mouse_y = e.pos
                self.coluna = (mouse_x - self.centro_x)/delay
                self.linha = (mouse_y - self.centro_y)/delay
    
    def aceitar_movimento(self):
        self.linha = self.linha_intencao
        self.coluna = self.coluna_intencao

                



if __name__ == "__main__":
    size = (600// 30)
    pacman = Pacman(size)
    cenario = Cenario(size, pacman)

    while True:
        #calcular as regras
        pacman.calcular_regras()
        cenario.calcular_regras()


        #pintar a tela
        screen.fill(PRETO)
        cenario.pintar(screen)
        pacman.pintar(screen)
        pygame.display.update()
        pygame.time.delay(100)
        

        #capturar eventos
        eventos = pygame.event.get()
        for e in eventos:
            if e.type == pygame.QUIT:
                exit()
        pacman.processar_eventos(eventos)
        #pacman.processar_eventos_mouse(eventos)