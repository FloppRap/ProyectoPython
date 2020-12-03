def modComprar(EntidadAdmin,EntidadCine,EntidadDatos):
    if EntidadAdmin.ComprobarDisponibilidad(EntidadCine):

        opc = int(input("\nSala Comun(1) o Sala Vip(2) ? "))

        if opc == 1:
                EntidadDatos.Sala = "COMUN"
        else:
                EntidadDatos.Sala = "VIP"

        dia = int(input("\nIngrese el dia de compra: "))
        while (dia < 1 or dia > 31):
                dia = int(input("Ingrese nuevamente el dia de compra: "))

        mes = int(input("\nIngrese el mes de compra: "))
        while (mes < 1 or mes > 12):
                mes = int(input("Ingrese nuevamente el mes de compra: "))

        EntidadDatos.Fecha = {dia:mes}

        EntidadDatos.Apellido = input("\nIngrese su apellido : ")

        EntidadAdmin.Comprar(EntidadCine,EntidadDatos)