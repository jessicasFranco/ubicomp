import http.server
import socketserver
PORT = ("",8000)
class myHandler(http.server.SimpleHTTPRequestHandler):

    def do_Get(self):
        self.send_response(200)
        self.send_header("Content-type","text/html")
        self.wfile.write("hello world")
        return
try:
    server = http.server.HTTPServer(PORT,myHandler)
    server.serve_forever()
except KeyboardInterrupt:
    print ("server ended")
    server.socket.close()
