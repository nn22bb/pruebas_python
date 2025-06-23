notas = []

print("Introduce notas numéricas. Escribe -1 para finalizar.\n")

while True:
    entrada = input("Nota: ")
    if entrada == "-1":
        break
    try:
        nota = float(entrada.replace(",", "."))  # Acepta 7,5 y 7.5
        notas.append(nota)
    except ValueError:
        print(" Eso no es una nota válida. Intenta de nuevo.")

# Mostrar resultados
if notas:
    print("\n Notas introducidas:", notas)
    print(" Primera nota:", notas[0])
    print(" Tres últimas:", notas[-3:])
    print(" De la segunda a la penúltima:", notas[1:-1])
else:
    print("No se ingresaron notas.")