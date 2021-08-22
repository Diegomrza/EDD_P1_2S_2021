#include <iostream>
#include <sstream>
#include <fstream>
#include <cstdlib>
#include <string>

#include "../Estructuras/ListaDoble.cpp"
#include "../Estructuras/ListaLinealizada.cpp"
#include "../Estructuras/Cola.cpp"
#include "../Estructuras/NodoListaDoble.cpp"
#include "../Estructuras/NodoLineal.cpp"
#include "../Estructuras/NodoCola.cpp"


using namespace std;

class Grafo
{
private:
    /* data */
public:
    int contImag;
    Grafo(/* args */);
    void generarGrafo(ListaDoble *);
    void grafoCola(Cola *);
    void grafoTareas(ListaLinealizada *);
    ~Grafo();
};

Grafo::Grafo(/* args */)
{
    this->contImag=0;
}

void Grafo::generarGrafo(ListaDoble *lista){ //Estudiantes
    string acumulador="digraph G{formar=png;\nrankdir = LR; \n node [shape=box]; \ncompound=true; \n";
    string nodo = "";
    string enlace = "";
    string label="";
    

    NodoListaDoble *temporal = lista->primero;

    while (temporal->siguiente!=lista->primero)
    {
        label+=temporal->noCarnet; label+="\n"; label+=temporal->dpi; label+="\n"; label+=temporal->nombre;
        label+="\n"; label+=temporal->carrera; label+="\n"; label+=temporal->password; label+="\n";
        label+= to_string(temporal->creditos); label+="\n"; label+=to_string(temporal->edad);; 
        nodo+="\"" + temporal->dpi + "\"" + "[label=\"" + label + "\"];\n";
        enlace+="\"" +  temporal->dpi + "\" -> \"" + temporal->siguiente->dpi + "\"[dir=\"both\"];\n";
        label="";
        temporal=temporal->siguiente;
    }
    label+=temporal->noCarnet; label+="\n"; label+=temporal->dpi; label+="\n"; label+=temporal->nombre;
    label+="\n"; label+=temporal->carrera; label+="\n"; label+=temporal->password; label+="\n";
    label+=to_string(temporal->creditos); label+="\n"; label+=to_string(temporal->edad); 
    nodo+="\"" + temporal->dpi + "\"" + "[label=\"" + label + "\"];\n";
    enlace+="\"" +  temporal->dpi + "\" -> \"" + temporal->siguiente->dpi + "\"[dir=\"both\"];\n";
    label="";

    acumulador+=nodo+enlace+ "\n}\n";

    string filename("g"+to_string(contImag)+".dot");
    fstream file_out;

    file_out.open(filename, std::ios_base::out);
    if(!file_out.is_open()){
        cout << "Error al abrir el archivo: " <<filename << '\n';
    }else{
        file_out << acumulador << endl;
        cout << "La escritura fue un exito" << endl;
    }

    string cmd = "dot -Tpng g"+to_string(contImag)+".dot -o g"+to_string(contImag)+".png";

    system(cmd.c_str());
    contImag++; 
    //file_out.close();
}

void Grafo::grafoCola(Cola *cola){



}

void Grafo::grafoTareas(ListaLinealizada *lista){
    
    string acumulador="digraph G{formar=pdf;\nrankdir = LR; \n node [shape=box]; \ncompound=true; \n";
    string nodo = "";
    string enlace = "";
    string label="";
    int contador=1;

    NodoTarea *temp = lista->primero;

    while (temp->siguiente!=NULL)
    {
        
        
        cout<<temp<<endl;
        label+=to_string(temp->carnet); label+="\n"; label+=temp->nombre_tarea; label+=+"\n"; label+=temp->descripcion_tarea; label+=+"\n";
        label+= temp->materia; label+=+"\n"; label+=temp->fecha; label+=+"\n"; label+=to_string(temp->hora); label+="\n"; label+=temp->estado;
        label+=+"\n"; 
        nodo+="\"" + to_string(temp->id_tarea) + "\"" + "[label=\"" + label + "\"];\n";
        enlace+="\"" + to_string(temp->id_tarea) + "\" -> \"" + to_string(temp->siguiente->id_tarea) + "\"[dir=\"both\"];\n";
        label="";
        
        temp=temp->siguiente;
        contador++;
        cout<<contador<<endl;
    }
    
    label="";

    acumulador+=nodo+enlace+ "\n}\n";

    string filename("h"+to_string(contImag)+".dot");
    fstream file_out;

    file_out.open(filename, std::ios_base::out);
    if(!file_out.is_open()){
        cout << "Error al abrir el archivo: " <<filename << '\n';
    }else{
        file_out << acumulador << endl;
        cout << "La escritura fue un exito" << endl;
    }

    string cmd = "dot -Tpdf h"+to_string(contImag)+".dot -o h"+to_string(contImag)+".pdf";

    system(cmd.c_str()); 
    contImag++;
    //file_out.close();
    

}

Grafo::~Grafo()
{
}
