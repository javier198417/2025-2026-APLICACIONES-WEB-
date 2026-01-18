class Program 
{
    static void Main() 
    {
        ListaEnlazada miLista = new ListaEnlazada();

        // Llenando la lista con algunos datos (incluyendo repetidos)
        miLista.Insertar(10);
        miLista.Insertar(25);
        miLista.Insertar(10);
        miLista.Insertar(50);
        miLista.Insertar(10);

        Console.WriteLine("Lista Original:");
        miLista.Mostrar();

        // 1. Prueba del método de búsqueda solicitado
        Console.WriteLine("\n--- Prueba de Búsqueda ---");
        miLista.BuscarYContar(10); // Debería encontrar 3
        miLista.BuscarYContar(100); // No debería encontrarlo

        // 2. Ejecución de Ejercicio B (Eliminar duplicados)
        Console.WriteLine("\n--- Eliminando Duplicados ---");
        miLista.EliminarDuplicados();
        miLista.Mostrar();

        // 3. Ejecución de Ejercicio A (Invertir)
        Console.WriteLine("\n--- Invirtiendo Lista ---");
        miLista.Invertir();
        miLista.Mostrar();
    }
}