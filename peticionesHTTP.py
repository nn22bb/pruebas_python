from http.server import BaseHTTPRequestHandler, HTTPServer
import re

# Validación básica de la ruta
def es_ruta_valida(path):
    return re.match(r'^/[\w\-/]*$', path)

# Manejador del servidor HTTP
class MiManejador(BaseHTTPRequestHandler):
    def do_GET(self): self.responder('GET')
    def do_POST(self): self.responder('POST')
    def do_PUT(self): self.responder('PUT')
    def do_DELETE(self): self.responder('DELETE')

    def responder(self, metodo):
        if not es_ruta_valida(self.path):
            self.send_response(400)
            mensaje = "Ruta inválida: contiene caracteres no permitidos"
        else:
            # Coincide con /categoría (sin ID)
            match_simple = re.match(r"^/(\w+)$", self.path)
            # Coincide con /categoría/id (con ID numérico)
            match_con_id = re.match(r"^/(\w+)/(\d+)$", self.path)

            if metodo == 'GET' and match_simple:
                categoria = match_simple.group(1)
                mensaje = f"Listado de todos los elementos en '{categoria}'"
                self.send_response(200)
            elif metodo == 'POST' and match_simple:
                categoria = match_simple.group(1)
                mensaje = f"Nuevo elemento creado en '{categoria}'"
                self.send_response(201)
            elif metodo in {'PUT', 'DELETE'} and match_con_id:
                categoria, recurso_id = match_con_id.groups()
                if metodo == 'PUT':
                    mensaje = f"Elemento {recurso_id} actualizado en '{categoria}'"
                else:
                    mensaje = f"Elemento {recurso_id} eliminado de '{categoria}'"
                self.send_response(200)
            else:
                mensaje = "Ruta o método no encontrado"
                self.send_response(404)

        print(f"Petición recibida: {metodo} {self.path}")
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()
        self.wfile.write(mensaje.encode())

def ejecutar_servidor():
    puerto = 8080
    servidor = HTTPServer(('localhost', puerto), MiManejador)
    print(f"Servidor ejecutándose en http://localhost:{puerto}")
    servidor.serve_forever()

if __name__ == "__main__":
    ejecutar_servidor()