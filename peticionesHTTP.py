from http.server import BaseHTTPRequestHandler, HTTPServer
import re

# Diccionario de rutas con funciones lambda
rutas = {
    ('GET', '/books'): lambda: "Listado de todos los libros",
    ('POST', '/books'): lambda: "Libro creado",
    ('PUT', '/books/123'): lambda: "Libro 123 actualizado",
    ('DELETE', '/books/123'): lambda: "Libro 123 eliminado"
}

# Función auxiliar para validar rutas
def es_ruta_valida(path):
    return re.match(r'^/[\w\-/]*$', path)

# Servidor
class MiManejador(BaseHTTPRequestHandler):
    def do_GET(self): self.responder('GET')
    def do_POST(self): self.responder('POST')
    def do_PUT(self): self.responder('PUT')
    def do_DELETE(self): self.responder('DELETE')

    def responder(self, metodo):
        if not es_ruta_valida(self.path):
            self.send_response(400)
            mensaje = "Ruta inválida: contiene caracteres no permitidos"
        elif (metodo, self.path) in rutas:
            mensaje = rutas[(metodo, self.path)]()
            self.send_response(200)
        else:
            # Si coincide con /books/<número>
            match = re.match(r"^/books/(\d+)$", self.path)
            if match:
                book_id = match.group(1)
                mensaje = f"Acceso dinámico al libro {book_id} con método {metodo}"
                self.send_response(200)
            else:
                mensaje = "Ruta o método no encontrado"
                self.send_response(404)

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