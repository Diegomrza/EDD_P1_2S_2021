#include <iostream>
#include <stdio.h>
#include <conio.h>

using namespace std;

class Persona{
    private:
        int edad;
        string nombre;
    public:
        Persona(int, string);
        void leer();
        void correr();
};
//constructor
Persona::Persona(int _edad, string _nombre){
    edad=_edad;
    nombre=_nombre;
}

void Persona::leer(){
    cout << "Soy "<<nombre<< " y estoy leyendo un libro" << endl;
}

void Persona::correr(){
    cout << "Soy "<< nombre<< " y estoy corriendo una maratón" << endl;
}