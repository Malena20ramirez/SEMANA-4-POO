from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante

# Crear restaurante
mi_restaurante = Restaurante()

# Crear productos
producto1 = Producto("papi pollo", 5.00)
producto2 = Producto("Refresco", 2.00)

# Crear cliente
cliente1 = Cliente("Luis Campos", "0959789076")
cliente2 = Cliente("Maria Gomez", "0987654321")

# Agregar al restaurante
mi_restaurante.agregar_producto(producto1)
mi_restaurante.agregar_producto(producto2)

mi_restaurante.agregar_cliente(cliente1)
mi_restaurante.agregar_cliente(cliente2)

# Mostar información
mi_restaurante.mostrar_productos()
mi_restaurante.mostrar_clientes()