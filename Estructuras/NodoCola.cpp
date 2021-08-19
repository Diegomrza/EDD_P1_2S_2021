#ifndef NODOCOLA_H
#define NODOCOLA_H

#include <stdlib.h>
#include <iostream>

using namespace std;

class NodoCola
{
private:
    /* data */
public:
    int id_error=0;
    string tipo;
    string descripcion;

    NodoCola *siguiente;
    NodoCola(int, string, string);
    ~NodoCola();
};

NodoCola::NodoCola(int _id_error, string _tipo, string _descripcion)
{
    this->id_error=_id_error;
    this->tipo=_tipo;
    this->descripcion=_descripcion;
    this->siguiente=NULL;
}

NodoCola::~NodoCola()
{
}

#endif