
import socket
import threading, logging

def echo_handler(conn, cli_addr):
    while True:
        try:
            data = conn.recv(1024)  # recv next message on connected socket
            if not data:       # eof when the socket closed
                logging.info('Client closing: {}'.format(cli_addr))
                break
            logging.debug('Received: {}'.format(data))
            conn.send(data)         # send a reply to the client
        except socket.error as e:              # socket.error exception
            logging.exception('socket error: {}'.format(e))
            break
    conn.close()

def echo_server(my_port):   
    """Echo server (iterative)""" 
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # make listening socket
#    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # Reuse port number if used
    sock.bind(('', my_port))        # bind it to server port number
    sock.listen(5)                  # listen, allow 5 pending connects
    logging.info('Server started')
    while True:                     # do forever (until process killed)
        conn, cli_addr = sock.accept()  # wait for next client connect
                                    # conn: new socket, addr: client addr
        logging.info('Connected by {}'.format(cli_addr))
        handler = threading.Thread(target=echo_handler, args=(conn, cli_addr))
        handler.daemon = True      # damonize this thread. i.e will not wait for it.
        handler.start()
        
if __name__ == '__main__':
    logging.basicConfig(filename='', level=logging.INFO)
    echo_server(50007)

