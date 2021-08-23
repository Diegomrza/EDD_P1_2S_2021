#ifndef COLA_H
#define COLA_H

#include <stdlib.h>
#include "NodoCola.cpp"
#include "NodoListaDoble.cpp"
#include "NodoTarea.cpp"
#include "ListaDoble.cpp"
#include "ListaLinealizada.cpp"
#include <cstdlib>

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
    int obtener_id();
    void encolar(string,string);
    void desencolar(ListaDoble *);
    void arreglarError(ListaDoble *, ListaLinealizada *);
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

void Cola::desencolar(ListaDoble *lista){
    
    NodoCola *aux = this->frente;
    
    while (aux != NULL)
    {
        if (aux->tipo=="estudiante")
        {
            cout<<aux->id_error<<endl;
            cout<<aux->id_tipo<<endl;
            cout<<aux->tipo<<endl;
            //lista->mostrarUno(aux->id_tipo);

        } else{
            cout<<aux->id_error<<endl;
            cout<<aux->id_tipo<<endl;
            cout<<aux->tipo<<endl;
        }
        aux = aux->siguiente;
    }
}

int Cola::obtener_id(){
    NodoCola *aux = this->frente;
    
    while (aux != NULL)
    {
        if (aux->tipo=="Estudiante")
        {
            return aux->id_error;
        } else{
            return aux->id_error;
        }
        aux = aux->siguiente;
        
    }
}

void Cola::arreglarError(ListaDoble *lst, ListaLinealizada *lista){

    NodoCola *temp = this->frente;
    while (temp!=NULL)
    {
        if (temp->tipo.compare("estudiante")==0)
        {
            lst->modificarR(temp->id_tipo);
            if (this->frente==this->fin)
            {
                this->frente=NULL;
                this->fin=NULL;
            } else {
                this->frente=frente->siguiente;
            }
            delete(temp);
            this->size--;
        } else{
            lista->modificar(temp->id_tipo);
            if (this->frente==this->fin)
            {
                this->frente=NULL;
                this->fin=NULL;
            } else {
                this->frente=frente->siguiente;
            }
            delete(temp);
            this->size--;
        }
        temp=temp->siguiente;
    }
    
}

bool Cola::vacia(NodoCola *frente){
    return (frente == NULL)? true: false;
}
#endif