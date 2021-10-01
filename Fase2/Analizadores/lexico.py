reserved = {
    'Elements': 'TELEMENTS',
    'element' : 'TELEMENT',
    'type' : 'TTYPE',
    'item' : 'TITEM',
    'Carnet' : 'TCARNET',
    'DPI' : 'TDPI',
    'Nombre' : 'TNOMBRE',
    'Carrera' : 'TCARRERA',
    'Correo': 'TCORREO',
    'Password' : 'TPASSWORD',
    'Creditos' : 'TCREDITOS',
    'Edad' : 'TEDAD',
    'Descripcion' : 'TDESCRIPCION',
    'Materia' : 'TMATERIA',
    'Fecha' : 'TFECHA',
    'Hora' : 'THORA',
    'Estado' : 'TESTADO'
}

tokens = [
    'LQUESTION','RQUESTION','DOLAR','ID','EQUALS','NUMBER','NORMSTRING'
] + list(reserved.values())

t_LQUESTION = r'\¿'
t_RQUESTION = r'\?'
t_DOLAR = r'\$'
t_EQUALS = r'\='

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID')
    return t

def t_NUMBER(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print('Error en print %d', t.value)
        t.value = 0
    #print("El valor es: '%d" % t.value)
    return t

def t_NORMSTRING(t):
    r'\"(\\.|[^"\\])*\"'
    #print("la cadena es: '%s" % t.value)
    return t

# Ignored characters
t_ignore = '\t\r\n'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    #print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

import ply.lex as lex
import re
lexer = lex.lex(reflags=re.IGNORECASE)