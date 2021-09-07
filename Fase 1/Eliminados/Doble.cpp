#ifndef DOBLE_H
#define DOBLE_H

#include <iostream>
#include <stdlib.h>
#include "Nodo.cpp"

template <typename T>
class Doble
{
private:
    /* data */
public:
    Nodo<T> *primero;
    Nodo<T> *ultimo;
    int size;
    Doble(/* args */);
    void insertar(T _noCarnet, T _dpi, T _nombre, T _carrera, T _correo, T _password, T _creditos, T _edad);
    ~Doble();
};

//Constructor
template <typename T>
Doble<T>::Doble(/* args */)
{
    this->primero = NULL;
    this->ultimo = NULL;
    this->size = 0;
}


template <typename T>
void Doble<T>::insertar(T _noCarnet, T _dpi, T _nombre, T _carrera, T _correo, T _password, T _creditos, T _edad){
    Nodo<T> *nuevo = new Nodo<T>(_noCarnet, _dpi, _nombre, _carrera, _correo, _password, _creditos, _edad);
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

//Desctructor
template <typename T>
Doble<T>::~Doble()
{

}
#endif