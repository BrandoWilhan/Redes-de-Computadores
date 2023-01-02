import socketserver
import http.server

HOST = "localhost"
PORT = 8888

httpd = None
socketserver.TCPServer.allow_reuse_address = True

try:
    
    Handler = http.server.SimpleHTTPRequestHandler
    httpd = socketserver.TCPServer((HOST, PORT), Handler)
    httpd.serve_forever()

except Exception as e:
    if httpd is not None:
        httpd.shutdown()
        httpd.server_close()
    raise