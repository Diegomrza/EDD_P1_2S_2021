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
    void insertar(T _valor);
    ~Doble();
};

template <typename T>
Doble<T>::Doble(/* args */)
{
    this->primero = NULL;
    this->ultimo = NULL;
    this->size = 0;
}

template <typename T>
void Doble<T>::insertar(T _valor){
    Nodo<T> *nuevo = new Nodo<T>(_valor);
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

template <typename T>
Doble<T>::~Doble()
{

}

#endif