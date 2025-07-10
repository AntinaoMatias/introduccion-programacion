

# return va antes de las excepciones de un try:
# eval 

import math

def calculadora_basica(num1, num2, op):
    try:
        if op == '/' and num2 != 0:
            resultado = eval(str(num1) + op + str(num2))
            print(f'{num1} {op} {num2} = {round(resultado,2)}')
        elif op == '+' or op == '-' or op == '*':
            resultado = eval(str(num1) + op + str(num2))
            print(f'{num1} {op} {num2} = {round(resultado,2)}')        
        else:
            print('No se puede dividir por 0')
    except:
        print('Valor ingresado NO corresponde a un  número...')

def calculadora_basica_v2(num1, num2, op):
    try:
        if op == '/' and num2 != 0:
            resultado = eval(str(num1) + op + str(num2))
        elif op == '+' or op == '-' or op == '*':
            resultado = eval(str(num1) + op + str(num2))
        else:
            print('No se puede dividir por 0')
        return resultado
    except:
        print('Valor ingresado NO corresponde a un  número...')