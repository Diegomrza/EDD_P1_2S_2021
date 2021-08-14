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
    Nodo(T _valor);
    ~Nodo();
};

//Constructor
template <typename T>
Nodo<T>::Nodo(T _valor)
{
    this->valor = _valor;
    this->siguiente = NULL;
    this->anterior = NULL;
}
template <typename T>
Nodo<T>::~Nodo()
{
}
#endif