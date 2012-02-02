# coding: utf-8

"""
Lista de exeercicios 1

    >>> filtrarlista(['Mariana', 'Ana', 'Paula'])
    ['Ana']
    
    >>> filtrarlista(['Pedro', 'Juca', 'Tom', 'Joaquim'])
    ['Juca', 'Tom']
    
    >>> listaassociativa(['Pedro', 'Juca', 'Tom', 'Joaquim'])
    [('P', 'Pedro'), ('J', 'Juca'), ('T', 'Tom'), ('J', 'Joaquim')]
    
    >>> montadicionario(['Pedro', 'Juca', 'Tom', 'Joaquim'])
    3
    
    >>> funcaozip(['Mariana', 'Ana', 'Paula'], ['Pedro', 'Juca', 'Tom', 'Joaquim'])
    3
    
    >>> casaisparadanca(['Mariana', 'Ana', 'Paula'], ['Pedro', 'Juca', 'Tom', 'Joaquim'])
    12
    
    >>> casaisparadancaComFiltro(['Mariana', 'Ana', 'Paula'], ['Pedro', 'Juca', 'Tom', 'Joaquim'])
    6
     
"""

def filtrarlista(lista):
    resultado = [item for item in lista if len(item) <= 4]
    return resultado

def listaassociativa(lista):
    resultado = [(item[0], item) for item in lista]
    return resultado

def montadicionario(lista):
    la = listaassociativa(lista)
    dicionario = {}
    for letra, item in la:
        dicionario[letra] = item
    return len(dicionario)

def funcaozip(lista1, lista2):
    la = []
    for (item1, item2) in zip(lista1, lista2):
        la.append((item1, item2))
    return len(la)

def casaisparadanca(listaM, listaH):
    casais = [(mulher, homem) for mulher in listaM for homem in listaH]
    return len(casais)

def casaisparadancaComFiltro(listaM, listaH):
    casais = [(mulher, homem) for mulher in listaM for homem in listaH if len(mulher) >= 4 and len(homem) >= 4]
    return len(casais)
