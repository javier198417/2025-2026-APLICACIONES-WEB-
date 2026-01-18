public class ListaEnlazada
    {
        public Nodo? Cabeza { get; private set; }

        public void Agregar(int dato)
        {
            Nodo nuevoNodo = new Nodo(dato);
            if (Cabeza == null)
            {
                Cabeza = nuevoNodo;
            }
            else
            {
                Nodo temp = Cabeza;
                while (temp.siguiente != null)
                {
                    temp = temp.siguiente;
                }
                temp.siguiente = nuevoNodo;
            }
        }

        // MÉTODO SOLICITADO: Invertir la lista
        public void Invertir()
        {
            Nodo? anterior = null;
            Nodo? actual = Cabeza;
            Nodo? siguiente = null;

            while (actual != null)
            {
                // Guardamos el siguiente nodo para no perderlo
                siguiente = actual.siguiente;

                // Invertimos el puntero del nodo actual
                actual.siguiente = anterior;

                // Movemos las referencias un paso adelante
                anterior = actual;
                actual = siguiente;
            }

            // Al final, 'anterior' será la nueva cabeza
            Cabeza = anterior;
        }

        public void Mostrar()
        {
            Nodo? temp = Cabeza;
            while (temp != null)
            {
                Console.Write(temp.dato + " -> ");
                temp = temp.siguiente;
            }
            Console.WriteLine("null");
        }
    }