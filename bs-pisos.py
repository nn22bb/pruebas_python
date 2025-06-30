def menu():
    datos = cargar_datos()

    while True:
        print("\n--- MENÚ DE GESTIÓN DE PISOS ---")
        print("1. Ver todos los pisos")
        print("2. Ver inquilinos de un piso")
        print("3. Añadir nuevo piso")
        print("4. Añadir inquilino a un piso")
        print("5. Mover inquilino a otro piso")
        print("6. Eliminar inquilino")
        print("0. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            ver_pisos(datos)

        elif opcion == "2":
            id_piso = input("ID del piso: ")
            ver_inquilinos(datos, id_piso)

        elif opcion == "3":
            id_piso = input("Nuevo ID de piso: ")
            ciudad = input("Ciudad: ")
            calle = input("Calle: ")
            numero = input("Número: ")
            datos[id_piso] = {
                "ciudad": ciudad,
                "calle": calle,
                "numero": numero,
                "inquilinos": []
            }
            print("✔️ Piso añadido.")

        elif opcion == "4":
            id_piso = input("ID del piso: ")
            nombre = input("Nombre del inquilino: ")
            trabajo = input("Trabajo: ")
            añadir_inquilino(datos, id_piso, nombre, trabajo)
            print("✔️ Inquilino añadido.")

        elif opcion == "5":
            origen = input("ID del piso actual: ")
            destino = input("ID del nuevo piso: ")
            nombre = input("Nombre del inquilino: ")
            mover_inquilino(datos, origen, destino, nombre)

        elif opcion == "6":
            id_piso = input("ID del piso: ")
            nombre = input("Nombre del inquilino: ")
            eliminar_inquilino(datos, id_piso, nombre)
            print("🗑️ Inquilino eliminado.")

        elif opcion == "0":
            guardar_datos(datos)
            print("👋 ¡Hasta luego!")
            break

        else:
            print("❗ Opción no válida.")