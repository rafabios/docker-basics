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
import time

PORT_NUMBER = int(os.getenv('WEBSERVICE_PORT'))


WEBSERVICE_NAME = str(os.getenv('WEBSERVICE_NAME'))
WEBSERVICE_VERSION =  str(os.getenv('WEBSERVICE_VERSION'))
HOSTNAME = str(socket.gethostname())
DATE     = str(time.ctime())

MESSAGE = '''
<html>
<head><title>PYTHON WEB SERVER</title></head>

<bodybgcolor="#E6E6FA">

<center>
<h1> PYTHON WEB SERVER </H1>

<br><br><br><br><br>


<br><br>
<b>WEBSERVICE_NAME</b>    = {0}

<br><br>

<b>WEBSERVICE_VERSION</b> = {1}

<br><br>

<b>CONTAINER NAME</b>    = {2}

<br><br>
</center>

<br><br><br><br><br><br><br><br><br><br><br>

<b>Data</b> : {3}

</body>
</html>

'''.format(WEBSERVICE_NAME, WEBSERVICE_VERSION , HOSTNAME, DATE  )




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
