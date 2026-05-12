from http.server import HTTPServer, BaseHTTPRequestHandler
import os.path

class MyHandler(BaseHTTPRequestHandler):
    content_type = { 
        'html': 'text/html', 
        'css': 'text/css', 
        'js': 'application/javascript', 
        'png': 'image/png', 
        'jpg': 'image/jpeg', 
        'gif': 'image/gif', 
        'application/json': 'application/json', 
        'text/plain': 'text/plain' 
    }

    def do_GET(self):        
        root = os.path.abspath("content")
        path = os.path.join(root, self.path)
        print("Path to file: ", path)
        if os.path.isfile(path):
            ext = path.split('.')[-1]
            for type in self.content_type:
                if ext == type:
                    with open(path, 'rb') as file:
                        content = file.read()
                    self.send_response(200)
                    self.send_header('Content-type', self.content_type[type])
                    self.end_headers()
                    self.wfile.write(content)
                    file.close()
                    return

def server():
    server_address = ('127.0.0.1', 8000)
    httpd = HTTPServer(server_address, MyHandler)
    print(f'Server running on http://{server_address[0]}:{server_address[1]}')
    httpd.serve_forever()

server()
