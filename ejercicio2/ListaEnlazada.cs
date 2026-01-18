public class ListaEnlazada
 {
    private Nodo? cabeza;

    public void Insertar(int dato)
     {
        Nodo nuevo = new Nodo(dato);
        if (cabeza == null) 
        {
            cabeza = nuevo;
        } 
        else 
        {
            Nodo actual = cabeza;
            while (actual.Siguiente != null) 
            {
                actual = actual.Siguiente;
            }
            actual.Siguiente = nuevo;
        }
    }

    // MÉTODO SOLICITADO: Buscar y contar ocurrencias
    public int BuscarYContar(int valor)
     {
        int contador = 0;
        Nodo? actual = cabeza;

        while (actual != null)
         {
            if (actual.Dato == valor)
             {
                contador++;
            }
            actual = actual.Siguiente;
        }

        if (contador == 0) 
        {
            Console.WriteLine($"El dato {valor} no fue encontrado en la lista.");
        } 
        else 
        {
            Console.WriteLine($"El dato {valor} se encontró {contador} veces.");
        }

        return contador;
    }

    public void Mostrar() {
        Nodo? actual = cabeza;
        while (actual != null) 
        {
            Console.Write(actual.Dato + " -> ");
            actual = actual.Siguiente;
        }
        Console.WriteLine("null");
    }

    public void EliminarDuplicados() 
    {
        if (cabeza == null) return;

        Nodo? actual = cabeza;
        while (actual != null) 
        {
            Nodo? buscador = actual;
            while (buscador.Siguiente != null) 
            {
                if (buscador.Siguiente.Dato == actual.Dato) 
                {
                    // Saltamos el nodo duplicado
                    buscador.Siguiente = buscador.Siguiente.Siguiente;
                } 
                else 
                {
                    buscador = buscador.Siguiente;
                }
            }
            actual = actual.Siguiente;
        }
    }

    public void Invertir() 
    {
    Nodo? anterior = null;
    Nodo? actual = cabeza;
    Nodo? siguiente = null; // Nodo? permite que reciba el nulo del final

    while (actual != null) 
    {
        siguiente = actual.Siguiente; // Aquí es donde suele saltar el CS8601
        actual.Siguiente = anterior;
        anterior = actual;
        actual = siguiente;
    }
    cabeza = anterior;
    }
 }

