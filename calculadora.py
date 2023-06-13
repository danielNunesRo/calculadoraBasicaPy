sair = ''

while sair != 's':
    num1 = input('Digite um numero: ')
    num2 = input('Digite outro numero: ')
    operador = input ('Digite o operador: (+ - * / ) ')
    operadores_validos = '+-*/'

    try:
        num1_float = float(num1)
        num2_float = float(num2)
    except Exception as error:
        print('Error: ', error)


    if operador not in operadores_validos:
        print('Operador não é válido')

    if len(operador) > 1:
        print('Digite apenas um operador')

    if operador == '+':
        resultado = num1_float + num2_float
        print(resultado)
    elif operador == '-':
        resultado = num1_float - num2_float
        print(resultado)
    elif operador == '*':
        resultado = num1_float * num2_float
        print(resultado)
    elif operador == '/':
        resultado = num1_float / num2_float
        print(resultado)



    sair = input('Deseja sair ? [s]im ').lower()