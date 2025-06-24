def calculadora(operacion, *args, operador='suma'):
    if not args:
        return "No se han proporcionado números."

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
                return "Error: división por cero."
            resultado /= num
    else:
        return "Operación no válida."

    return f"Resultado de la {operacion}: {resultado}"