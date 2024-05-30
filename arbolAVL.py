class NodoAVL:
    def __init__(self, codigo, pelicula):
        self.codigo = codigo
        self.pelicula = pelicula
        self.izquierda = None
        self.derecha = None
        self.altura = 1

class AVL:
    def __init__(self):
        self.raiz = None

    def altura(self, nodo):
        if nodo is None:
            return 0
        return nodo.altura

    def balance(self, nodo):
        if nodo is None:
            return 0
        return self.altura(nodo.izquierda) - self.altura(nodo.derecha)

    def rotar_derecha(self, z):
        y = z.izquierda
        T3 = y.derecha

        y.derecha = z
        z.izquierda = T3

        z.altura = 1 + max(self.altura(z.izquierda), self.altura(z.derecha))
        y.altura = 1 + max(self.altura(y.izquierda), self.altura(y.derecha))

        return y

    def rotar_izquierda(self, z):
        y = z.derecha
        T2 = y.izquierda

        y.izquierda = z
        z.derecha = T2

        z.altura = 1 + max(self.altura(z.izquierda), self.altura(z.derecha))
        y.altura = 1 + max(self.altura(y.izquierda), self.altura(y.derecha))

        return y

    def insertar(self, codigo, pelicula):
        def _insertar(nodo, codigo, pelicula):
            if nodo is None:
                return NodoAVL(codigo, pelicula)
            if codigo < nodo.codigo:
                nodo.izquierda = _insertar(nodo.izquierda, codigo, pelicula)
            else:
                nodo.derecha = _insertar(nodo.derecha, codigo, pelicula)

            nodo.altura = 1 + max(self.altura(nodo.izquierda), self.altura(nodo.derecha))

            balance = self.balance(nodo)

            # Casos de desbalance
            if balance > 1:  # Subárbol izquierdo más pesado
                if codigo < nodo.izquierda.codigo:
                    return self.rotar_derecha(nodo)
                else:
                    nodo.izquierda = self.rotar_izquierda(nodo.izquierda)
                    return self.rotar_derecha(nodo)

            if balance < -1:  # Subárbol derecho más pesado
                if codigo > nodo.derecha.codigo:
                    return self.rotar_izquierda(nodo)
                else:
                    nodo.derecha = self.rotar_derecha(nodo.derecha)
                    return self.rotar_izquierda(nodo)

            return nodo

        self.raiz = _insertar(self.raiz, codigo, pelicula)

    def buscar(self, codigo):
        def _buscar(nodo, codigo):
            if nodo is None:
                return None
            if codigo == nodo.codigo:
                return nodo.pelicula
            elif codigo < nodo.codigo:
                return _buscar(nodo.izquierda, codigo)
            else:
                return _buscar(nodo.derecha, codigo)

        return _buscar(self.raiz, codigo)

    def eliminar(self, codigo):
        def _eliminar(nodo, codigo):
            if nodo is None:
                return nodo

            if codigo < nodo.codigo:
                nodo.izquierda = _eliminar(nodo.izquierda, codigo)
            elif codigo > nodo.codigo:
                nodo.derecha = _eliminar(nodo.derecha, codigo)
            else:
                if nodo.izquierda is None:
                    temp = nodo.derecha
                    nodo = None
                    return temp
                elif nodo.derecha is None:
                    temp = nodo.izquierda
                    nodo = None
                    return temp

                temp = self.min_valor_nodo(nodo.derecha)
                nodo.codigo = temp.codigo
                nodo.derecha = _eliminar(nodo.derecha, temp.codigo)

            if nodo is None:
                return nodo

            nodo.altura = 1 + max(self.altura(nodo.izquierda), self.altura(nodo.derecha))
            balance = self.balance(nodo)

            # Rebalanceo
            if balance > 1:  # Subárbol izquierdo más pesado
                if self.balance(nodo.izquierda) >= 0:
                    return self.rotar_derecha(nodo)
                else:
                    nodo.izquierda = self.rotar_izquierda(nodo.izquierda)
                    return self.rotar_derecha(nodo)

            if balance < -1:  # Subárbol derecho más pesado
                if self.balance(nodo.derecha) <= 0:
                    return self.rotar_izquierda(nodo)
                else:
                    nodo.derecha = self.rotar_derecha(nodo.derecha)
                    return self.rotar_izquierda(nodo)

            return nodo

        self.raiz = _eliminar(self.raiz, codigo)

    def min_valor_nodo(self, nodo):
        actual = nodo
        while actual.izquierda is not None:
            actual = actual.izquierda
        return actual


#árbol AVL
gestor_peliculas = AVL()

gestor_peliculas.insertar(1, "El Padrino")
gestor_peliculas.insertar(2, "Pulp Fiction")
gestor_peliculas.insertar(3, "La Fiesta de las Salchichas")
gestor_peliculas.insertar(4, "Cadena perpetua")
gestor_peliculas.insertar(5, "El club de la lucha")

while True:
    opcion = input("Ingrese la opción que desea: 'Buscar, Insertar, Eliminar o Salir: ").lower()
    
    if opcion == 'salir':
        break
    
    if opcion == 'buscar':
        codigo = int(input("Ingresa el codigo de la película que desea buscar: "))
        pelicula = gestor_peliculas.buscar(codigo)
        if pelicula:
            print(f"La película del codigo {codigo} es: {pelicula}")
        else:
            print(f"No se encontró una película con el codigo {codigo}.")
    
    elif opcion == 'insertar':
        codigo = int(input("Ingresa el codigo de la película que desea insertar: "))
        pelicula = input("Ingresa el nombre de la película que va insertar: ")
        gestor_peliculas.insertar(codigo, pelicula)
        print(f"La Película '{pelicula}' es insertada correctamente  con el codigo número {codigo}.")
    
    elif opcion == 'eliminar':
        codigo = int(input("Ingresa el codigo de la película que desea eliminar: "))
        gestor_peliculas.eliminar(codigo)
        print(f"La película del codigo número {codigo} ha sido eliminada.")
    
    else:
        print("Opción no válida. Inténtalo de nuevo.")

print("Busqueda finalizado.")
