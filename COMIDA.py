class buffet:
    def __init__(self):
        self.comidas = ["Pochoclos dulces",
                        "Pochocolos salados",
                        "Papas Fritas"]

        self.gaseosas = ["Coca-Cola",
                         "Pepsi",
                         "7up"]

        self.listaPedido = []

    def comida_bebida(self):
        print(f"Comidas : {self.comidas}")

        pedido = input("Que comida desea? ")
        for k in self.comidas:
            if pedido == k:
                self.listaPedido.append(pedido)

        print(f"Bebidas {self.gaseosas}")
        
        pedido = input("Que gaseosa desea? ")
        for k in self.gaseosas:
            if pedido == k:
                self.listaPedido.append(pedido)
        
        return self.listaPedido