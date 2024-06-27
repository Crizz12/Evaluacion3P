
Titulo = []
Autor = []
Género = []
Precio = []
NombreL = []
CantVender = []
PrecioU = []
PrecioF = []
def registroL():
    A = input("Ingrese el nombre del libro: ")
    Titulo.append(A)
    B = input("Ingrese el autor del libro: ")
    Autor.append(B)
    C = input("Ingrese el genero del libro: ")
    Género.append(C)
    D = int(input("Ingrese el precio de su libro: "))
    Precio.append(D)

def Venta():
    P = input("¿Cual es el nombre del libro que desea vender?: ")
    NombreL.append(P)
    F = int(input("¿Cual es la cantidad de libros que desea vender?: "))
    CantVender.append(F)
    V = int(input("¿Cual va a ser el precio por unidad?: "))
    PrecioU.append(V)
    J = CantVender * PrecioU
    PrecioF.append(J)


while True:
    print("(1)Registar libro\n(2)Listar todos los libros\n(3)Registrar venta\n(4)Imprimir reporte de ventas\n(5)Generar txt\n(0)Salir del programa")
    opc=int(input("Seleccione una opción: "))
    
    if opc==1:
        registroL()
    
    elif opc==2:
        print(Titulo)
        print(Autor)
        print(Género)
        print(Precio)
    
    elif opc==3:
        Venta()
        print(PrecioF)
        if Venta is not Titulo:
            print("No se encuentra ese libro")

    elif opc==4:
        print("Imprimiento reporte de ventas")

    elif opc==5:
        print("Generando txt")
        
    elif opc==0:
        print("Saliendo del programa...")
        break