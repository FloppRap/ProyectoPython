from CINE import Cine
from ADMIN import Admin
from REGISTRO import BuscarClientePorFecha, GuardarRegistro

#Alguas Variables
opciones = ""
opcBucle = True
opcSala = int()
cantPersonas = int()
apellido = ""
dia = int()
mes = int()

registro = open("registro.txt","wt")
registro.write("Apellido \t Cantidad \t Fecha \n")
registro.close()




#Instancias
prueba = Cine()
prueba.salaCine.ElegirSala(1)

prueba2 = Cine()
prueba2.salaCine.ElegirSala(2)

adm = Admin()


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
            print(f"""\nSala Comun :
                  Butacas Libres -> {prueba.salaCine.sala.cantButacas}
                  Butacas Ocupadas -> {prueba.salaCine.sala.cantButacasOcupadas}
                  Incluye 3D -> {prueba.salaCine.sala.TresDe}
                  Incluye servicio de comida -> {prueba.salaCine.sala.servicioComida}""")

            print(f"""Sala Vip :
                  Butacas Libres -> {prueba2.salaCine.sala.cantButacas}
                  Butacas Ocupadas -> {prueba2.salaCine.sala.cantButacasOcupadas}
                  Incluye 3D -> {prueba2.salaCine.sala.TresDe}
                  Incluye servicio de comida -> {prueba2.salaCine.sala.servicioComida}""")
      
      elif opciones == '3':
            if adm.ComprobarDisponibilidad(prueba):

                  sala = input("Sala Comun(1) o Sala Vip(2) ? ")
                  print("")

                  if (sala == '1'):
                        dia = int(input("Ingrese el dia de compra: "))
                        while (dia < 1 or dia > 31):
                              dia = int(input("Ingrese nuevamente el dia de compra: "))

                        mes = int(input("Ingrese el mes de compra: "))
                        while (mes < 1 or mes > 12):
                              mes = int(input("Ingrese nuevamente el mes de compra: "))

                        cantPersonas = int(input("Cuantas personas son: "))
                        apellido = input("\nIngrese el apellido del responsable: ")

                        adm.Comprar(prueba,cantPersonas,apellido,dia,mes)
                  elif (sala == '2'):
                        dia = int(input("Ingrese el dia de compra: "))
                        while (dia < 1 or dia > 31):
                              dia = int(input("Ingrese nuevamente el dia de compra: "))

                        mes = int(input("Ingrese el mes de compra: "))
                        while (mes < 1 or mes > 12):
                              mes = int(input("Ingrese nuevamente el mes de compra: "))

                        cantPersonas = int(input("Cuantas personas son: "))
                        apellido = input("\nIngrese el apellido del responsable: ")

                        adm.Comprar(prueba2,cantPersonas,apellido,dia,mes)

      elif opciones == '4':
            print("\n")
            adm.MostrarClientes()

      elif opciones == '5':
            dia = int(input("Ingrese el dia de compra: "))
            while (dia < 1 or dia > 31):
                  dia = int(input("Ingrese nuevamente el dia de compra: "))
                  
            mes = int(input("Ingrese el mes de compra: "))
            while (mes < 1 or mes > 12):
                  mes = int(input("Ingrese nuevamente el mes de compra: "))
            
            print(f"\nFecha -> dia: {dia}, mes: {mes}")
            BuscarClientePorFecha(adm.clientes,dia,mes)

      elif opciones == '6':
            registro = open("registro.txt","at")
            GuardarRegistro(adm.clientes,registro)
            registro.close()

      elif (opciones == 's' or opciones == 'S'):
            opcBucle = False
else:
      print("\nGracias, vuelva pronto!")