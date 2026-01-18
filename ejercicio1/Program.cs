class Program
    {
        static void Main(string[] args)
        {
            ListaEnlazada lista = new ListaEnlazada();
            lista.Agregar(1);
            lista.Agregar(2);
            lista.Agregar(3);
            lista.Agregar(4);

            Console.WriteLine("Lista Original:");
            lista.Mostrar();

            lista.Invertir();

            Console.WriteLine("\nLista Invertida:");
            lista.Mostrar();
        }
    }


