#Vamos a ver quien eres y tu mascota
nombre = input("Como te llamas: ")

if nombre == "Nataly":
    print("Hola Nataly")
    animal = input("¿Tu mascota es un gato o un perro? ")
    if animal == "gato" or animal == "Gato":
        print("Tu mascota es un gato")
        print("Claro es Simba!")
    else:
        print("No lo conozco, pero seguro es genial!")



elif nombre is not ["Nataly", "Natalie"]:
    print("Hola, no te conozco")
    animal = input("¿Tienes una mascota? (si/no) ")
    if animal.lower() == "si":
        print("Genial, siemprees es bueno tener una mascota.")
    else:
        print("Está bien, no todos tienen mascotas.")