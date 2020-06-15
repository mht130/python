from http.server import HTTPServer,SimpleHTTPRequestHandler

class Serv(SimpleHTTPRequestHandler):
    def do_GET(self):
        # res="Hello"
        # self.send_response(200)
        # self.end_headers
        # self.wfile.write(res.encode("utf-8"))
        f=open("log.txt",'a')
        f.write(self.address_string()+" : "+self.path+'\n')
htttpd=HTTPServer(('0.0.0.0',8080),Serv)
htttpd.serve_forever()
