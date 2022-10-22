from http.server import SimpleHTTPRequestHandler as handler
from operator import length_hint
from socketserver import TCPServer
import os 

registro= []

httpd= TCPServer(("",1234),handler)
registro = httpd.serve_forever()
file = open("registrar.txt", "w")
for n in registro:
file.write( registro + os.linesep)
