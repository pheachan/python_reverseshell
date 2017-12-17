import socket


HOST = '127.0.0.1'
PORT = 8080

def connect():
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind((HOST,PORT))
    server.listen(1)
    conn, addr = server.accept()

    print("connection coming from ",addr[0])

    while True:
        cmd = input("SHELL...>")
        conn.send(cmd.encode('utf-8'))
        if 'terminate' in cmd:
            conn.close()
            break
        print(conn.recv(2024).decode('utf-8'))


connect()