#ifndef LISTALINEALIZADA_H
#define LISTALINEALIZADA_H

#include <iostream>
#include "NodoLineal.cpp"
#include "NodoTarea.cpp"

using namespace std;

class ListaLinealizada
{
private:
    /* data */
public:
    NodoTarea *primero;
    NodoTarea *ultimo;
    int size;

    ListaLinealizada(/* args */);
    void insertar(string, int, NodoTarea *);
    void mostrarUno(int);
    void mostrar();
    ~ListaLinealizada();
};

ListaLinealizada::ListaLinealizada(/* args */)
{
    this->primero=NULL;
    this->ultimo=NULL;
    this->size=0;
}

void ListaLinealizada::insertar(string nombre, int posicion, NodoTarea *nuevo){
    nuevo->nombre_tarea+=" - "+nombre;
    nuevo->id_tarea = posicion;
    if (this->primero==NULL){
        this->primero = nuevo;
        this->ultimo = nuevo;
    } else if (nuevo->id_tarea < this->primero->id_tarea){
        nuevo->siguiente = this->primero;
        this->primero->anterior = nuevo;
        this->primero = nuevo;

        this->primero->anterior = this->ultimo;
        this->ultimo->siguiente = this->primero;
    } else {
        NodoTarea *aux = this->primero;
        while (aux->siguiente != NULL){
            if (nuevo->id_tarea < aux->siguiente->id_tarea){

                nuevo->siguiente = aux->siguiente;
                aux->siguiente->anterior = nuevo;
                nuevo->anterior = aux;
                aux->siguiente = nuevo;
                break;
            }
            aux = aux->siguiente;
        }
            
        if (aux->siguiente == NULL){
            aux->siguiente = nuevo;
            nuevo->anterior = aux;
            }
    }
    
}

void ListaLinealizada::mostrar(){
    NodoTarea *aux = this->primero;

    while (aux!= NULL)
    {
        if (aux->carnet != -1)
        {
            cout<<aux->id_tarea<<endl;
            cout<<" - "<<aux->nombre_tarea<<endl;
            cout<<" - "<<aux->materia<<endl;
            cout<<" - "<<aux->estado<<endl;
            cout<<" - "<<aux->descripcion_tarea<<endl;
            cout<<"Error - "<<aux->err_carnet<<endl<<endl;
        }
        aux=aux->siguiente;
    }
    //cout<<aux->id_tarea<<aux->nombre_tarea<<endl;
    //cout<<aux->id_tarea<<aux->materia<<endl;
    //cout<<aux->id_tarea<<aux->estado<<endl;
    //cout<<aux->id_tarea<<aux->descripcion_tarea<<endl;
    
}

void ListaLinealizada::mostrarUno(int id){
    NodoTarea *aux =this->primero;
    while (aux != NULL)
    {
        if (id==aux->id_tarea)
        {
            cout<<"Posicion: "<<aux->nombre_tarea<<endl;
            break;
        }
        
        aux = aux->siguiente;
    }
    
}

ListaLinealizada::~ListaLinealizada()
{
}
#endif