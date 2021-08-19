#ifndef COLA_H
#define COLA_H

#include <stdlib.h>
#include "NodoCola.cpp"

class Cola
{
private:
    /* data */
public:
    NodoCola *frente;
    NodoCola *fin;

    Cola(/* args */);
    bool vacia(NodoCola *);
    void insertar(int, string, string);
    void desencolar();
    ~Cola();
};

//Constructor
Cola::Cola()
{
    this->frente=NULL;
    this->fin=NULL;
}

//Destructor
Cola::~Cola()
{
}
void Cola::insertar(int id_error, string tipo, string descripcion){
    NodoCola *nuevo = new NodoCola(id_error, tipo, descripcion);
    
    if (vacia(this->frente)){
        this->frente=nuevo;
        this->fin=nuevo;
        nuevo->id_error++;
    } else{
        nuevo->siguiente=this->fin;
        this->fin=nuevo;
        nuevo->id_error++;
    }
}

bool Cola::vacia(NodoCola *frente){
    return (frente == NULL)? true: false;
}
#endif