#ifndef NODO_H
#define NODO_H

#include <stdlib.h>

template <typename T>
class Nodo
{
private:
    /* data */
public:
    //el id es el dpi
    T valor;
    T noCarnet;
    T dpi;
    T nombre;
    T carrera;
    T correo;
    T password;
    T creditos;
    T edad;
    Nodo * siguiente;
    Nodo * anterior;
    Nodo(T _noCarnet, T _dpi, T _nombre, T _carrera, T _correo, T _password, T _creditos, T _edad);
    ~Nodo();
};

//Constructor
template <typename T>
Nodo<T>::Nodo(T _noCarnet, T _dpi, T _nombre, T _carrera, T _correo, T _password, T _creditos, T _edad)
{
    //this->valor = _valor;
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

//Desctructor
template <typename T>
Nodo<T>::~Nodo()
{
}
#endif