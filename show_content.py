import http.client

HOST = "localhost"
PORT = 8888

def HTTPclient(host, port):
    l = int(input())
    
    for x in range(l):
        content = input()
        conn = http.client.HTTPConnection(host, port)
        conn.request("GET", content)
        response = conn.getresponse()
        data = response.read().decode()
        print(data)


HTTPclient(HOST, PORT)