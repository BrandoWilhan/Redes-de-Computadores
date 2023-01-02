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
        headers = response.getheaders()
        
        if(headers[2][1] == "text/html"):
            print("Browsing: " + content)
        if(headers[2][1] == "audio/mpeg"):
            print("Playing audio: " + content)
        if(headers[2][1] == "video/x-msvideo"):
            print("Playing media: " + content)
        if(headers[2][1] == "application/json"):
            print("Processing JSON: " + content)
        if(headers[2][1] == "video/mp4"):
            print("Unknown file/media: video/mp4-" + content)
        if(headers[2][1] == "audio/ogg"):
            print("Unknown file/media: audio/ogg-" + content)
        if(headers[2][1] == "close"):
            print("Content not found")


HTTPclient(HOST, PORT)
