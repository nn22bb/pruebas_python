def calculadora(operacion, *args):
    if not args:
        return "No se han proporcionado números."

    operaciones_validas = {'suma', 'resta', 'multiplicacion', 'division'}
    if operacion not in operaciones_validas:
        return f"Operación '{operacion}' no reconocida. Las válidas son: {', '.join(operaciones_validas)}"

    try:
        if operacion == 'suma':
            resultado = sum(args)
        elif operacion == 'resta':
            resultado = args[0]
            for num in args[1:]:
                resultado -= num
        elif operacion == 'multiplicacion':
            resultado = 1
            for num in args:
                resultado *= num
        elif operacion == 'division':
            resultado = args[0]
            for num in args[1:]:
                if num == 0:
                    return "Error: división por cero no permitida."
                resultado /= num
    except Exception as e:
        return f"Ha ocurrido un error: {e}"

    return f"Resultado de la {operacion}: {resultado}"

# Interfaz por consola
if __name__ == "__main__":
    operacion = input("Escribe la operación (suma, resta, multiplicacion, division): ").strip().lower()
    numeros = input("Escribe los números separados por comas (por ejemplo: 4,5,6): ")
    
    try:
        lista_numeros = [float(num.strip()) for num in numeros.split(',') if num.strip() != '']
        if not lista_numeros:
            print("No se ingresaron números válidos.")
        else:
            resultado = calculadora(operacion, *lista_numeros)
            print(resultado)
    except ValueError:
        print("Error: asegúrate de introducir solo números separados por comas.")