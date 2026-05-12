from http.server import HTTPServer, BaseHTTPRequestHandler
import os
from pathlib import Path

class FileHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Default to index.html for root path
        file_path = self.path
        if file_path == '/':
            file_path = '/index.html'
        
        # Remove leading slash and build full path
        file_path = os.path.join('files', file_path.lstrip('/'))
        
        try:
            # Check if file exists
            if os.path.isfile(file_path):
                with open(file_path, 'rb') as f:
                    content = f.read()
                
                # Send response
                self.send_response(200)
                
                # Determine content type
                if file_path.endswith('.html'):
                    self.send_header('Content-type', 'text/html')
                elif file_path.endswith('.css'):
                    self.send_header('Content-type', 'text/css')
                elif file_path.endswith('.js'):
                    self.send_header('Content-type', 'application/javascript')
                elif file_path.endswith('.json'):
                    self.send_header('Content-type', 'application/json')
                else:
                    self.send_header('Content-type', 'text/plain')
                
                self.send_header('Content-length', len(content))
                self.end_headers()
                self.wfile.write(content)
            else:
                # File not found
                self.send_response(404)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b'<h1>404 - File Not Found</h1>')
        
        except Exception as e:
            self.send_response(500)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(f'<h1>500 - Server Error</h1><p>{str(e)}</p>'.encode())
    
    def log_message(self, format, *args):
        # Quiet logging
        print(f"{self.address_string()} - {format % args}")

if __name__ == '__main__':
    domain = '127.0.0.1'
    port = 8000
    server = HTTPServer((domain, port), FileHandler)
    print(f"Server running on http://{domain}:{port}")
    print('Press Ctrl+C to stop')
    server.serve_forever()
