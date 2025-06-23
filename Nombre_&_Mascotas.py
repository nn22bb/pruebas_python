nombre = input("¿Cómo te llamas? ")
nombres_validos = ["nataly", "natalie", "andrea"]

if nombre.lower() in nombres_validos:
    print(f"Hola {nombre}, ¡qué bueno conocerte!")

    animal = input("¿Tu mascota es un gato o un perro? ")
<<<<<<< HEAD
    if animal.lower() == "gato":
        print("Tu mascota es un gato.")
        print("¡Claro, es Simba!")
=======
    if animal == "gato" or animal == "Gato":
        print("Tu mascota es un gato")
        print("Claro es Simba!")
>>>>>>> c7b2602245f9d82d05c269b404483f70ca9a2c15
    else:
        print("No tienes perro.")
else:
    print("Hola, no te conozco.")
    tiene_mascota = input("¿Tienes mascota? (sí/no) ")

<<<<<<< HEAD
    if tiene_mascota.lower() == "sí":
        print("Genial, siempre es bueno tener una mascota.")
    elif tiene_mascota.lower() == "no":
        print("Está bien, no todos tienen mascotas.")
=======
elif nombre is not ["Nataly", "Natalie"]:
    print("Hola, no te conozco")
    animal = input("¿Tienes una mascota? (si/no) ")
    if animal.lower() == "si":
        print("Genial, siemprees es bueno tener una mascota.")
    else:
        print("Está bien, no todos tienen mascotas.")
>>>>>>> c7b2602245f9d82d05c269b404483f70ca9a2c15
