from CINE import Cine
from ADMIN import Admin
from REGISTRO import Registro
from DATOCLIENTE import DATOS

from moduloComprar import modComprar
from moduloDisponibilidad import disponibilidad

#Alguas Variables
opciones = ""
opcBucle = True
opcSala = int()
cantPersonas = int()
apellido = ""
dia = int()
mes = int()


#Instancias
EntidadCine = Cine()

EntidadAdmin = Admin()

EntidadDatos = DATOS()


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

            EntidadCine.DesplegarCartelera()
      
      elif opciones == '2':
            
            disponibilidad(EntidadCine)
      
      elif opciones == '3':

            print("""
                  1-Infantiles
                  2-Adolescentes
                  3-Adultos
                  """)
            
            pegi = int(input("\nIngrese una categoria : "))

            while( pegi < 1 or pegi > 3):
                  pegi = int(input("\nReingrese una categoria : "))

            if pegi == 1:
                  cont = 1
                  for peli in EntidadCine.PeliChicos:
                        print(f"{cont}-{peli}")
                        cont += 1
                  opcPeli = int(input("\nEscoja una pelicula : "))
                  EntidadDatos.Pelicula = EntidadCine.PeliChicos[opcPeli-1]

            elif pegi == 2:
                  cont = 1
                  for peli in EntidadCine.PeliAdolescentes:
                        print(f"{cont}-{peli}")
                        cont += 1
                  opcPeli = int(input("\nEscoja una pelicula : "))
                  EntidadDatos.Pelicula = EntidadCine.PeliChicos[opcPeli-1]

            else:
                  cont = 1
                  for peli in EntidadCine.PeliAdultos:
                        print(f"{cont}-{peli}")
                        cont += 1
                  opcPeli = int(input("\nEscoja una pelicula : "))
                  EntidadDatos.Pelicula = EntidadCine.PeliChicos[opcPeli-1]

            modComprar(EntidadAdmin,EntidadCine,EntidadDatos)

      elif opciones == '4':

            print("\n")
            EntidadAdmin.MostrarClientes()

      elif opciones == '5':
            
            opcBusqueda = int(input("\nBuscar por '1-Fecha' o '2-Apellido' : "))

            while (opcBusqueda < 1 or opcBusqueda > 2):
                  print("\nReingrese.\n")
                  opcBusqueda = int(input("Buscar por '1-Fecha' o '2-Apellido' : "))

            if opcBusqueda == 1:
                  print("\nBuscar por Fecha:\n")

                  dia = int(input("\nIngrese el dia de compra: "))
                  while (dia < 1 or dia > 31):
                        dia = int(input("Ingrese nuevamente el dia de compra: "))

                  mes = int(input("\nIngrese el mes de compra: "))
                  while (mes < 1 or mes > 12):
                        mes = int(input("Ingrese nuevamente el mes de compra: "))

                  Fecha = {dia:mes}

                  EntidadAdmin.BuscarPorFecha(Fecha)
                  
            else:
                  print("\nBuscar por apellido:\n")
                  apellido_a_buscar = input("\nIngrese un apellido que desea buscar : ")
                  EntidadAdmin.Buscar(apellido_a_buscar)

      elif opciones == '6':
            EntidadAdmin.Guardar()

      elif (opciones == 's' or opciones == 'S'):
            opcBucle = False
else:
      print("\nGracias, vuelva pronto!")