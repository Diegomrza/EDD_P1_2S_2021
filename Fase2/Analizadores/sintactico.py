from sys import api_version
from Analizadores.lexico import tokens
from Estructuras.Arboles.Nodos import NodoAVL, NodoTarea


estudiante = NodoAVL(0,'','','','','',0,0,'') #0,'','','','','',0,0,''
tarea = NodoTarea(0,'','','','',0,'') #0,'','','','',0,''
tipo = ''

# dictionary of names
names = {}
objetos = []

def p_statement_group(t):
    'statement : LQUESTION TELEMENTS RQUESTION elementos LQUESTION DOLAR TELEMENTS RQUESTION'
    print('Ok')


def p_elementos_group(t):
    """elementos : elementos elemento
                 | elemento
    """
    #objetos.append(estudiante)
    global tipo, estudiante, tarea
    

def p_elemento(t):
    'elemento : LQUESTION TELEMENT  tipoElemento RQUESTION items LQUESTION DOLAR TELEMENT RQUESTION'
    global estudiante, tarea, tipo
    if tipo == '"user"':
        nuevo = NodoAVL(estudiante.carnet, estudiante.dpi, estudiante.nombre,estudiante.carrera, estudiante.correo,estudiante.password,estudiante.creditos,estudiante.edad,'') 
        objetos.append(nuevo)
    elif tipo == '"task"':
        nuevo = NodoTarea(tarea.carnet, tarea.nombre, tarea.descripcion, tarea.materia,tarea.fecha,tarea.hora,tarea.estado)
        objetos.append(nuevo)

def p_tipoElemento(t):
    """tipoElemento : TTYPE EQUALS NORMSTRING
    """
    global tipo#, estudiante, tarea
    tipo = t[3]
    
    
def p_items(t):
    """items : items item
             | item
    """
    
def p_item(t):
    """item : LQUESTION TITEM tipeItem EQUALS valueItem DOLAR RQUESTION
    """
    global estudiante, tarea, tipo
    if tipo == '"user"':
        if t[3].lower() == 'carnet':
            estudiante.carnet = t[5]
        elif t[3].lower() == 'dpi':
            estudiante.dpi = t[5]
        elif t[3].lower() == 'nombre':
            estudiante.nombre = t[5]
        elif t[3].lower() == 'carrera':
            estudiante.carrera = t[5]
        elif t[3].lower() == 'password':
            estudiante.password = t[5]
        elif t[3].lower() == 'creditos':
            estudiante.creditos = t[5]
        elif t[3].lower() == 'edad':
            estudiante.edad = t[5]
        elif t[3].lower() == 'correo':
            estudiante.correo = t[5]
    elif tipo == '"task"':
        if t[3].lower() == 'carnet':
            tarea.carnet = t[5]
        elif t[3].lower() == 'nombre':
            tarea.nombre = t[5]
        elif t[3].lower() == 'descripcion':
            tarea.descripcion = t[5]
        elif t[3].lower() == 'materia':
            tarea.materia = t[5]
        elif t[3].lower() == 'fecha':
            tarea.fecha = t[5]
        elif t[3].lower() == 'hora':
            tarea.hora = t[5]
        elif t[3].lower() == 'estado':
            tarea.estado = t[5]
        
    
def p_valueItem(t):
    """valueItem : NORMSTRING
                 | NUMBER
                 """
    t[0] = t[1]
    

def p_tipeItem(t):
    """tipeItem : TCARNET
                | TDPI
                | TNOMBRE
                | TCARRERA
                | TPASSWORD
                | TCREDITOS
                | TEDAD
                | TDESCRIPCION
                | TMATERIA
                | TFECHA
                | THORA
                | TESTADO
                """
    t[0] = t[1]
    

def p_error(t):
    print("Syntax error at '%s'" % t.value)

import ply.yacc as yacc
parser = yacc.yacc()