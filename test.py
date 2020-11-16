from CINE import Cine
from ADMIN import Admin
from CLIENTE import Mostrar, BuscarClientePorFecha

#Alguas Variables
opciones = ""
opcBucle = True
opcSala = int()
cantPersonas = int()
apellido = ""
dia = int()
mes = int()


#Instancias
prueba = Cine()
adm = Admin()

print("Salas: 1-Chica, 2-Grande")
opcSala = int(input("Escoja una sala : "))

if opcSala == 1:
      prueba.salaCine.ElegirSala(1)
elif opcSala == 2:
      prueba.salaCine.ElegirSala(2)
      
while opcBucle == True:
      
      print("""
            #Cliente
            1.Ver Cartelera
            2.Ver Disponibilidad
            3.Comprar

            #Administracion
            4.Mostrar Clientes
            5.Buscar clientes por fecha
            6.Guardar Registro de Clientes
            (s,S).Salir
      """)
      opciones = input("\nIngrese una Opcion: ")

      if opciones == '1':
            print(f" [pelicula:edad minima] : {prueba.cartelera}")
      
      elif opciones == '2':
            print(f"\nButacas Libres : {prueba.salaCine.sala.cantButacas}")
            print(f"Butacas Ocupadas : {prueba.salaCine.sala.cantButacasOcupadas}")
      
      elif opciones == '3':
            if adm.ComprobarDisponibilidad(prueba):
                  dia = int(input("Ingrese el dia de compra: "))
                  mes = int(input("Ingrese el mes de compra: "))

                  cantPersonas = int(input("Cuantas personas son: "))
                  apellido = input("\nIngrese el apellido del responsable: ")

                  adm.Comprar(prueba,cantPersonas,apellido,dia,mes)

      elif opciones == '4':
            print("\n")
            Mostrar(adm.clientes)

      elif opciones == '5':
            dia = int(input("Ingrese el dia de compra: "))
            mes = int(input("Ingrese el mes de compra: "))
            
            BuscarClientePorFecha(adm.clientes,dia,mes)

      elif (opciones == 's' or opciones == 'S'):
            opcBucle = False
else:
      print("\nGracias, vuelva pronto!")