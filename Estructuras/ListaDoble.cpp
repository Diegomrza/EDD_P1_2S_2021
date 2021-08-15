#ifndef LISTADOBLE_H
#define LISTADOBLE_H

#include <iostream>
#include <stdlib.h>
#include "NodoListaDoble.cpp"

using namespace std;

class ListaDoble
{
private:
    /* data */
public:
    NodoListaDoble *primero;
    NodoListaDoble *ultimo;
    int size;
    ListaDoble(/* args */);
    void insertar(string , string, string, string, string, string, int, int);
    void mostrar();
    void modificar(string);
    void eliminar();
    ~ListaDoble();
};

ListaDoble::ListaDoble(/* args */)
{
    this->primero = NULL;
    this->ultimo = NULL;
    this->size = 0;
}

void ListaDoble::insertar(string _noCarnet, string _dpi, string _nombre, string _carrera, string _correo, string _password, int _creditos, int _edad){

    NodoListaDoble *nuevo = new NodoListaDoble(_noCarnet, _dpi, _nombre, _carrera, _correo, _password, _creditos, _edad);

    if (this->primero == NULL)
    {
        this->primero = nuevo;
        this->ultimo = nuevo;
        this->size++;
    } else{
        nuevo->siguiente = this->primero;
        primero->anterior = nuevo;

        nuevo->anterior = this->ultimo;
        this->ultimo->siguiente = nuevo;
        this->ultimo = nuevo;
        this->size++;
    }
}

void ListaDoble::mostrar(){
    
    NodoListaDoble *temporal = this->primero;

    while (temporal->siguiente != this->primero)
    {
       cout<<temporal->noCarnet<<endl;
       cout<<temporal->dpi<<endl;
       cout<<temporal->nombre<<endl;
       cout<<temporal->carrera<<endl;
       cout<<temporal->correo<<endl;
       cout<<temporal->password<<endl;
       cout<<temporal->creditos<<endl;
       cout<<temporal->edad<<"\n\n\n";
       temporal = temporal->siguiente;
    }
}

void ListaDoble::modificar(string dpi){
    NodoListaDoble *temporal = this->primero;

    while (temporal->siguiente != this->primero)
    {
        if (temporal->dpi == dpi)
        {
            cout<<"modificando datos";
        }
        
        temporal = temporal->siguiente;
    }
    
}

void ListaDoble::eliminar(){
    
}

ListaDoble::~ListaDoble()
{
}
#endif