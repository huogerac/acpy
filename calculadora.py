# coding: utf-8

import operator as op

"""
Calculadora na linha de comando

    >>> calcular(0.0, ['+', 100.0], {'+' : op.add, '-' : op.sub, '*' : op.mul, '/' : op.div, '**': op.pow})
    100.0
    >>> calcular(100.0, ['+', 100.0], {'+' : op.add, '-' : op.sub, '*' : op.mul, '/' : op.div, '**': op.pow})
    200.0

"""


def ler_entrada(valores, operacoes_validas):
    """
    Efetua a leitura na linha de comando,
    Se valor = um operador (+, - ...) é colocado na posição 0 da lista de valores
    Se valor = número válido,         é colocado na posição 1 da lista de valores
    Caso contrário é exibido um erro
    """
    valores[1] = 0.00
    input_str = raw_input(valores[0])
    if input_str in operacoes_validas:
        valores[0] = input_str
    else:
        try:
            valores[1] = float(input_str)
        except ValueError:                     
            print u'Valor inválido: ', input_str
    return valores



def calcular(total, valores, operacoes):
    """
    Efetua o calculo do total conforme o operador e valor
    Ex: Total = Total [+, -, *, /] valor
    """
    operador = valores[0]
    valor = valores[1]
    if valor > 0:            
        total = operacoes[operador](total, valor)
    return total
    
#Linha de comando
if __name__ == "__main__":
    operacoes = {'+' : op.add, 
                 '-' : op.sub, 
                 '*' : op.mul, 
                 '/' : op.div,
                 '**': op.pow}
    
    total = 0.0
    valores_input = ['+', 0.00] 
    while True:
      print total
      valores_input = ler_entrada(valores_input, operacoes)
      total = calcular(total, valores_input, operacoes)             