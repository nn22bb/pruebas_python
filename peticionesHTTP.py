from http.server import BaseHTTPRequestHandler, HTTPServer

# Diccionario que mapea rutas a funciones y métodos
rutas = {
    ('GET', '/'): lambda: "Bienvenida a la página principal",
    ('GET', '/about'): lambda: "Acerca de nosotros",
    ('POST', '/datos'): lambda: "Procesando datos...",
    ('PUT', '/recurso'): lambda: "Recurso actualizado",
    ('DELETE', '/recurso'): lambda: "Recurso eliminado"
}

class MiManejador(BaseHTTPRequestHandler):
    def do_GET(self):
        self.responder('GET')

    def do_POST(self):
        self.responder('POST')

    def do_PUT(self):
        self.responder('PUT')

    def do_DELETE(self):
        self.responder('DELETE')

    def responder(self, metodo):
        ruta_clave = (metodo, self.path)
        if ruta_clave in rutas:
            mensaje = rutas[ruta_clave]()
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