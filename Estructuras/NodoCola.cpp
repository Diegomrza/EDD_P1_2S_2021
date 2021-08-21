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
    int id_error;
    string id_tipo;
    string tipo;
    //string descripcion;

    NodoCola *siguiente;
    NodoCola(int, string, string);
    ~NodoCola();
};

NodoCola::NodoCola(int _id_error, string _tipo, string _id_tipo)
{
    this->id_tipo=_id_tipo;
    this->id_error=_id_error;
    this->tipo=_tipo;
    this->siguiente=NULL;
}

NodoCola::~NodoCola()
{
}

#endif