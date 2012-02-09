# coding: utf-8

"""
Lista de exeercicios 1

    >>> fox = 'The quick brown fox jumps over the lazy dog.'
    >>> fox_letters = set(l.upper() for l in fox if l.isalpha())
    >>> len(fox_letters)
    26
    
    >>> fox = 'The quick brown fox jumps over the lazy dog.'
    >>> fox_letters = set(l.upper() for l in fox)
    >>> len(fox_letters)
    28

    >>> fox = 'The quick brown fox jumps over the lazy dog.'
    >>> fox_letters = set(l.upper() for l in fox if l.isalpha())
    >>> import string
    >>> letters = set(string.ascii_uppercase)
    >>> foxletters == letters
    True
    
    >>> jabuti = 'Um pequeno jabuti xereta viu dez cegonhas felizes.'
    >>> jabuti_letras = set(l.upper() for l in jabuti if l.isalpha())

    >>> letters - jabuti_letras
    set(['Y', 'K', 'W'])
    
    >>> letters ^ jabuti_letras
    set(['K', 'W', 'Y'])
            
     
"""

# Operador ^ eh o operador bit a bit XOR