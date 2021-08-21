//Importaciones de librerias importantes
#include <iostream>
#include <stdio.h>
#include <conio.h>
#include <fstream>
#include <locale.h>
#include <string.h>
#include <cstdlib> 
#include <cstring>
#include <regex>

//Importaciones de estructuras
#include "./Estructuras/ListaDoble.cpp"
#include "./Estructuras/NodoListaDoble.cpp"
#include "./Estructuras/Cola.cpp"
#include "./Estructuras/NodoCola.cpp"
#include "./Estructuras/NodoTarea.cpp"
#include "./Grafos/Grafo.cpp"
using namespace std;
//                  C:\Users\Squery\Desktop\Programas\Estudiantes.csv
//                  C:\Users\Squery\Desktop\Programas\Tareas.csv
ListaDoble *lst = new ListaDoble();
NodoTarea *listaTareas[5][30][9];
Cola *colaErrores = new Cola(); 

//                                            Hora dia mes

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
    menu();
}

//Menú principal
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
        cout << "* 6. Mostrar usuarios   *" << endl;
        cout << "*************************" << endl;
        cout << "Ingrese una opcion:\n>> ";
        cin >> opcion;

        if (opcion == "1"){
            cargaUsuarios();
        } else if (opcion == "2"){
            cargaTareas();
        } else if (opcion == "3"){
            ingresoManual();
        } else if (opcion == "4")
        {
            reportes();
        } else if (opcion == "5"){
            exit(0);
        } else if (opcion == "6"){
            lst->mostrar();
            cout << "Hay " << lst->size << " Elementos en la lista" << endl;
        } else if (opcion == "7")
        {
            colaErrores->desencolar();
        } else {
            cout << endl;
            cout << "Opcion invalida, seleccione una opcion del 1 al 5, por favor" << endl
                 << endl
                 << endl
                 << endl
                 << endl;
        }
    }
}


//Métodos de carga masiva       ****************************************
void cargaUsuarios()
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
        string arreglo[contador - 1];

        texto = "";

        stringstream input_stringstream(texting);
        getline(input_stringstream, texto, '\n');

        while (getline(input_stringstream, texto, '\n'))
        {
            arreglo[contador2] = texto;
            contador2++;
        }
        texto = "";
        //cout << contador << "      " << contador2 << endl;

        for (size_t i = 0; i < contador2; i++)
        {
            stringstream input_stringstream(arreglo[i]);
            
            getline(input_stringstream, texto, ','); //Carnet
            string carnet = texto;
            getline(input_stringstream, texto, ','); //Dpi
            string dpi = texto;
            getline(input_stringstream, texto, ','); //Nombre
            string nombre = texto;
            getline(input_stringstream, texto, ','); //Carrera
            string carrera = texto;
            getline(input_stringstream, texto, ','); //Password
            string password = texto;
            getline(input_stringstream, texto, ','); //Creditos
            long creditos = atoi(texto.c_str());
            getline(input_stringstream, texto, ','); //Edad
            long edad = atoi(texto.c_str());
            getline(input_stringstream, texto, ','); //Correo
            string correo = texto;

            regex r("[a-zA-Z_0-9\.]+@[a-zA-Z]+.(com|es|org){1}"); smatch m;
            //cout<<correo<<endl;
            
            string err_correo="";
            string err_dpi="";
            string err_carnet="";
            bool error_estudiantes=false;

            //Error en correo
            if (correo!="" && regex_match(correo, m, r)==0){
                err_correo="El correo no cumple";
                error_estudiantes=true;
            }
            //Error en dpi
            if (dpi!="" && dpi.length()!=13){
                err_dpi="El dpi no cumple con los 13 digitos establecidos";
                error_estudiantes=true;
            }
            //Error en carnet
            if (carnet!="" && carnet.length()!=9){
                err_carnet="El carnet no cumple con los 9 digitos establecidos";
                error_estudiantes=true;
            }
            //Si hay algun error en el dato se ingresa a la cola de errores
            if (error_estudiantes==true)
            {                           //Tipo      id
                colaErrores->encolar("estudiante",dpi);
            }
            if (nombre != "")
            {
                lst->insertar(carnet, dpi, nombre, carrera, correo, password, creditos, edad, err_carnet, err_dpi, err_correo);
            }
        }
    }
    archivo.close();
}

void cargaTareas()
{
    ifstream archivo;
    string texto;
    string texting;
    string ruta = "";
    int contadorT=0;
    int contadorT2=0;

    cout << "ingrese una ruta: " << endl;
    cin >> ruta;

    archivo.open(ruta, ios::in);

    if (archivo.fail()){
        cout << "No se pudo abrir el archivo :C" << endl;
    }
    else{
        while (!archivo.eof())
        {
            getline(archivo, texto);
            texting += texto + "\n";
            contadorT++;
        }
        string arreglo[contadorT-1];
        texto = "";
        
        stringstream input2_stringstream(texting);
        getline(input2_stringstream, texto, '\n');
        
        while (getline(input2_stringstream, texto, '\n')){
            arreglo[contadorT2] = texto;
            contadorT2++;
        }
        texto = "";
        
        int id_contador=0;
        for (int i = 0; i < 5; i++){
                for (int j = 0; j < 30; j++){
                    for (int k = 0; k < 9; k++){
                        NodoTarea *nuevo = new NodoTarea(id_contador,-1,"-1","-1","-1","-1",-1,"-1");
                        listaTareas[i][j][k]= nuevo;
                        id_contador++;
                    }
                    
                }
            }
        for (int a = 0; a < contadorT2; a++){
            stringstream input_stringstream(arreglo[a]);

            getline(input_stringstream, texto, ','); //Mes
            int mes = atoi(texto.c_str());
            getline(input_stringstream, texto, ','); //Día
            int dia = atoi(texto.c_str());
            getline(input_stringstream, texto, ','); //Hora
            int hora = atoi(texto.c_str());
            getline(input_stringstream, texto, ','); //Carnet
            int carnet = atoi(texto.c_str());
            getline(input_stringstream, texto, ','); //Nombre
            string nombre = texto;
            getline(input_stringstream, texto, ','); //Descripción
            string descripcion = texto;
            getline(input_stringstream, texto, ','); //Materia
            string materia = texto;
            getline(input_stringstream, texto, ','); //Fecha
            string fecha = texto;
            getline(input_stringstream, texto, ','); //Estado
            string estado = texto;

            

            for (int i = 1; i <= 5; i++){
                for (int j = 1; j <= 30; j++){
                    for (int k = 1; k <= 9; k++){
                        if ((mes==i+6) && dia==j && (hora==k+7)){
                            NodoTarea *nuevo = new NodoTarea(id_contador,carnet,nombre,descripcion,materia,fecha,hora,estado);
                            listaTareas[i-1][j-1][k-1]->carnet= carnet;
                            listaTareas[i-1][j-1][k-1]->nombre_tarea= nombre;
                            listaTareas[i-1][j-1][k-1]->descripcion_tarea= descripcion;
                            listaTareas[i-1][j-1][k-1]->materia= materia;
                            listaTareas[i-1][j-1][k-1]->fecha= fecha;
                            listaTareas[i-1][j-1][k-1]->hora= hora;
                            listaTareas[i-1][j-1][k-1]->estado= estado;
                        }
                        
                    } //For de los Meses
                } //For de los días
            } //For de las horas
        } //Fin del primer for que se usa para leer el archivo

        for (int i = 0; i < 5; i++){
            for (int j = 0; j < 30; j++){
                for (int k = 0; k < 9; k++){
                    if (listaTareas[i][j][k] != NULL){
                        cout<<listaTareas[i][j][k]->nombre_tarea<<endl;
                        cout<<listaTareas[i][j][k]->id_tarea<<endl;
                        cout<<listaTareas[i][j][k]->descripcion_tarea<<endl;
                        cout<<listaTareas[i][j][k]->estado<<endl<<endl<<endl;
                    }
                }
            }
        }
    } //Fin primer if
    archivo.close();
}
//Fin métodos de carga masiva   ****************************************


//---------------------------------------------------------------------------------------------------------//


//Métodos de ingreso manual     ****************************************
void ingresoManual()
{
    cout << "*Menu ingreso manual*" << endl;
    cout << "* 1.   Usuarios     *" << endl;
    cout << "* 2.   Tareas       *" << endl;
    cout << "* 3.   Regresar     *" << endl;
    cout << "*********************" << endl;
    int opcion = 0;
    cin >> opcion;

    if (opcion == 1){
        menuUsuarios();
    }else if (opcion == 2){
        menuTareas();
    }else if (opcion == 3){
        menu();
    }
}

void menuUsuarios()
{

    cout << "**Menu Usuarios**" << endl;
    cout << "* 1. Ingresar   *" << endl;
    cout << "* 2. Modificar  *" << endl;
    cout << "* 3. Eliminar   *" << endl;
    cout << "* 4. Regresar   *" << endl;
    cout << "*****************" << endl;
    int opcion;
    cout << "Ingrese una opcion: " << endl;
    cin >> opcion;
    if (opcion == 1)
    {
        cout << "Ingrese los datos del nuevo usuario: " << endl;
        string noCarnet;
        cout << "Numero de carnet: " << endl;
        cin >> noCarnet;

        string dpi;
        cout << "Numero de dpi: \n";
        cin >> dpi;

        string correo;
        cout << "Correo: " << endl;
        cin >> correo;

        string password;
        cout << "Password: " << endl;
        cin >> password;

        int creditos;
        cout << "Creditos: " << endl;
        cin >> creditos;

        int edad;
        cout << "Edad: " << endl;
        cin >> edad;

        string nom;
        cout << "Nombre: " << endl;
        cin.ignore(); //Sirve para el getline
        getline(cin, nom);

        string carrera;
        cout << "Carrera: " << endl;
        getline(cin, carrera);

        lst->insertar(noCarnet, dpi, nom, carrera, correo, password, creditos, edad,"","","");
    }
    else if (opcion == 2)
    {
        string dpi;
        cout << "Ingrese el dpi del usuario que desea modificar" << endl;
        cin >> dpi;
        lst->modificar(dpi);
    }
    else if (opcion == 3)
    {
        string dpi;
        cout << "Ingrese el dpi del usuario que desea eliminar" << endl;
        cin >> dpi;
        lst->eliminar(dpi);
    }
    else if (opcion == 4)
    {
        ingresoManual();
    }
    //lst->mostrar();
    //cout << "El numero de elementos en la lista es: " <<lst->size<< endl;
}

void menuTareas()
{
    cout << "** Menu Tareas **" << endl;
    cout << "* 1. Ingresar   *" << endl;
    cout << "* 2. Modificar  *" << endl;
    cout << "* 3. Eliminar   *" << endl;
    cout << "* 4. Regresar   *" << endl;
    cout << "*****************" << endl;
    int opcion;
    cout << "Ingrese una opcion: " << endl;
    cin >> opcion;
    if (opcion == 1)
    {
    }
    else if (opcion == 2)
    {
        string dpi;
        cout << "Ingrese el id de la tarea que desea modificar" << endl;
        cin >> dpi;
    }
    else if (opcion == 3)
    {
        string dpi;
        cout << "Ingrese el id de la tarea que desea eliminar" << endl;
        cin >> dpi;
    }
    else if (opcion == 4)
    {
        ingresoManual();
    }
}
//Fin métodos de ingreso manual ****************************************


//---------------------------------------------------------------------------------------------------------//


//Método de reportes
void reportes()
{
    cout << "Metodo de reportes" << endl;
}
