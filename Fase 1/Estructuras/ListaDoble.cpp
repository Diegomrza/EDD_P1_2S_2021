#ifndef LISTADOBLE_H
#define LISTADOBLE_H

#include <iostream>
#include <stdlib.h>
#include <cstdlib>
#include <cstring>
#include "NodoListaDoble.cpp"
#include "ListaLinealizada.cpp"

using namespace std;

class ListaDoble
{
private:
    /* data */
public:
    NodoListaDoble *primero;
    NodoListaDoble *ultimo;
    int size;
    ListaDoble(/* args */);
    void insertar(string, string, string, string, string, string, int, int, string, string, string);
    void mostrar();
    void mostrarUno(string);
    void modificar(string);
    void modificarR(string);
    void eliminar(string);
    bool verificarCarnet(string);
    string devolverErrores(string);
    string cadenaReporte(ListaLinealizada *);
    ~ListaDoble();
};

ListaDoble::ListaDoble(/* args */)
{
    this->primero = NULL;
    this->ultimo = NULL;
    this->size = 0;
}

void ListaDoble::insertar(string _noCarnet, string _dpi, string _nombre, string _carrera, string _correo, string _password, int _creditos, int _edad, string _err_noCarnet, string _err_dpi, string _err_correo)
{

    NodoListaDoble *nuevo = new NodoListaDoble(_noCarnet, _dpi, _nombre, _carrera, _correo, _password, _creditos, _edad);
    nuevo->err_noCarnet=_err_noCarnet;
    nuevo->err_dpi=_err_dpi;
    nuevo->err_correo=_err_correo;
    
    if (this->primero == NULL)
    {
        this->primero = nuevo;
        this->ultimo = nuevo;
        this->size++;
    }
    else
    {
        nuevo->siguiente = this->primero;
        primero->anterior = nuevo;

        nuevo->anterior = this->ultimo;
        this->ultimo->siguiente = nuevo;
        this->ultimo = nuevo;
        this->size++;
    }
}

void ListaDoble::mostrar()
{
    NodoListaDoble *temporal = this->primero;
    int contador = 0;
    while (temporal->siguiente != this->primero)
    {
        cout<<" - "<<contador<<" - ";
        cout << temporal->noCarnet << endl;
        cout << temporal->dpi << endl;
        cout << temporal->nombre << endl;
        cout << temporal->carrera << endl;
        cout << temporal->correo << endl;
        cout << temporal->password << endl;
        cout << temporal->creditos << endl;
        cout << temporal->edad << "\n\n\n";
        cout << temporal->err_correo << "\n\n\n";
        cout << temporal->err_dpi << "\n\n\n";
        cout << temporal->err_noCarnet << "\n\n\n";
        temporal = temporal->siguiente;
        contador++;
    }
    cout<<" - "<<contador<<" - ";
    cout << temporal->noCarnet << endl;
    cout << temporal->dpi << endl;
    cout << temporal->nombre << endl;
    cout << temporal->carrera << endl;
    cout << temporal->correo << endl;
    cout << temporal->password << endl;
    cout << temporal->creditos << endl;
    cout << temporal->edad << "\n\n\n";
    cout << temporal->err_correo << "\n\n\n";
    cout << temporal->err_dpi << "\n\n\n";
    cout << temporal->err_noCarnet << "\n\n\n";
}

void ListaDoble::mostrarUno(string id){
    cout<<id<<endl;
    NodoListaDoble *aux =this->primero;
    while (aux->siguiente != this->primero)
    {
        cout<<"HMMM: "<<(id.compare(aux->noCarnet)==0)<<endl;
        if (id.compare(aux->noCarnet)==0)
        {
            cout<<"Errores: " <<endl;
            cout<<aux->err_correo<<endl;
            cout<<aux->err_noCarnet<<endl;
            cout<<aux->err_dpi<<endl;
            break;
        }
        
        aux = aux->siguiente;
    }
    
}

void ListaDoble::modificar(string dpi)
{
    bool bandera = false;
    NodoListaDoble *temporal = this->primero;
    while (temporal->siguiente != this->primero)
    {
        if (temporal->dpi == dpi)
        {
            while (bandera == false)
            {
                cin.ignore();
                cout<<"\n\nIngrese el dato que desea cambiar: "<<endl;
                cout<<"1. creditos actuales: "<<temporal->creditos<<endl;
                cout<<"2. edad actual: "<<temporal->edad<<endl;
                cout<<"3. carnet actual: "<<temporal->noCarnet<<endl;
                cout<<"4. dpi actual: "<<temporal->dpi<<endl;
                cout<<"5. correo actual: "<<temporal->correo<<endl;
                cout<<"6. password actual: "<<temporal->password<<endl;
                cout<<"7. nombre actual: "<<temporal->nombre<<endl;
                cout<<"8. carrera actual: "<<temporal->carrera<<endl;
                cout<<"9. Terminar cambios: "<<endl;
                int dato = 0;
                cin >> dato;
                if (dato==1)
                {
                    cout << "creditos"<< endl; int nuevo_creditos; cin >> nuevo_creditos; temporal->creditos = nuevo_creditos;
                } else if (dato == 2)
                {
                    cout << "edad: " << endl; int nuevo_edad; cin >> nuevo_edad; temporal->edad = nuevo_edad;
                } else if (dato == 3)
                {
                    cout << "carnet: " << endl; string nuevo_noCarnet; cin >> nuevo_noCarnet; temporal->noCarnet = nuevo_noCarnet;
                } else if (dato == 4)
                {
                    cout << "dpi: " << endl; string nuevo_dpi; cin >> nuevo_dpi; temporal->dpi = nuevo_dpi;
                } else if (dato == 5)
                {
                    cout << "correo: " << endl; string nuevo_correo; cin >> nuevo_correo; temporal->correo = nuevo_correo;
                } else if (dato == 6)
                {
                    cout << "password: " << endl; string nuevo_password; cin >> nuevo_password; temporal->password = nuevo_password;
                } else if (dato == 7)
                {
                    cout << "nombre: " << endl; string nuevo_nombre;  getline(cin, nuevo_nombre); temporal->nombre = nuevo_nombre;
                } else if (dato == 8)
                {
                    cout << "carrera: " << endl; string nuevo_carrera; getline(cin, nuevo_carrera); temporal->carrera = nuevo_carrera;
                } else if (dato == 9)
                {
                    bandera = true;
                    cout<<"\n\n"<<endl;
                }
            }
            cout << "Cambios realizados con exito" << endl;
            break;
        }
    temporal = temporal->siguiente;
    }
}

void ListaDoble::modificarR(string dpi){
    bool bandera = false;
    NodoListaDoble *temporal = this->primero;
    while (temporal->siguiente != this->primero)
    {
        if (temporal->dpi == dpi)
        {
            while (bandera == false)
            {
                cin.ignore();
                cout<<"\n\nIngrese el dato que desea cambiar: "<<endl;
                cout<<"1. creditos actuales: "<<temporal->creditos<<endl;
                cout<<"2. edad actual: "<<temporal->edad<<endl;
                cout<<"3. carnet actual: "<<temporal->noCarnet<<" - Error: "<<temporal->err_noCarnet<<endl;
                cout<<"4. dpi actual: "<<temporal->dpi<<" - Error: "<<temporal->err_dpi<<endl;
                cout<<"5. correo actual: "<<temporal->correo<<" - Error: "<<temporal->err_correo<<endl;
                cout<<"6. password actual: "<<temporal->password<<endl;
                cout<<"7. nombre actual: "<<temporal->nombre<<endl;
                cout<<"8. carrera actual: "<<temporal->carrera<<endl;
                cout<<"9. Terminar cambios: "<<endl;
                int dato = 0;
                cin >> dato;
                if (dato==1)
                {
                    cout << "creditos"<< endl; int nuevo_creditos; cin >> nuevo_creditos; temporal->creditos = nuevo_creditos;
                } else if (dato == 2)
                {
                    cout << "edad: " << endl; int nuevo_edad; cin >> nuevo_edad; temporal->edad = nuevo_edad;
                } else if (dato == 3)
                {
                    cout << "carnet: " << endl; string nuevo_noCarnet; cin >> nuevo_noCarnet; temporal->noCarnet = nuevo_noCarnet;
                } else if (dato == 4)
                {
                    cout << "dpi: " << endl; string nuevo_dpi; cin >> nuevo_dpi; temporal->dpi = nuevo_dpi;
                } else if (dato == 5)
                {
                    cout << "correo: " << endl; string nuevo_correo; cin >> nuevo_correo; temporal->correo = nuevo_correo;
                } else if (dato == 6)
                {
                    cout << "password: " << endl; string nuevo_password; cin >> nuevo_password; temporal->password = nuevo_password;
                } else if (dato == 7)
                {
                    cout << "nombre: " << endl; string nuevo_nombre;  getline(cin, nuevo_nombre); temporal->nombre = nuevo_nombre;
                } else if (dato == 8)
                {
                    cout << "carrera: " << endl; string nuevo_carrera; getline(cin, nuevo_carrera); temporal->carrera = nuevo_carrera;
                } else if (dato == 9)
                {
                    bandera = true;
                    cout<<"\n\n"<<endl;
                }
            }
            cout << "Cambios realizados con exito" << endl;
            break;
        }
    temporal = temporal->siguiente;
    }
}

void ListaDoble::eliminar(string dpi)
{
    NodoListaDoble *temporal=this->primero;
    while (temporal->siguiente!=this->primero)
    {
        if (temporal->dpi==dpi)
        {
            int opcion;
            cout<<"Esta seguro que desea eliminar a este usuario? "<<endl; //Pendiente
            cout<<"1. Si "<<endl;
            cout<<"2. No "<<endl;
            cin>>opcion;
            if (opcion==1)
            {
                if (this->primero == this->ultimo) // Si solo hay un nodo
                {
                this->primero=NULL;
                } 
                else if (temporal==this->primero) //Si el nodo es la cabeza de la lista
                {
                    temporal->siguiente->anterior=this->ultimo;
                    temporal->anterior->siguiente=temporal->siguiente;
                    this->primero=temporal->siguiente;
                    delete(temporal);
                }
                else{ //Si es un nodo intermedio
                temporal->anterior->siguiente = temporal->siguiente;
                temporal->siguiente->anterior = temporal->anterior;

                delete(temporal);
                this->size--;
                }
            }else{
                cout<<"No se elimino"<<endl;
            }
            break;
        }
        temporal=temporal->siguiente;
    }
    
    if (temporal==this->ultimo)
    {
        int opcion;
        cout<<"\n\n\n\nEsta seguro que desea eliminar a este usuario? "<<endl; //Pendiente
        cout<<"1. Si "<<endl;
        cout<<"2. No "<<endl;
        cin>>opcion;
        if (opcion==1)
        {
           cout<<"Eliminado"<<endl;
            temporal->anterior->siguiente=this->primero;
            temporal->siguiente->anterior=temporal->anterior;
            this->ultimo=temporal->anterior;
        } else{
            cout<<"\nNo se elimino"<<endl;
        }
    } else{
        cout<<"\n\n\n\n*******no se encontro**********\n\n\n\n"<<endl;
    }      
}

bool ListaDoble::verificarCarnet(string carnet){
    NodoListaDoble *aux = this->primero;

    while (aux!=this->ultimo){
        if (aux->noCarnet==carnet){
            return true;
        }
        aux=aux->siguiente;
    }
    if (aux->noCarnet==carnet){
        return true;
    } else{
        return false;
    }
}

string ListaDoble::cadenaReporte(ListaLinealizada *lista){
    string cadena="";

    NodoListaDoble *temp = this->primero;
    while (temp->siguiente!=this->ultimo)
    {
        cadena += "  ¿element type=\"user\"?\n";
        cadena += "    ¿item Carnet = "+temp->noCarnet+" $?\n";
        cadena += "    ¿item DPI = "+temp->dpi+" $?\n";
        cadena += "    ¿item Nombre = "+temp->nombre+" $?\n";
        cadena += "    ¿item Carrera = "+temp->carrera+" $?\n";
        cadena += "    ¿item Password = "+temp->password+" $?\n";
        cadena += "    ¿item Creditos = "+to_string(temp->creditos)+" $?\n";
        cadena += "    ¿item Edad = "+to_string(temp->edad)+" $?\n";
        cadena += "  ¿$element?\n";
        if (lista->cadenaReporte(temp->noCarnet)!="")
        {
            cadena+=lista->cadenaReporte(temp->noCarnet);
        }
        temp=temp->siguiente;
    }
    cadena += "  ¿element type=\"user\"?\n";
    cadena += "    ¿item Carnet = "+temp->noCarnet+" $?\n";
    cadena += "    ¿item DPI = "+temp->dpi+" $?\n";
    cadena += "    ¿item Nombre = "+temp->nombre+" $?\n";
    cadena += "    ¿item Carrera = "+temp->carrera+" $?\n";
    cadena += "    ¿item Password = "+temp->password+" $?\n";
    cadena += "    ¿item Creditos = "+to_string(temp->creditos)+" $?\n";
    cadena += "    ¿item Edad = "+to_string(temp->edad)+" $?";
    cadena += "  ¿$element?";
    if (lista->cadenaReporte(temp->noCarnet)!="")
    {
        cadena+=lista->cadenaReporte(temp->noCarnet);
    }
    return cadena;
}

string ListaDoble::devolverErrores(string dpi){

    NodoListaDoble *temp=this->primero;
    string cadena;
    while (temp->siguiente!=this->primero)
    {
        if (temp->dpi.compare(dpi))
        {
            cout<<"Fact 1"<<cadena<<endl;
            if (!(temp->err_correo.compare("")==0))
            {
                cadena+=temp->err_correo;
                cadena+="\n";
            }
            if (!(temp->err_dpi.compare(""))==0)
            {
                cadena+=temp->err_dpi ;
                cadena+="\n";
            }
            if (!(temp->err_noCarnet.compare("")==0))
            {
                cadena+=temp->err_noCarnet;
            }
            return cadena;
        }
        temp=temp->siguiente;
    }
    if (!(temp->err_correo.compare("")==0))
    {
        cadena+=temp->err_correo;
        cadena+="\n";
    }
    if (!(temp->err_dpi.compare(""))==0)
    {
        cadena+=temp->err_dpi ;
        cadena+="\n";
    }
    if (!(temp->err_noCarnet.compare("")==0))
    {
        cadena+=temp->err_noCarnet;
    }
    return cadena;
}

ListaDoble::~ListaDoble()
{
}
#endif