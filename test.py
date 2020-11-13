from CINE import Cine
from SUPERSU import Mantener


#Alguas Variables
opcBucle = True
opciones = str()
nuevaCantidad = int()

prueba1 = Mantener()

while opcBucle:
    print("\n")
    print("1-Modificar Pelis\n")
    print("2-Limpiar registro\n")
    print("3-Modificar butacas\n")
    print("S/s-Salir")
    opciones = input("\nIngrese una opcion: ")

    if (opciones == "1"):
        print("\n")
        prueba1.ModificarCartelera()
    elif (opciones == "2"):
        prueba1.LimpiarRegistroClientes()
    elif (opciones == "3"):
        nuevaCantidad = int(input("Ingrese la nueva cantidad de butacas : "))
        prueba1.ModificarButacas(nuevaCantidad)
    elif (opciones.lower() == "s"):
        opcBucle = False 