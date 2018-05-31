import socket, sys
import msg

class Client:
    """Client class with file-like object"""
    def __init__(self, server_addr):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect(server_addr)      # connect to server process
        self.in_file = self.sock.makefile('rb')     # file-like obj 

    def doit(self):
        sent_bytes = []
        recv_bytes = []
        for message in msg.msgs(20, max_length=2000):
            self.sock.sendall(message)
            sent_bytes.append(len(message))
            data = self.in_file.readline() # receive response
            if not data:
                print('Server closing')
                break
            recv_bytes.append(len(data))
        self.sock.close()                    # to send eof to server

        print('sent {} times: {}'.format(len(sent_bytes), sum(sent_bytes)))
        print(sent_bytes)
        print('received {} times: {}'.format(len(recv_bytes), sum(recv_bytes)))
        print(recv_bytes)

if __name__ == '__main__':
    import os

    serv_addr = ('np.hufs.ac.kr', 7)    # default server_addr

    if len(sys.argv) == 3:
        serv_addr = sys.argv[1], int(sys.argv[2])
    elif len(sys.argv) != 1:
        print('Usage: {} host port'.format( os.path.basename(sys.argv[0])))
        sys.exit(1)

    cli = Client(serv_addr)
    cli.doit()
