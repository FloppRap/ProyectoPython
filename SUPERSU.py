from CINE import Cine

class Mantener:
    def __init__(self):
        self.cartelera = Cine.cartelera
    
    def LimpiarRegistroClientes(self):
        registro = open("RegistroCliente.txt","wt")
        registro.write(f"Nuevo registro : {Cine.cantidadClientes}")
        registro.close()
        Cine.cantidadClientes = 0

    def ModificarButacas(self):
        Cine.cantidadButacas = int(input("Nueva cantidad de butacas :"))

    def ModificarCartelera(self):
        print("1-Eliminar pelicula/s")
        print("\n2-Agregar pelicula/s")
        print("\n3-Modificar edad")
        
        opc = int(input("\n\nIngrese la opcion: "))

        if opc == 1:
            for peli,rango in self.cartelera.items():
                print(f"{peli}-{rango}")
            else:
                print("\nCual desea eliminar? ")
                pelicula = input()
                
                if self.cartelera.get(pelicula):
                    self.cartelera.pop(pelicula)
                else:
                    print("Nombre Incorrecto.")
        elif opc == 2:
            pelicula = input("Ingrese la pelicula: ")
            edad = int(input("Edad correspondiente (1.ATP),(2.+13),(3.+18) :"))
            if edad == 1:
                rango = [0,100]
            elif edad == 2:
                rango = [13,100]
            elif edad == 3:
                rango = [18,100]
            else:
                print("ERROR")
            self.cartelera.setdefault(pelicula,rango)
        elif opc == 3:
            for peli,rango in self.cartelera.items():
                print(f"{peli}-{rango}")
            pelicula = input("Cual desea modificar? ")
            edad = int(input("Edad correspondiente (1.ATP),(2.+13),(3.+18) :"))
            if edad == 1:
                rango = [0,100]
            elif edad == 2:
                rango = [13,100]
            elif rango == 3:
                rango = [18,100]
            else:
                print("ERROR")

            if self.cartelera.get(pelicula):
                self.cartelera.update({pelicula:rango})