class Automovel:

    combustivel = None
    cor = None
    
    def __init__(self) -> None:
        pass

    def Acelerar(self):
        return "Aceleraaaa"

    def Parar(self):
        pass

class Carro(Automovel):

    def __init__(self) -> None:
        pass

    def Acelerar(self):
        return "Acelera de novo"


meu_carro = Carro()
meu_carro.combustivel = "Gasolina"

print(meu_carro.Acelerar())
