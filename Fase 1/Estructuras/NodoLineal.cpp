#ifndef NODOLINEAL_H
#define NODOLINEAL_H

#include <iostream>

using namespace std;

class NodoLineal
{
private:
    /* data */
public:

    int id;
    string carnet;
    string nombre;
    string descripcion;
    string materia;
    string fecha;
    int hora;
    string estado;

    NodoLineal *siguiente;
    NodoLineal *anterior;

    NodoLineal(int, string, string, string, string, string, int, string);
    ~NodoLineal();
};

NodoLineal::NodoLineal(int _id, string _carnet, string _nombre, string _descripcion, string _materia, string _fecha, int _hora, string _estado)
{
    this->siguiente=NULL;
    this->anterior=NULL;
    this->id=_id;
    this->carnet=_carnet;
    this->nombre=_nombre;
    this->descripcion=_descripcion;
    this->materia=_materia;
    this->fecha=_fecha;
    this->hora=_hora;
    this->estado=_estado;
}

NodoLineal::~NodoLineal()
{
}
#endif