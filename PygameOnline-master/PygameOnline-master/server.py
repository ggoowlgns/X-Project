HOST = '172.20.10.4'
PORT = 12800

import socket, sys
from threading import Thread
import pickle

class ThreadClient(Thread):
    def __init__(self, conn):
        Thread.__init__(self)
        self.connection = conn
        self.resend = True
    def run(self):
        nom = self.getName()
        while 1:
            msgClient = self.connection.recv(1024)
            try:
                msgClient = pickle.loads(msgClient)
            except:
                self.resend = False
            else:
                self.resend = True



            msgEnvoi = pickle.dumps(msgClient)

            if self.resend == True:
                for cle in conn_client:
                    if cle != nom:
                        conn_client[cle].send(msgEnvoi)


        self.connection.close()
        del conn_client[nom]
        print("Client {} connected ".format(nom))



mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    mySocket.bind((HOST, PORT))
except socket.error:
    print("Error")
    sys.exit()
print("Server opened 성공")
mySocket.listen(5)

conn_client = {}
while 1:
    connection, adresse = mySocket.accept()
    th = ThreadClient(connection)
    th.start()
    it = th.getName()
    conn_client[it] = connection
    print("Client {0} connected, addresse IP : {1}, port  : {2}".format(it, adresse[0], adresse[1]))
    connection.send(b"Connected.")