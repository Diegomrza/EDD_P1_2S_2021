#ifndef NODOTAREA_H
#define NODOTAREA_H

#include <iostream>
#include <stdlib.h>


using namespace std;

class NodoTarea
{
private:
    /* data */
public:

    int mes;
    int dia;

    int id_tarea;
    int carnet;
    string nombre_tarea;
    string descripcion_tarea;
    string materia;
    string fecha;
    int hora;
    string estado;
    string err_carnet;

    NodoTarea *siguiente;
    NodoTarea *anterior;
    
    NodoTarea(int, int, string, string, string, string, int, string);
    ~NodoTarea();
};

NodoTarea::NodoTarea(int _id_tarea, int _carnet, string _nombre_tarea, string _descripcion_tarea, string _materia, string _fecha, int _hora, string _estado)
{
    this->id_tarea=_id_tarea;
    this->carnet=_carnet;
    this->nombre_tarea=_nombre_tarea;
    this->descripcion_tarea=_descripcion_tarea;
    this->materia=_materia;
    this->fecha=_fecha;
    this->hora=_hora;
    this->estado=_estado;
    
    this->siguiente=NULL;
    this->anterior=NULL;
    
}

NodoTarea::~NodoTarea()
{
}
#endif