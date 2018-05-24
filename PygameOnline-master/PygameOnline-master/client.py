import socket, sys
import pickle
from threading import Thread
import pygame

#addfdsfsdfsf
host = "192.168.0.9"
port = 12800

#test
#chaf
#hihi
class Affichage:
    def __init__(self):
        self.perso = pygame.Surface((32, 32))
        self.perso.fill((255, 0, 0))
        self.pos_perso = self.perso.get_rect()
        self.screen = pygame.display.set_mode((640, 480))
        self.perso2 = pygame.Surface((32, 32))
        self.perso2.fill((0, 255, 0))


    def replacer(self, direction):
        if direction == "up":
            self.pos_perso = self.pos_perso.move(0, -3)
        if direction == "down":
            self.pos_perso = self.pos_perso.move(0, 3)
        if direction == "left":
            self.pos_perso = self.pos_perso.move(-3, 0)
        if direction == "right":
            self.pos_perso = self.pos_perso.move(3, 0)

    def afficher(self):
        self.screen.fill((255, 255, 255))
        try:
            self.screen.blit(self.perso2, self.pos_perso2)
        except:
            self.screen.blit(self.perso2, (0, 0))
        self.screen.blit(self.perso, self.pos_perso)
        pygame.display.flip()


class EnvoiMessage(Thread):
    def __init__(self, conn):
        Thread.__init__(self)
        self.connection = conn

    def run(self):
        while 1:
            msg_envoi = pickle.dumps(affichage.pos_perso)
            self.connection.send(msg_envoi)

    def stop(self):
        self._stop.set()

class responseMessage(Thread):
    def __init__(self, co):
        Thread.__init__(self)
        self.connection = co

    def run(self):
        while 1:
            msg_recu = self.connection.recv(1024)
            try:
                msg_recu = pickle.loads(msg_recu)
                print(msg_recu)
                affichage.pos_perso2 = msg_recu
            except:
                pass

    def stop(self):
        self._stop.set()

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    connection.connect((host, port))
except socket.error:
    print("Error")
    sys.exit()
print("Connected")

th1 = EnvoiMessage(connection)
th2 = responseMessage(connection)
affichage = Affichage()

th1.start()
th2.start()

pygame.key.set_repeat(10)
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                affichage.replacer("down")
            if event.key == pygame.K_UP:
                affichage.replacer("up")
            if event.key == pygame.K_RIGHT:
                affichage.replacer("right")
            if event.key == pygame.K_LEFT:
                affichage.replacer("left")
            if event.key == pygame.K_q:
                th1.stop()
                th2.stop()
                th1.join()
                th2.join()
                connection.close()
                sys.exit()
    affichage.afficher()



