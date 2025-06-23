alumnos = []

while True:
    entrada = input("Introduce nombre, edad y cursos separados por comas (o escribe 'salir'): ")
    if entrada.lower() == "salir":
        break

    try:
        nombre, edad, cursos = entrada.split(",", 2)
        edad = int(edad.strip())
        lista_cursos = [curso.strip() for curso in cursos.split("-")]  # Por ejemplo: mates-historia-inglés
        alumnos.append({"nombre": nombre.strip(), "edad": edad, "cursos": lista_cursos})
    except ValueError:
        print("Formato incorrecto. Usa: nombre, edad, curso1-curso2-curso3")

# Mostrar base de datos
if alumnos:
    print("\nBase de datos de alumnos:")
    for alumno in alumnos:
        print(f"- {alumno['nombre']} ({alumno['edad']} años): {', '.join(alumno['cursos'])}")
else:
    print("No se registraron alumnos.")