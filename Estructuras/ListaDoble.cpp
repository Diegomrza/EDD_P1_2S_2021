#ifndef NODO_H
#define NODO_H

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
    void insertar(int, int, string, string, string, string, int, int);
    
    ListaDoble(/* args */);
    ~ListaDoble();
};

ListaDoble::ListaDoble(/* args */)
{
}

void insertar(int noCarnet, int dpi, string nombre, string carrera, string correo, string password, int creditos, int edad){

    NodoListaDoble *nuevo = new NodoListaDoble(noCarnet, dpi, nombre, carrera, correo, password, creditos, edad);

}

ListaDoble::~ListaDoble()
{
}
#endif