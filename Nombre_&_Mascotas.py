nombre = input("¿Cómo te llamas? ")
nombres_validos = ["nataly", "natalie", "andrea"]

if nombre.lower() in nombres_validos:
    print(f"Hola {nombre}, ¡qué bueno conocerte!")

    animal = input("¿Tu mascota es un gato o un perro? ")
    if animal.lower() == "gato":
        print("Tu mascota es un gato.")
        print("¡Claro, es Simba!")
    else:
        print("No tienes perro.")
else:
    print("Hola, no te conozco.")
    tiene_mascota = input("¿Tienes mascota? (sí/no) ")

    if tiene_mascota.lower() == "sí":
        print("Genial, siempre es bueno tener una mascota.")
    elif tiene_mascota.lower() == "no":
        print("Está bien, no todos tienen mascotas.")