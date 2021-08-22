#ifndef LISTALINEALIZADA_H
#define LISTALINEALIZADA_H

#include <iostream>
#include "NodoLineal.cpp"
#include "NodoTarea.cpp"

using namespace std;

class ListaLinealizada
{
private:
    /* data */
public:
    NodoTarea *primero;
    NodoTarea *ultimo;
    int size;

    ListaLinealizada(/* args */);
    void insertar(string, int, NodoTarea *);
    void mostrarUno(int);
    void mostrar();
    void modificar(int);
    void eliminar(int);
    ~ListaLinealizada();
};

ListaLinealizada::ListaLinealizada(/* args */)
{
    this->primero=NULL;
    this->ultimo=NULL;
    this->size=0;
}

void ListaLinealizada::insertar(string nombre, int posicion, NodoTarea *nuevo){
    nuevo->nombre_tarea+=" - "+nombre;
    nuevo->id_tarea = posicion;
    if (this->primero==NULL){
        this->primero = nuevo;
        this->ultimo = nuevo;
    } else if (nuevo->id_tarea < this->primero->id_tarea){
        nuevo->siguiente = this->primero;
        this->primero->anterior = nuevo;
        this->primero = nuevo;

        this->primero->anterior = this->ultimo;
        this->ultimo->siguiente = this->primero;
    } else {
        NodoTarea *aux = this->primero;
        while (aux->siguiente != NULL){
            if (nuevo->id_tarea < aux->siguiente->id_tarea){

                nuevo->siguiente = aux->siguiente;
                aux->siguiente->anterior = nuevo;
                nuevo->anterior = aux;
                aux->siguiente = nuevo;
                break;
            }
            aux = aux->siguiente;
        }
            
        if (aux->siguiente == NULL){
            aux->siguiente = nuevo;
            nuevo->anterior = aux;

            //nuevo->siguiente=this->primero;
            this->ultimo=nuevo;
            }
    }
    
}

void ListaLinealizada::mostrar(){
    NodoTarea *aux = this->primero;
    
    while (aux!= NULL)
    {
        if (aux->carnet != -1)
        {
            cout<<aux->id_tarea<<endl;
            cout<<" - "<<aux->nombre_tarea<<endl;
            cout<<" - "<<aux->materia<<endl;
            cout<<" - "<<aux->estado<<endl;
            cout<<" - "<<aux->descripcion_tarea<<endl;
            cout<<"Error - "<<aux->err_carnet<<endl<<endl;
        }
        aux=aux->siguiente;
    }
}

void ListaLinealizada::mostrarUno(int id){
    NodoTarea *aux =this->primero;
    while (aux != NULL)
    {
        if (id==aux->id_tarea)
        {
            cout<<"Posicion: "<<aux->nombre_tarea<<endl;
            break;
        }
        aux = aux->siguiente;
    }
}

void ListaLinealizada::modificar(int indice){
    NodoTarea *aux = this->primero;
    while (aux!=NULL)
    {
        if (/*aux->carnet!=-1 && */indice==aux->id_tarea)
        {
            bool bandera = false;
            while (bandera==false)
            {   
                cout<<"Qué dato desea modificar?"<<endl;cout<<"1. Carnet"<<endl;
                cout<<"2. Nombre"<<endl;cout<<"3. Descripcion"<<endl;
                cout<<"4. Materia"<<endl;cout<<"5. Fecha"<<endl;
                cout<<"6. Hora"<<endl;cout<<"7. Estado"<<endl;cout<<"8. Terminar"<<endl;
                int opcion; cin >> opcion;
                if (opcion==1){
                   cout<<"Ingrese el nuevo carnet: "<<endl; int carnetM; cin>>carnetM; aux->carnet=carnetM;
                } else if (opcion==2){
                   cout<<"Ingrese el nuevo nombre: "<<endl; string nombreM; cin.ignore(); getline(cin, nombreM); aux->nombre_tarea=nombreM;
                } else if (opcion==3){
                   cout<<"Ingrese la nueva descripcion: "<<endl; string descripcionM; cin.ignore(); getline(cin, descripcionM); aux->descripcion_tarea=descripcionM;
                } else if (opcion==4){
                   cout<<"Ingrese la nueva materia: "<<endl; string materiaM; cin.ignore(); getline(cin, materiaM); aux->materia=materiaM;
                } else if (opcion==5){
                   cout<<"Ingrese la nueva fecha: "<<endl; string fechaM; cin.ignore(); getline(cin, fechaM); aux->fecha=fechaM;
                } else if (opcion==6){
                   cout<<"Ingrese la nueva hora: "<<endl; int horaM; cin>>horaM; aux->hora=horaM;
                } else if (opcion==7){
                   cout<<"Ingrese el nuevo estado: "<<endl; string estadoM; cin.ignore(); getline(cin, estadoM); aux->estado=estadoM;
                } else if (opcion==8) {
                    bandera=true;
                } else {
                    cout<<"Ingrese una opcion valida"<<endl;
                }
            }
            break;
        }
        aux=aux->siguiente;
    }
    cout<<"Datos modificados"<<endl;

}

void ListaLinealizada::eliminar(int id){
    cout<<"id: "<<id<<endl;
    NodoTarea *temporal = this->primero;
    cout<<"id: "<<temporal->id_tarea<<endl;
    while (temporal!=NULL)
    {
        if (id==temporal->id_tarea)
        {   
            if (temporal==this->primero)
            {
                cout<<"No se puede eliminar al primero"<<endl;
                this->primero=temporal->siguiente;
                delete(temporal);
            } else if (temporal==this->ultimo)
            {
                cout<<"No se puede eliminar al ultimo"<<endl;
                
                temporal->anterior->siguiente=NULL;
                delete(temporal);
            } else{
                temporal->siguiente->anterior=temporal->anterior;
                temporal->anterior->siguiente=temporal->siguiente;
            
                delete(temporal);
            }
            break;
        }
        temporal=temporal->siguiente;
    }
    
}

ListaLinealizada::~ListaLinealizada()
{
}
#endif