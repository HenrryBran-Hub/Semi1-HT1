from http.server import BaseHTTPRequestHandler, HTTPServer
import json

# Define el puerto en el que el servidor escuchará las conexiones
PORT = 5000

# Define el manejador de peticiones (RequestHandler)
class MiManejador(BaseHTTPRequestHandler):
    def do_GET(self):
        # Configura las cabeceras de la respuesta
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        # Define la respuesta como un diccionario JSON
        if self.path == '/check':
            respuesta = {'Estado': 'Check endpoint status: OK!!'}
        else:
            respuesta = {
                'Instancia': 'Instancia #2 - API #2',
                'Curso': 'Seminario de Sistemas 1',
                'Estudiante': 'Henrry David Bran Velasquez - 201314439'
            }

        # Envía la respuesta como JSON
        self.wfile.write(json.dumps(respuesta).encode('utf-8'))

# Crea el servidor con el manejador definido
with HTTPServer(('localhost', PORT), MiManejador) as servidor:
    print(f'Servidor activo en http://localhost:{PORT}')
    # Espera conexiones y maneja las solicitudes
    servidor.serve_forever()
