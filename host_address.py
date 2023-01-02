import socket

l = int(input())

for x in range(l):
    ip_adress = input()

    print(socket.gethostbyaddr(ip_adress)[0])