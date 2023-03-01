import pygame


AMARELO = (255,255,0)
PRETO = (0,0,0)
VELOCIDADE = 1
RAIO = 30

pygame.init()

screen = pygame.display.set_mode((800,600),0)

#classe para desenhar o pacman
class Pacman:
    #criação
    def __init__(self):
        self.centro_x = 400
        self.centro_y = 300
        self.tamanho = 100
        self.raio = int(self.tamanho/2)
        self.vel_x = 1
        self.vel_y = 1

    #metodo calcular regras

    def calcular_regras(self):
        self.centro_x = self.centro_x + self.vel_x
        self.centro_y = self.centro_y + self.vel_y

        if self.centro_x + self.raio > 800:
            self.vel_x = -1

        if self.centro_x - self.raio < 0:
            self.vel_x = 1

        if self.centro_y + self.raio > 600:
            self.vel_y = -1

        if self.centro_y - self.raio < 0:
            self.vel_y = 1            



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


if __name__ == "__main__":
    pacman = Pacman()

    while True:
        #calcular as regras
        screen.fill(PRETO)
        pacman.calcular_regras()

        #pintar a tela
        pacman.pintar(screen)
        pygame.display.update()

        #capturar eventos
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                exit()
