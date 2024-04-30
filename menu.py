import os
import helpers
from Producto import Producto

helpers.limpiar_pantalla()

def iniciar():
    while True:
      os.system('clear') # cls en Windows
      print("========================")
      print(" BIENVENIDO AL MANAGER DE PRODUCTOS ")
      print("========================")
      print("[1] Listar productos ")
      print("[2] Buscar producto ")
      print("[3] Añadir producto ")
      print("[4] Modificar producto ")
      print("[5] Borrar producto ")
      print("[6] Cerrar el Manager ")
      print("========================")
      opcion = input("> ")
      os.system('clear') # cls en Windows
      if opcion == '1':
            print("Listando los productos...\n")
            for producto in db.Productos.lista:
                 print(producto)
      elif opcion == '2':
            print("Buscando un producto...\n")
            codigo = helpers.leer_texto(3, 3, "Código (2 ints y 1 char)").upper()
            producto = db.Productos.buscar(codigo)
            print(producto) if producto else print("Producto no encontrado.")
      elif opcion == '3':
            print("Añadiendo un producto...\n")
            codigo = helpers.leer_texto(3, 3, "Código (2 ints y 1 char)").upper()
            nombre = helpers.leer_texto(2, 30, "Nombre (de 2 a 30 chars)").capitalize()
            tipo = helpers.leer_texto(2, 30, "Tipo (de 2 a 30 chars)").capitalize()
            db.Productos.crear(codigo, nombre, tipo)
      elif opcion == '4':
            print("Modificando un producto...\n")
            codigo = helpers.leer_texto(3, 3, "Código (2 ints y 1 char)").upper()
            producto = db.Productos.buscar(codigo)
            if producto:
                 nombre = helpers.leer_texto(2, 30, f"Nombre (de 2 a 30 chars)[{producto.nombre}]").capitalize()
                 tipo = helpers.leer_texto(2, 30, f"Tipo (de 2 a 30 chars)[{producto.tipo}]").capitalize()
                 db.Productos.modificar(producto.codigo, nombre, tipo)
                 print("Producto modificado correctamente.")
            else:
                 print("Producto no encontrado.")
      elif opcion == '5':
            print("Borrando un producto...\n")
            codigo = helpers.leer_texto(3, 3, "Código (2 ints y 1 char)").upper()
            print("Producto borrado correctamente.") if db.Productos.borrar(codigo) else print("Producto no encontrado.")
      elif opcion == '6':
            print("Saliendo...\n")
            break
      input("\nPresiona ENTER para continuar...")
