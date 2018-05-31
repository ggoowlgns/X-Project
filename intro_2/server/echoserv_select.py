'''
Created on 2015. 5. 25.

@author: JPHONG
'''
"""I/O Multiplexing echo server"""
import socket
import select

def server(my_port):
    """I/O Mulitplexing Server"""    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(('', my_port))
    sock.listen(5)
    read_socks = [sock]
    print('Server starting')
    while True:
        readables, _, _ = select.select(read_socks, [], [])
        for s in readables:
            if s is sock: # listening socket
                conn, addr = sock.accept()
                read_socks.append(conn)
                print('Connected by {}'.format(addr))
            else:               # connected socket
                try:
                    data = s.recv(1024)
                    if data:    # data received
                        print('Received from {}:\n'.format(addr), data)
                        s.sendall(data)
                    else:
                        print('Client closing', addr)
                        s.close()
                        read_socks.remove(s)
                except socket.error as e:
                    print('socket error:', e)
                    s.close()
                    read_socks.remove(s)

if __name__ == '__main__':
    server(50007)

    