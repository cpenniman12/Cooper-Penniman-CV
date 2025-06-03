#!/usr/bin/env python3
import http.server
import socketserver
import os

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        super().end_headers()

PORT = 3003
Handler = MyHTTPRequestHandler

os.chdir('/Users/cooperpenniman/Documents/personal-website')

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at http://localhost:{PORT}")
    print(f"Current directory: {os.getcwd()}")
    print(f"Files: {os.listdir('.')}")
    httpd.serve_forever() 