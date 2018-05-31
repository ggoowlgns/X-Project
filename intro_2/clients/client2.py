import socket
import msg

def client(server_addr):
    """Client - with shutdown and receiving more"""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(server_addr)       # connect to server process

    sent_bytes = []
    recv_bytes = []
    for message in msg.msgs(20, max_length=2000):  # generate 20 msgs
        n_sent = sock.send(message)          # send message to server
        sent_bytes.append(n_sent)
        data = sock.recv(1024)      # receive response from server
        if not data:                # check if server terminates abormally
            print('Server closing')
            break
        recv_bytes.append(len(data))
    else: #for문 정상적으로 끝났을떄
        # Now all the messages sent. Terminate outgoing TCP connection.
        sock.shutdown(socket.SHUT_WR) # send eof mark (FIN)
        # Receive the remaining messages
        while True:
            data = sock.recv(1024)
            if  not data: break
            recv_bytes.append(len(data))
    sock.close() # for 문 break으로 나오게될떄

    print('sent {} times: {}'.format(len(sent_bytes), sum(sent_bytes)))
    print(sent_bytes)
    print('received {} times: {}'.format(len(recv_bytes), sum(recv_bytes)))
    print(recv_bytes)

if __name__ == '__main__':
    client(('np.hufs.ac.kr', 7))
