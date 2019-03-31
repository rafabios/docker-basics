############################################################################################################
# Simples Web Server em python!
# Criado em 31/03/2019
# Criado por: Rafael Souza
#
# Passar os seguintes dados como variavel de ambiente:
# 
# WEBSERVICE_PORT     (INFORMAR PORTA TCP)
# WEBSERVICE_NAME     (INFORMAR NOME DO WEB SERVER)
# WEBSERVICE_VERSION  (INFORMAR A VERSAO)
# 
############################################################################################################

from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
import os
import socket

PORT_NUMBER = int(os.getenv('WEBSERVICE_PORT'))


WEBSERVICE_NAME = 'API_NAME: ' + str(os.getenv('WEBSERVICE_NAME'))
WEBSERVICE_VERSION = 'API_VERSION: ' + str(os.getenv('WEBSERVICE_VERSION'))
HOSTNAME = 'HOSTNAME: ' + str(socket.gethostname())


MESSAGE =  WEBSERVICE_NAME + '\n          '+ WEBSERVICE_VERSION + '\n               ' + '\n  ' + '\n  ' + HOSTNAME



#This class will handles any incoming request from
#the browser
class myHandler(BaseHTTPRequestHandler):

        #Handler for the GET requests
        def do_GET(self):
                self.send_response(200)
                self.send_header('Content-type','text/html')
                self.end_headers()
                # Send the html message
                self.wfile.write(MESSAGE)
                return

try:
        #Create a web server and define the handler to manage the
        #incoming request
        server = HTTPServer(('', PORT_NUMBER), myHandler)
        print 'Iniciando o webserver na porta: ' , str(PORT_NUMBER)

        #Wait forever for incoming htto requests
        server.serve_forever()

except KeyboardInterrupt:
        print '^C received, shutting down the web server'
        server.socket.close()
