from CINE import Cine
from ADMIN import Admin

#Alguas Variables
opciones = ""
opcBucle = True
opcSala = int()
cantPersonas = int()


"""
print(f"Clientes maximos en la fecha correspondiente : {prueba.cantClientes}")
"""

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
            1.Ver Cartelera
            2.Ver Disponibilidad
            3.Comprar
            4.Guardar Registro de Clientes
            5.Mostrar Registro de Clientes
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
                  cantPersonas = int(input("Cuantas personas son: "))
                  adm.Comprar(prueba,cantPersonas)
      elif opciones == '4':
            adm.GuardarRegistroClientes(prueba)
      elif opciones == '5':
            adm.VerRegistroClientes(prueba)
      elif (opciones == 's' or opciones == 'S'):
            opcBucle = False
else:
      print("\nGracias, vuelva pronto!")