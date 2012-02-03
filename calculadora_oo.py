# coding: utf-8

"""
Calculadora 

    >>> calc = Calculadora()
    >>> calc.aceitar(10)
    >>> calc.visor()
    10
    >>> calc.pilha()
    [10]
    
    >>> calc.aceitar(20)
    >>> calc.visor()
    20
    >>> calc.pilha()
    [10, 20]
    
    >>> calc.aceitar('+')
    >>> calc.visor()
    30
    >>> calc.pilha()
    [30]
    
    >>> calc.aceitar(10)
    >>> calc.aceitar(11)
    >>> calc.aceitar(12)
    >>> calc.pilha()
    [30, 10, 11, 12]
    
    >>> calc.aceitar('+')
    >>> calc.pilha()
    [30, 10, 23]
    
    >>> calc.aceitar('-')
    >>> calc.pilha()
    [30, -13]
    
    >>> calc.aceitar('+')
    >>> calc.pilha()
    [17]
    
    >>> calc.aceitar('+')
    Traceback (most recent call last):
    ...
    ValueError: Numero de argumentos invalidos!
    
"""
import operator as op

class Operacao(object):
    
    operacoes = {'+' : op.add, 
                 '-' : op.sub, 
                 '*' : op.mul, 
                 '/' : op.div,
                 '**': op.pow}
    
    def __init__(self):
        self._operador = '+'    
    
    def valida(self, valor):
        existe = valor in self.operacoes
        if existe:
            self._operador = valor
        return existe
        
    def operador(self):
        return self.operacoes[self._operador]



    
class Calculadora(object):
    
    operacao = Operacao()
        
    def __init__(self):
        self._pilha = []
        
    def aceitar(self, valor):
        if self.operacao.valida(valor):
            self.calcular()
        else:
            self._pilha.append(valor)
    
    def visor(self):
        return self._pilha[-1]
    
    def pilha(self):
        return self._pilha
    
    def calcular(self):
        if len(self._pilha) < 2:
            raise ValueError('Numero de argumentos invalidos!')
        
        x = self._pilha[-2]
        y = self._pilha[-1]
        resultado = self.operacao.operador()(x, y)
        self._pilha.pop()
        self._pilha.pop()
        self.aceitar(resultado)
