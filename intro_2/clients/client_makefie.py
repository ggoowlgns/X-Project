import socket
import msg

def client(server_addr):
    """Client - using file-like object instead of socket obj"""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(server_addr)       # connect to server process
    in_file = sock.makefile('rb')     # file-like obj
    out_file = sock.makefile('wb')

    sent_bytes = []
    recv_bytes = []
    # for message in msg.msgs(20, max_length=2000):
    #     n_sent = out_file.write(message)
    #     out_file.flush()     # flush-out buffer to send immediately
    #     sent_bytes.append(n_sent)
    #     data = in_file.readline()     # receive response
    #     if not data: break
    #     recv_bytes.append(len(data))

    for line in msg.msgs(20,max_length = 2000):
        message = line.encode()
        n_sent = sock.send(message)
        sent_bytes.append(n_sent)
        data = in_file.readline()
        if not data:break
        recv_bytes.append(len(data))

    sock.close()

    print('sent {} times: {}'.format(len(sent_bytes), sum(sent_bytes)))
    print(sent_bytes)
    print('received {} times: {}'.format(len(recv_bytes), sum(recv_bytes)))
    print(recv_bytes)

if __name__ == '__main__':
    client(('np.hufs.ac.kr', 7))
