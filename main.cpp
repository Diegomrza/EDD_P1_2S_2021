#include <iostream>
#include <stdio.h>
#include <conio.h>
#include <fstream>
#include<locale.h>

using namespace std;

void lectura();

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

int main()
{
    setlocale(LC_CTYPE,"English");

    Persona p1 = Persona(20, "Diego");
    p1.leer();

    string opcion; //variable de tipo cadena de letras
    bool bandera = true; //variable de tipo falso o verdadero
    cout << "\n\n\n";
    while (bandera==true)
    {
        cout << "***********Menu**********" << endl;
        cout << "* 1. Carga de usuarios  *" << endl;
        cout << "* 2. Carga de tareas    *" << endl;
        cout << "* 3. Ingreso manual     *" << endl;
        cout << "* 4. Reportes           *" << endl;
        cout << "*************************" << endl; 
        cout << "Ingrese una opcion:\n>> ";
        cin >> opcion;
        
        if (opcion == "1")
        {
            cout << endl;
            cout << "Carga de usuarios...." << endl;
            lectura();
            bandera = false;
        } 
        else if (opcion == "2")
        {
            cout << endl;
            cout << "Carga de tareas...." << endl;
            bandera = false;
        } 
        else if (opcion == "3")
        {
            cout << endl;
            cout << "Ingreso manual...." << endl;
            bandera = false;
        } 
        else if (opcion == "4")
        {
            cout << endl;
            cout << "Reportes...." << endl;
            bandera = false;
        } 
        else
        {
            cout << endl;
            cout << "Opcion invalida, seleccione una opcion del 1 al 4, por favor" << endl << endl << endl << endl << endl;
        }
    }
}

void lectura(){
    ifstream archivo;
    string texto;
    string texting;
    string ruta = "";

    cout << "Ingrese la ruta del archivo: " << endl;
    cin >> ruta;

    archivo.open(ruta, ios::in);  //Abriendo el archivo en modo lectura

    if (archivo.fail())
    {
        cout << "Hubo un error al intentar abrir el archivo" << endl;
    } else{
        while (!archivo.eof()) 
        {
            getline(archivo, texto);
            texting += texto + "\n";
        }
        cout <<texting;
    }
    archivo.close();
}