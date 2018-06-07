"""Iterative echo server"""
import sys
from socket import *
from threading import Thread
import MySQLdb
my_ip = "192.168.0.11"
data = "type:load\r\ntime:(현재시각)\r\ntemperature:(평균온도)\r\n"

class temp_time():
    def __init__(self,data):
        self.time = (data.split(":")[2]+':'+data.split(":")[3]+':'+data.split(":")[4]).split("\r")[0]
        self.temp = data.split(":")[5].split("\r")[0]

class myThread(Thread):
    def __init__(self,connection):
        Thread.__init__(self)
        self.connection = connection
        self.resend = True
    def run(self):
        try:
            while True:
                data = self.connection.recv(1024)  # recv next message on connected socket


                if not data: break  # eof when the socket closed
                print('Server received:', data.decode())
                data =data.decode()
                if "load" in data:
                    te = temp_time(data)
                    reciveTemp(te.time,te.temp)
                    print(te.time,te.temp)
                    self.connection.send("200 OK".encode("utf-8"))  # send a reply to the client
                if "get" in data:
                    temp_value = sendTemp((data.split(":")[2]+':'+data.split(":")[3]+':'+data.split(":")[4]).split("\r")[0])
                    sendmsg = "300 OK" +"\n" +temp_value
                    self.connection.send(sendmsg.encode("utf-8"))  # send a reply to the client
        except OSError as e:  # socket.error exception
            print('socket error:', e)
        except Exception as e:
            print('Exception:', e)



def echo_server(my_port):   
    """Echo server (iterative)"""
    try:
        sock = socket(AF_INET, SOCK_STREAM) # make listening socket
        sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1) # Reuse port number if used
        sock.bind(('', my_port))        # bind it to server port number
        sock.listen(5)                  # listen, allow 5 pending connects


    except OSError as e:
        print('socket error', e)
        sock.close()
        sys.exit(1)
    else:
        print('Server started')

        while True:  # do forever (until process killed)
            conn, cli_addr = sock.accept()  # wait for next client connect
            # conn: new socket, addr: client addr
            print('Connected by', cli_addr)
            th = myThread(conn)
            th.start()

#받는 형태 :“type:load\r\ntime:(현재시각)\r\ntemperature:(평균온도)\r\n
def reciveTemp(time,temp):
    connection = MySQLdb.connect(host=my_ip,
                                 user="root",
                                 passwd="root",
                                 db="xproj")

    cursor = connection.cursor()

    staff_data = [(time, temp) ]

    for p in staff_data:
        format_str = """INSERT INTO temp_time (time , temp)
        VALUES ( '{time}' , '{temp}');
        """

        sql_command = format_str.format(time=p[0], temp=p[1])
        print(sql_command)
        cursor.execute(sql_command)

    connection.commit()
    cursor.close()
    connection.close()

#“type:get\r\ntime:(현재시각)\r\n”
def sendTemp(time):
    connection = MySQLdb.connect(host=my_ip,
                                 user="root",
                                 passwd="root",
                                 db="xproj")

    cursor = connection.cursor()

    format_str = "SELECT * FROM temp_time WHERE time IN ('"+time+"');"

    sql_command = format_str
    print(sql_command)
    res=cursor.execute(sql_command)
    fetall = cursor.fetchall()
    connection.commit()
    cursor.close()
    connection.close()
    if res ==1:
        return  fetall[0][1]


if __name__ == '__main__':
    # s=sendTemp(("2018-06-05 02:10:06"))
    # print(s)
    echo_server(50007)

