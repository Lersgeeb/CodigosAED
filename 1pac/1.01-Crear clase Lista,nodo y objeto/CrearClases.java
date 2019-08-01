public class CrearClases{

    public static void main(String [] args){
        
        Estudiante juan =new Estudiante("juan", 2018100);
        Nodo nodo =new Nodo(0,juan);
        ListaEnlazada lista = new ListaEnlazada(nodo);
    }
}

public class ListaEnlazada{

    private int primero;
    
    public void ListaEnlazada(int primero){
        this.primero = primero;
    }
}

public class Nodo{

    private String nombre;
    private Estudiante estudiante;
    private String siguiente;

    public void ListaEnlazada(String nombre, Estudiante estudiante){
        this.nombre = nombre;
        this.estudiante = estudiante;
        this.siguiente = null;
    }
}

public class Estudiante{

    private String nombre;
    private int nCuenta;
    private int indice;

    public void ListaEnlazada(String nombre, int nCuenta){
        this.nombre = nombre;
        this.nCuenta = nCuenta;
        this.indice = 100;
    }
}

