#ifndef COLA_H
#define COLA_H

#include <stdlib.h>
#include "NodoCola.cpp"
#include "NodoListaDoble.cpp"
#include "NodoTarea.cpp"

class Cola
{
private:
    /* data */
public:
    NodoCola *frente;
    NodoCola *fin;
    int size=0;

    Cola(/* args */);
    bool vacia(NodoCola *);
    void encolar(string,string);
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

void Cola::encolar(string tipo, string id_tipo){

    NodoCola *nuevo = new NodoCola(this->size,tipo, id_tipo);
    
    if (this->frente==NULL){
        this->frente=nuevo;
        this->size++;
    } else{
        nuevo->siguiente = NULL;
        this->fin->siguiente = nuevo;
        this->size++;
    }
    this->fin=nuevo;
}

void Cola::desencolar(){

    NodoCola *aux = this->frente;
    
    while (aux != NULL)
    {
        cout<<"i"<<endl;
        cout<<aux->id_error<<endl;
        cout<<aux->id_tipo<<endl;
        cout<<aux->tipo<<endl;
        aux = aux->siguiente;
    }
    //cout<<aux->id_error<<endl;
    //cout<<aux->id_tipo<<endl;
    //cout<<aux->tipo<<endl;

}

bool Cola::vacia(NodoCola *frente){
    return (frente == NULL)? true: false;
}
#endif