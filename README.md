# COMPARATIVO Y ANALISIS 
 Los Algoritmos que se uso  de Búsqueda Lineal y Árbol AVL
## Búsqueda Lineal: Lista de Estudiantes

Este algoritmo implementa una búsqueda lineal en una lista de nombres de estudiantes de la carrera de ingeniería en sistemas. Permite al usuario buscar un nombre específico en la lista y le indica si el nombre está presente o no. La búsqueda se repite hasta que el usuario decide salir.

### Código Importante

#### Función `busqueda_lineal`
```python
def busqueda_lineal(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1
```
Esta función recorre la lista arr y compara cada elemento con `x`. 

Si encuentra una coincidencia, devuelve el índice del elemento. Si no lo encuentra, devuelve `-1`.

#### Lista de `Estudiantes`
```python
lista_estudiantes = ["Anthony", "Bruno", "Anderson", "Siomara", "Daddy", "kevyn", "Santiago", "Ricardo", "Danny", "Leonardo"]
```

Esta es la lista de nombres de estudiantes en la que se realizará la búsqueda.

#### Función `main`
```python
def main():
    while True:
        nombre = input("Ingresa el nombre del estudiante de la carrera de ingeniera en sistemas (o 'salir' para terminar la búsqueda): ")
        if nombre.lower() == 'salir':
            break

        resultado = busqueda_lineal(lista_estudiantes, nombre)
        if resultado != -1:
            print(f"{nombre} está presente en la lista de estudiantes.")
        else:
            print(f"{nombre} no se encuentra en la lista de estudiantes.")

if __name__ == "__main__":
    main()
```
 Esta función principal maneja la interacción con el usuario. 
 
 Permite ingresar nombres para buscar en la lista y muestra el resultado de la búsqueda. El ciclo se repite hasta que el usuario ingrese `salir`.

## Árbol AVL: Gestión de Películas

Este algoritmo implementa un Árbol AVL para la gestión de un catálogo de películas. Permite insertar, buscar y eliminar películas del árbol, manteniendo el balance del árbol AVL para asegurar operaciones eficientes.

### Código Importante
#### Clase `NodoAVL`
```python
class NodoAVL:
    def __init__(self, codigo, pelicula):
        self.codigo = codigo
        self.pelicula = pelicula
        self.izquierda = None
        self.derecha = None
        self.altura = 1
```
Representa un nodo del árbol AVL, almacenando el código y nombre de la película, punteros a los nodos izquierdo y derecho, y la altura del nodo.

#### Clase `AVL`
```python
class AVL:
    def __init__(self):
        self.raiz = None
```
Representa el árbol AVL y contiene métodos para insertar, buscar y eliminar nodos, así como para mantener el balance del árbol.

#### Método `insertar`
```python
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
```
Inserta un nuevo nodo en el árbol AVL y asegura que el árbol permanezca balanceado después de cada inserción. Realiza rotaciones necesarias para mantener el balance.

#### Método `buscar`
```python
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
```
Busca un nodo en el árbol AVL por su código. Si encuentra el nodo, devuelve el nombre de la película; de lo contrario, devuelve None.

#### Método `eliminar`

```python
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
```
Elimina un nodo del árbol AVL por su código y asegura que el árbol permanezca balanceado después de cada eliminación. 

Realiza rotaciones necesarias para mantener el balance.


#### Método `min_valor_nodo`

```python
def min_valor_nodo(self, nodo):
    actual = nodo
    while actual.izquierda is not None:
        actual = actual.izquierda
    return actual
```
 Encuentra el nodo con el valor mínimo en un subárbol, utilizado durante la eliminación de nodos.

## Ejecución del Programa

```python
# Árbol AVL
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
        print(f"La Película '{pelicula}' es insertada correctamente con el codigo número {codigo}.")
    
    elif opcion == 'eliminar':
        codigo = int(input("Ingresa el codigo de la película que desea eliminar: "))
        gestor_peliculas.eliminar(codigo)
        print(f"La película del codigo número {codigo} ha sido eliminada.")
    
    else:
        print("Opción no válida. Inténtalo de nuevo.")

print("Busqueda finalizada.")
```
Este fragmento de código implementa la interacción del usuario con el árbol AVL para gestionar el catálogo de películas. 

Permite al usuario buscar, insertar y eliminar películas del árbol, asegurando que el árbol permanezca balanceado.
 ## Ejemplo de Uso
### `Insertar` Películas

```python
gestor_peliculas.insertar(1, "El Padrino")
gestor_peliculas.insertar(2, "Pulp Fiction")
gestor_peliculas.insertar(3, "La Fiesta de las Salchichas")
gestor_peliculas.insertar(4, "Cadena perpetua")
gestor_peliculas.insertar(5, "El club de la lucha")
```
Inserta las películas con sus respectivos códigos en el árbol AVL.

### `Buscar` una Película
```python
pelicula = gestor_peliculas.buscar(3)
if pelicula:
    print(f"La película del código 3 es: {pelicula}")
else:
    print("No se encontró una película con el código 3.")
```
Busca y muestra la película con el código `3`.

### `Eliminar` una Película

```python
gestor_peliculas.eliminar(4)
print("La película del código número 4 ha sido eliminada.")
```
Elimina la película con el código `4` del árbol AVL.

---

Demuesntra la comparación de los dos algoritmos que tiene la misma funcionalidad, con diferentes complejidad basandose en la busqueda de lista de estudiantes y gestion de peliculas.











