def busqueda_lineal(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

lista_estudiantes = ["Anthony", "Bruno", "Anderson", "Siomara", "Daddy", "kevyn", "Santiago", "Ricardo", "Danny", "Leonardo"]

def main():
    while True:
        nombre = input("Ingresa el nombre del estudiante de la carrera de ingeniera en sistemas (o 'salir' para terminar la busqueda): ")
        if nombre.lower() == 'salir':
            break

        resultado = busqueda_lineal(lista_estudiantes, nombre)
        if resultado != -1:
            print(f"{nombre} está presente en la lista de estudiantes.")
        else:
            print(f"{nombre} no se encuentra en la lista de estudiantes.")

if __name__ == "__main__":
    main()

print("La busqueda a finalizado.")