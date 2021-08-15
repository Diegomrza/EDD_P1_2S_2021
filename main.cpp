#include <iostream>
#include <stdio.h>
#include <conio.h>
#include <fstream>
#include <locale.h>
#include <string.h>
#include <cstdlib> //Convertir a entero
#include <regex>

//#include "./Estructuras/Doble.cpp"
//#include "./Estructuras/Nodo.cpp"
#include "./Estructuras/ListaDoble.cpp"
#include "./Estructuras/NodoListaDoble.cpp"
#include "./Grafos/Grafo.cpp"

using namespace std;

// C:\Users\Squery\Desktop\Programas\Estudiantes.csv

void menu();
void lectura();
void cargaUsuarios();
void cargaTareas();
void ingresoManual();
void reportes();

int main()
{
    //setlocale(LC_CTYPE,"English");
    //[5][30][9] = 1350 posiciones
    
    menu();
}

void menu()
{
    string opcion;       //variable de tipo cadena de letras
    bool bandera = true; //variable de tipo falso o verdadero
    cout << "\n\n\n";
    while (bandera == true)
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
        }
        else if (opcion == "5")
        {
            exit(0);
        }
        else
        {
            cout << endl;
            cout << "Opcion invalida, seleccione una opcion del 1 al 5, por favor" << endl
                 << endl
                 << endl
                 << endl
                 << endl;
        }
    }
}

void lectura()
{
    ifstream archivo;
    string texto;
    string texting;
    string ruta = "";

    cout << "Ingrese la ruta del archivo: " << endl;
    cin >> ruta;

    archivo.open(ruta, ios::in); //Abriendo el archivo en modo lectura

    int contador = 0;
    int contador2 = 0;

    if (archivo.fail())
    {
        cout << "Hubo un error al intentar abrir el archivo" << endl;
    }
    else
    {
        while (!archivo.eof())
        {
            getline(archivo, texto);
            texting += texto + "\n";
            contador++;
        }
        string arreglo[contador-1];

        texto = "";
        stringstream input_stringstream(texting);
        getline(input_stringstream, texto, '\n');
        while (getline(input_stringstream, texto, '\n'))
        {
            arreglo[contador2] = texto;
            contador2++;
        }
        texto = "";
        cout << contador<< "      "<< contador2<<endl;

        //Doble<int> *lst = new Doble<int>();
        ListaDoble *lst = new ListaDoble();
        
        for (size_t i = 0; i < contador2; i++)
        {
            
            stringstream input_stringstream(arreglo[i]);
            getline(input_stringstream, texto, ',');
            string carnet = texto;

            getline(input_stringstream, texto, ',');
            string dpi = texto;

            getline(input_stringstream, texto, ',');
            string nombre = texto;

            getline(input_stringstream, texto, ',');
            string carrera = texto;
            
            getline(input_stringstream, texto, ',');
            string password = texto;

            getline(input_stringstream, texto, ',');
            long creditos = atoi(texto.c_str());

            getline(input_stringstream, texto, ',');
            long edad = atoi(texto.c_str());

            getline(input_stringstream, texto, ',');
            string correo = texto;

            cout <<"El dpi tiene " <<dpi.length() << "digitos" << endl;
            cout << "El carnet tiene " << carnet.length() << "digitos" << endl;
 
            if (carrera!="")
            {
                lst->insertar(carnet,dpi,nombre,carrera,correo,password,creditos,edad);
            }
        }
        lst->mostrar();
        cout << "El numero de elementos en la lista es: " <<lst->size<< endl;

    }
    archivo.close();
}

void cargaUsuarios()
{
    cout << "Metodo de carga de usuarios" << endl;
    lectura();
}

void cargaTareas()
{
    cout << "Metodo de carga de tareas" << endl;
}

void ingresoManual()
{
    cout << "Metodo de ingreso manual" << endl;
    cout << "1. Usuarios" << endl;
    cout << "2. Tareas" << endl;
    cout << "3. Regresar" << endl;
    int opcion = 0;

    if (opcion == 1)
    {
        cout << "Usuarios" << endl;
    }
    else if (opcion == 2)
    {
        cout << "Tareas" << endl;
    }
    else if (opcion == 3)
    {
        cout << "Regresando" << endl;
    }
}

void reportes()
{
    cout << "Metodo de reportes" << endl;
}