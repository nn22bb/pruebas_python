alumnos = []

while True:
    entrada = input("Introduce nombre y nota separados por coma (o escribe 'salir'): ")
    
    if entrada.lower() == "salir":
        break

    try:
        nombre, nota = entrada.split(",")
        nota = nota.strip().replace(",", ".")  # Permitir comas como separador decimal
        nota_float = float(nota)
        alumnos.append((nombre.strip(), nota_float))
    except ValueError:
        print("Formato incorrecto. Usa: nombre, nota   (ej. Ana, 7.5 o Jorge, 6,2)")

# Si se ingresaron datos, mostramos la información
if alumnos:
    print("\n Todos los alumnos:")
    for nombre, nota in alumnos:
        print(f" - {nombre}: {nota}")

    print(f"\n Primer alumno: {alumnos[0][0]} con nota {alumnos[0][1]}")

    print("\n Últimos tres:")
    for nombre, nota in alumnos[-3:]:
        print(f" - {nombre}: {nota}")

    print("\n🔹 Desde el segundo hasta el penúltimo:")
    for nombre, nota in alumnos[1:-1]:
        print(f" - {nombre}: {nota}")
else:
    print("No se ingresaron alumnos.")