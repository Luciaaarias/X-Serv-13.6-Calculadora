#!/usr/bin/python3

import sys

if (len(sys.argv)!= 4):
    print("Numero erroneo de argumentos")

else:
    # argumentos que meto en el terminal, desde python3
    nombre_programa, operacion, num1, num2 = sys.argv
    operaciones = ["sumar", "restar", "multiplicar", "dividir"]

    if operacion in operaciones:
       try:
            # compruebo si los parametros metidos son numeros y si lo son los
            # convierto a float para operar con ellos
            num1 = float(num1)
            num2 = float(num2)
            # si son numeros puedo operarlos
            if operacion == "sumar":
                resultado = num1 + num2
            elif operacion == "restar":
                resultado = num1 - num2
            elif operacion == "multiplicar":
                resultado = num1 * num2
            elif operacion == "dividir":
                try:
                    resultado = num1 / num2
                except ZeroDivisionError:
                    print("Error al dividir entre cero")
                    sys.exit()
            print(resultado)
       except ValueError:
           print("Los operandos introducidos no son numeros")
    else:
        print("Operacion no permitida")

