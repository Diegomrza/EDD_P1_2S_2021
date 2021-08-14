#include <iostream>
#include <stdio.h>
#include <conio.h>
#include <fstream>
#include <locale.h>
#include "./Estructuras/Doble.cpp"
#include "./Grafos/Grafo.cpp"
using namespace std;

void menu();
void lectura();
void cargaUsuarios();
void cargaTareas();
void ingresoManual();
void reportes();

int main()
{
    //setlocale(LC_CTYPE,"English");
    //Doble<int> *lst = new Doble<int>();
    //lst->insertar(1);
    //lst->insertar(2);
    //lst->insertar(3);

    //cout << "El tamanio de la lista es: "<<lst->size << endl;

    menu();
}

void menu(){
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
        cout << "* 5. Cerrar el programa *" << endl;
        cout << "*************************" << endl; 
        cout << "Ingrese una opcion:\n>> ";
        cin >> opcion;
        
        if (opcion == "1")
        {
            cargaUsuarios();
        } 
        else if (opcion == "2")
        {
            cargaTareas();
        } 
        else if (opcion == "3")
        {
            ingresoManual();
        } 
        else if (opcion == "4")
        {
            reportes();
        } else if (opcion == "5")
        {
           exit(0);
        }
        else
        {
            cout << endl;
            cout << "Opcion invalida, seleccione una opcion del 1 al 5, por favor" << endl << endl << endl << endl << endl;
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

void cargaUsuarios(){
    cout << "Metodo de carga de usuarios" << endl;
}

void cargaTareas(){
    cout << "Metodo de carga de tareas" << endl;
}

void ingresoManual(){
    cout << "Metodo de ingreso manual" << endl;
    cout << "1. Usuarios" << endl;
    cout << "2. Tareas" << endl;
    cout << "3. Regresar" << endl;
    int opcion = 0;

    if (opcion == 1)
    {
        cout << "Usuarios" << endl;
    } else if (opcion == 2)
    {
        cout << "Tareas" << endl;
    } else if (opcion == 3)
    {
        cout << "Regresando" << endl;
    }
    
}

void reportes(){
    cout << "Metodo de reportes" << endl;
}   

