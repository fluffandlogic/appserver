from http.server import HTTPServer, BaseHTTPRequestHandler
import os
import sys
from pathlib import Path

class FileHandler(BaseHTTPRequestHandler):
    __root_folder = os.path.abspath("files")
    __content_type = {
        'html': 'text/html',
        'css': 'text/css',
        'js': 'application/javascript',
        'json': 'application/json',
        'default': 'text/plain'
    }
    __page_404 = os.path.join(__root_folder, "404.html")
    __page_500 = os.path.join(__root_folder, "500.html")


    def do_GET(self):
        path = self.path # This is the request from the browser
        if path == "/":
            path = "/index.html"        
        file_path = self.__root_folder + path

        try: 
            print(file_path)
            if os.path.isfile(file_path):
                with open(file_path, 'rb') as f:
                    content = f.read()

                self.send_response(200)

                file_parts = file_path.split('.')
                file_extension = file_parts.pop()
                content_type = self.__content_type["default"]

                for extension in self.__content_type:                                        
                    if file_extension == extension:                        
                        content_type = self.__content_type[extension]
                        break

                self.send_header('Content-type', content_type)
                self.send_header('Content-length', len(content))
                self.end_headers()

                self.wfile.write(content)
            else:
                self.send_response(404)
                self.send_header("Content-type", self.__content_type['html'])
                self.end_headers()

                with open(self.__page_404, 'rb') as f:
                    content = f.read()
                    f.close()
                    self.wfile.write(content)
                
        except Exception as e:
            self.send_response(500)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open(self.__page_500, 'rb') as f:
                content = f.read()
                f.close()
                self.wfile.write(content)


def server():
    domain = "127.0.0.1" # Localhost is denied access (Maybe Brave only issue?)
    port = 8000
    server = HTTPServer((domain, port), FileHandler)
    
    print(f"Server running on http://{domain}:{port}")
    print('Press Ctrl + C to stop')
    server.serve_forever()