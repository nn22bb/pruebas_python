alumnos = []

while True:
    entrada = input("Introduce nombre y nota separados por coma (o escribe 'salir'): ")
    if entrada.lower() == "salir":
        break

    try:
        nombre, nota = entrada.split(",")
        alumnos.append((nombre.strip(), float(nota.strip())))
    except ValueError:
        print("Formato incorrecto. Debe ser: nombre, nota")

# Mostrar resultados si hay alumnos registrados
if alumnos:
    print("\n Todos los alumnos:")
    for nombre, nota in alumnos:
        print(f" - {nombre}: {nota}")

    print(f"\n Primer alumno: {alumnos[0][0]} con nota {alumnos[0][1]}")

    ultimos_tres = alumnos[-3:]
    print("\n🔸 Últimos tres:")
    for nombre, nota in ultimos_tres:
        print(f" - {nombre}: {nota}")

    print("\n🔹 Desde el segundo hasta el penúltimo:")
    for nombre, nota in alumnos[1:-1]:
        print(f" - {nombre}: {nota}")
else:
    print("No se ingresaron alumnos.")