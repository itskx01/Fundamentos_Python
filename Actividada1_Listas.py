# Tienda escolar
productosTienda = ["Lapices","Borradores","Tajalapiz","Esferos","Micropuntas","Reglas" ]
print (f"Que articulo busca: ", productosTienda)

# Precios de la tienda
preciosTienda = [float(1541), float(1288), float(1478), float(2788), float(2585), float(3857)]
print(f"El precio de los articulos son: ",preciosTienda )

# Cantidad de productos
cantidadTienda = [1000, 200, 1000, 2500, 1500, 1200]
print(f"El precio de los articulos son: ",cantidadTienda)

# Inventario
print(len(cantidadTienda))
# Impresion

print(f"Producto {productosTienda[0]}, el precio es: {preciosTienda[0]}, y esta disponible {cantidadTienda[0]}")
print(f"Producto {productosTienda[1]}, el precio es: {preciosTienda[1]}, y esta disponible {cantidadTienda[1]}")
print(f"Producto {productosTienda[2]}, el precio es: {preciosTienda[2]}, y esta disponible {cantidadTienda[2]}")
print(f"Producto {productosTienda[3]}, el precio es: {preciosTienda[3]}, y esta disponible {cantidadTienda[3]}")
print(f"Producto {productosTienda[4]}, el precio es: {preciosTienda[4]}, y esta disponible {cantidadTienda[4]}")
print(f"Producto {productosTienda[5]}, el precio es: {preciosTienda[5]}, y esta disponible {cantidadTienda[5]}")

print(type(productosTienda))
print(type(productosTienda[0]))
