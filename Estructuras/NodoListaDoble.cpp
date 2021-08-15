#ifndef NODOLISTADOBLE_H
#define NODOLISTADOBLE_H

#include <iostream>
#include <stdlib.h>


using namespace std;

class NodoListaDoble
{
private:
    /* data */
public:
    int noCarnet;
    int dpi;
    string nombre;
    string carrera;
    string correo;
    string password;
    int creditos;
    int edad;

    NodoListaDoble * siguiente;
    NodoListaDoble * anterior;

    NodoListaDoble(int,int,string,string,string,string,int,int);
    ~NodoListaDoble();
};

NodoListaDoble::NodoListaDoble(int _noCarnet, int _dpi, string _nombre, string _carrera, string _correo, string _password, int _creditos, int _edad)
{
    this->noCarnet = _noCarnet;
    this->dpi = _dpi;
    this->nombre = _nombre;
    this->carrera = _carrera;
    this->correo = _correo;
    this->password = _password;
    this->creditos = _creditos;
    this->edad = _edad;
    this->siguiente = NULL;
    this->anterior = NULL;
}

NodoListaDoble::~NodoListaDoble()
{
}
#endif