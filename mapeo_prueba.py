notas = []

print("Introduce notas numéricas. Escribe -1 para finalizar.")

while True:
    entrada = input("Nota: ")
    if entrada == "-1":
        break
    try:
        nota = float(entrada.replace(",", "."))
        notas.append(nota)
    except ValueError:
        print("Formato no válido. Intenta de nuevo.")

if notas:
    print("\nNotas introducidas:", notas)
    print("Primera nota:", notas[0])
    print("Tres últimas:", notas[-3:])
    print("De la segunda a la penúltima:", notas[1:-1])
else:
    print("No se ingresaron notas.")