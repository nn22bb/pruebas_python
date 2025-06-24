from http.server import BaseHTTPRequestHandler, HTTPServer
import re

# Función auxiliar para validar rutas
def es_ruta_valida(path):
    return re.match(r'^/[\w\-/]*$', path)

# Lógica para cada categoría
def manejar_cliente(metodo, recurso_id=None):
    if metodo == 'GET' and recurso_id:
        return f"Mostrando cliente con ID {recurso_id}"
    elif metodo == 'GET':
        return "Listado de todos los clientes"
    elif metodo == 'POST':
        return "Nuevo cliente creado"
    elif metodo == 'PUT' and recurso_id:
        return f"Cliente {recurso_id} actualizado"
    elif metodo == 'DELETE' and recurso_id:
        return f"Cliente {recurso_id} eliminado"
    return "Operación no permitida para clientes"

def manejar_producto(metodo, recurso_id=None):
    if metodo == 'GET' and recurso_id:
        return f"Detalles del producto {recurso_id}"
    elif metodo == 'GET':
        return "Catálogo de productos"
    elif metodo == 'POST':
        return "Nuevo producto añadido"
    elif metodo == 'PUT' and recurso_id:
        return f"Producto {recurso_id} actualizado"
    elif metodo == 'DELETE' and recurso_id:
        return f"Producto {recurso_id} eliminado"
    return "Operación no permitida para productos"

def manejar_pedido(metodo, recurso_id=None):
    if metodo == 'GET' and recurso_id:
        return f"Información del pedido {recurso_id}"
    elif metodo == 'GET':
        return "Listado de pedidos"
    elif metodo == 'POST':
        return "Pedido registrado"
    elif metodo == 'PUT' and recurso_id:
        return f"Pedido {recurso_id} modificado"
    elif metodo == 'DELETE' and recurso_id:
        return f"Pedido {recurso_id} cancelado"
    return "Operación no permitida para pedidos"

# Diccionario que asocia categorías con funciones
categorias = {
    'clientes': manejar_cliente,
    'productos': manejar_producto,
    'pedidos': manejar_pedido
}

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
            partes = self.path.strip('/').split('/')
            categoria = partes[0] if len(partes) > 0 else None
            recurso_id = partes[1] if len(partes) > 1 else None

            if categoria in categorias:
                funcion = categorias[categoria]
                mensaje = funcion(metodo, recurso_id)
                self.send_response(200)
            else:
                mensaje = f"Categoría '{categoria}' no reconocida"
                self.send_response(404)

        print(f"{metodo} {self.path}")
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