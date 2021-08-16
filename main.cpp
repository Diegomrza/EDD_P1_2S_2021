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
ListaDoble *lst = new ListaDoble(); //lista global


void menu();
void lectura();
void cargaUsuarios();
void cargaTareas();
void ingresoManual();
void reportes();
void menuUsuarios();
void menuTareas();

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
        } else if (opcion=="6")
        {
            lst->mostrar();
        } else
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
    cout << "\n\n\n" << endl;
    lectura();
}

void cargaTareas()
{
    cout << "Metodo de carga de tareas" << endl;
}

void ingresoManual()
{   
    cout << "*Menu ingreso manual*" << endl;
    cout << "* 1.   Usuarios     *" << endl;
    cout << "* 2.   Tareas       *" << endl;
    cout << "* 3.   Regresar     *" << endl;
    cout << "*********************"<<endl;
    int opcion = 0;
    cin >> opcion;

    if (opcion == 1)
    {
        menuUsuarios();
    }
    else if (opcion == 2)
    {
        menuTareas();
    }
    else if (opcion == 3)
    {
        menu();
    }
}

void menuUsuarios(){

    cout << "**Menu Usuarios**" <<endl;
    cout << "* 1. Ingresar   *" << endl;
    cout << "* 2. Modificar  *" << endl;
    cout << "* 3. Eliminar   *" << endl;
    cout << "* 4. Regresar   *" << endl;
    cout << "*****************" <<endl;
    int opcion;
    cout << "Ingrese una opcion: " <<endl;
    cin >> opcion;
    if (opcion == 1)
    {
        cout << "Ingrese los datos del nuevo usuario: " << endl;
        string noCarnet;
        string dpi;
        string nombre;
        string carrera;
        string correo;
        string password;
        int creditos;
        int edad;
        cout << "Numero de carnet: "<< endl; 
        cin>> noCarnet;       
        cout << "Numero de dpi: " << endl; 
        cin>> dpi;        
        cout << "Nombre: " << endl; 
        getline(cin,nombre);
        cout << "Carrera: " << endl; 
        getline(cin, carrera);       
        cout << "Correo: " << endl; 
        cin >> correo; 
        cout << "Password: " << endl; 
        cin >> password;  
        cout << "Creditos: " << endl; 
        cin >> creditos;
        cout << "Edad: " << endl; 
        cin >> edad;

        lst->insertar(noCarnet, dpi, nombre, carrera, correo, password, creditos, edad);
        
    } else if (opcion == 2)
    {
        string dpi;
        cout << "Ingrese el dpi del usuario que desea modificar" << endl;
    } else if (opcion == 3)
    {
        string dpi;
        cout << "Ingrese el dpi del usuario que desea eliminar" << endl;
    } else if (opcion == 4)
    {
        ingresoManual();
    }
    lst->mostrar();
    cout << "El numero de elementos en la lista es: " <<lst->size<< endl;
    
}

void menuTareas(){

}

void reportes()
{
    cout << "Metodo de reportes" << endl;
}