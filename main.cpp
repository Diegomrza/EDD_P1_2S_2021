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
#include <stdlib.h>

//Importaciones de estructuras
#include "./Estructuras/ListaLinealizada.cpp"
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
ListaLinealizada *linealizacion = new ListaLinealizada(); 

void menu();
void lectura();
void cargaUsuarios();
void cargaTareas();
void ingresoManual();
void reportes();
void menuUsuarios();
void menuTareas();
void linealizar();
void reporte_de_salida();

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
            //colaErrores->desencolar(lst);
            cout<<"\nLinealizacion"<<endl;
            linealizacion->mostrar();
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
            {                          //Tipo      id
                colaErrores->encolar("estudiante",dpi);
            }
            if (nombre != "")
            {
                lst->insertar(carnet, dpi, nombre, carrera, correo, password, creditos, edad, err_carnet, err_dpi, err_correo);
            }
        }
    }
    archivo.close();
    cout<<"\n\n\n";
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
        
        //Rellenando el vector con -1
        for (int i = 0; i < 5; i++)
        {
            for (int j = 0; j < 30; j++){
                for (int k = 0; k < 9; k++){
                    NodoTarea *nuevo = new NodoTarea(0,-1,"-1","-1","-1","-1",-1,"-1");
                    nuevo->mes=-1; nuevo->dia=-1;
                    listaTareas[i][j][k]= nuevo;
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

                            NodoTarea *nuevo = new NodoTarea(0,carnet,nombre,descripcion,materia,fecha,hora,estado);
                            nuevo->mes=mes; nuevo->dia=dia;
                            if (lst->verificarCarnet(to_string(nuevo->carnet)) == false)
                            {
                                nuevo->err_carnet="El numero de carnet no existe en la lista de estudiantes";
                                colaErrores->encolar("Tarea",to_string(nuevo->carnet));
                            }
                            listaTareas[i-1][j-1][k-1]=nuevo;
                        }
                    }
                } 
            } 
        } 
        linealizar();
    }
    archivo.close();
}

void linealizar(){
    int mes=5;
    int dia=30;
    int hora=9;
    for (int i = 1; i <= 5; i++)
    {
        for (int j = 1; j <= 30; j++)
        {
            for (int k = 1; k <= 9; k++)
            {
                //  i    j   k
                //  fil col pro
                //  mes-dia-hora
                //  (col*Tamfil + fil)*TamPro+pro
                int pos=((j-1)*mes+(i-1))*hora+(k-1);
                ////int pos=((j-1)*mes+(i-5))*9+(k-8);
                
                /*
                int pos=0;
                pos= ((dia-1)*9+(hora-8))*5+(mes-7);
                */
                //string var= to_string(i)+ "," + to_string(j)+ "," + to_string(k);
                linealizacion->insertar("", pos, listaTareas[i-1][j-1][k-1]);
            }
        }
    }
    //linealizacion->mostrar();
    cout<<"\n\n\n";
}
//Fin métodos de carga masiva   ****************************************


//---------------------------------------------------------------------------------------------------------//


//Métodos de ingreso manual     ****************************************
void ingresoManual()
{
    cout << "\n\n\n*Menu ingreso manual*" << endl;
    cout << "* 1.   Usuarios     *" << endl;
    cout << "* 2.   Tareas       *" << endl;
    cout << "* 3.   Regresar     *" << endl;
    cout << "*********************" << endl;
    int opcion = 0;
    cin >> opcion;

    if (opcion == 1){
        cout<<"\n\n\n";
        menuUsuarios();
    }else if (opcion == 2){
        cout<<"\n\n\n";
        menuTareas();
    }else if (opcion == 3){
        cout<<"\n\n\n";
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
        cout<<"\n\n\n";
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
        cout<<"\n\n\n";
    }
    else if (opcion == 2)
    {
        cout<<"\n\n\n";
        string dpi;
        cout << "Ingrese el dpi del usuario que desea modificar" << endl;
        cin >> dpi;
        lst->modificar(dpi);
        cout<<"\n\n\n";
    }
    else if (opcion == 3)
    {
        cout<<"\n\n\n";
        string dpi;
        cout << "Ingrese el dpi del usuario que desea eliminar" << endl;
        cin >> dpi;
        lst->eliminar(dpi);
        cout<<"\n\n\n";
    }
    else if (opcion == 4)
    {
        cout<<"\n\n\n";
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
        cout<<"\n\n\n";
        cout<<"Ingrese el mes: "<<endl;
        int mes; cin>>mes;
        mes=mes-7;          cout<<mes<<endl;
        cout<<"Ingrese el dia: "<<endl;
        int dia; cin>>dia;
        dia=dia-1;          cout<<dia<<endl;
        cout<<"Ingrese la hora: "<<endl;
        int hora; cin>>hora;
        hora=hora-8;        cout<<hora<<endl;

        cout<<"Numero de carnet: "<<endl;
        int carnet; cin>>carnet;

        cout<<"Nombre de la tarea: "<<endl;
        string nombre;      cin.ignore();   getline(cin, nombre);

        cout<<"Descripcion de la tarea: "<<endl;
        string descripcion; /*cin.ignore();*/   getline(cin, descripcion);

        cout<<"Materia: "<<endl;
        string materia;     /*cin.ignore();*/   getline(cin, materia);

        cout<<"Fecha de la tarea: "<<endl;
        string fecha;   cin>>fecha;    //cin.ignore();   getline(cin, fecha);

        cout<<"Estado: "<<endl;
        string estado;    cin>>estado;  //cin.ignore();   getline(cin, estado);
        //  pro col fil
        //  fil col pro
        //  mes-dia-hora
        //  (col*Tamfil + fil)*TamPro+pro
        int pos=0;
        //   ((j-1)*mes+(i-1))*hora+(k-1)
        pos= (dia*5+mes)*9+hora;

        NodoTarea *nuevo = new NodoTarea(0,carnet,nombre,descripcion,materia,fecha,hora,estado);
        nuevo->mes=mes+7; nuevo->dia=dia+1;
        linealizacion->insertar("",pos,nuevo);
        cout<<"\n\n\n";
    }
    else if (opcion == 2)
    {
        cout<<"\n\n\n";
        int indice;
        cout << "Ingrese el id de la tarea que desea modificar" << endl;
        cin >> indice;
        linealizacion->modificar(indice);
        cout<<"\n\n\n";
    }
    else if (opcion == 3)
    {
        cout<<"\n\n\n";
        int id;
        cout << "Ingrese el id de la tarea que desea eliminar" << endl;
        cin >> id;
        linealizacion->eliminar(id);
        cout<<"\n\n\n";
    }
    else if (opcion == 4)
    {
        cout<<"\n\n\n";
        ingresoManual();
    }
}
//Fin métodos de ingreso manual ****************************************


//---------------------------------------------------------------------------------------------------------//


//Método de reportes
void reportes()
{
    Grafo *nuevo = new Grafo();
    

    while (true)
    {
        cout << "\n\n\nSeleccione una opcion:\n1. Reporte sobre la lista de estudiantes" << endl;
        cout << "2. Reporte sobre la lista de tareas linealizadas" << endl;
        cout << "3. Busqueda en estructura linealizada" << endl;
        cout << "4. Busqueda de posicion en lista linealizada" << endl;
        cout << "5. Cola de errores" << endl;
        cout << "6. Codigo generado de salida" << endl;
        cout << "7. Regresar" << endl;
        int opcion=0;
        cin>>opcion;
        if (opcion==1)
        {
            nuevo->generarGrafo(lst);
            
        } else if (opcion==2)
        {
            nuevo->grafoTareas(linealizacion);
            
        } else if (opcion==3)
        {
            cout<<"Ingrese el mes, el dia y la hora: "<<endl;
            int mes;
            int dia;
            int hora;
            cout<<"Mes: "<<endl; cin>>mes;
            cout<<"Dia: "<<endl; cin>>dia;
            cout<<"Hora: "<<endl; cin>>hora;
            linealizacion->metodoReporte(mes, dia, hora);
            
        } else if (opcion==4)
        {
            cout<<"Ingrese el mes, el dia y la hora: "<<endl;
            int mes; cout<<"Mes: "<<endl; cin>>mes; mes=mes-7;
            int dia; cout<<"Dia: "<<endl; cin>>dia; dia=dia-1;
            int hora; cout<<"Hora: "<<endl; cin>>hora; hora=hora-8;
            
            int pos= (dia*5+mes)*9+hora;
            cout<<"Posicion: "<<pos<<endl;
        } else if (opcion==5)
        {
            nuevo->grafoCola(colaErrores);
            
        } else if (opcion==6)
        {
            
        } else if(opcion==7)
        {
            menu();
        }
    }
}

void reporte_de_salida(){
    
}