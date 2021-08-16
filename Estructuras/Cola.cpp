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
    void insertar(NodoCola *, NodoCola *);
    ~Cola();
};

Cola::Cola(/* args */)
{
    this->frente=NULL;
    this->fin=NULL;
}

Cola::~Cola()
{
}

void Cola::insertar(NodoCola *frente, NodoCola *fin){
    NodoCola *nuevo = new NodoCola();


}

bool Cola::vacia(NodoCola *frente){
    return (frente == NULL)? true: false;
}
#endif