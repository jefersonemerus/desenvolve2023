class Usuario:

    nome = None
    email = None
    senha = None
    idade = None

    def __init__(self) -> None:
        pass

    def nome_email(self):
        return self.nome + " - " + self.email

    def idade_multiplica(self, multiplica: int=0):
        if multiplica == 0:
            multiplica = 1
        return self.idade * multiplica



meu_usario = Usuario()
meu_usario.nome = "Jeferson"
meu_usario.email = "jeferson.emer@grupoboticario.com.br"
meu_usario.senha = "123"
meu_usario.idade = 30

usuario = meu_usario.nome_email()
print(usuario)

idade_nova = meu_usario.idade_multiplica(3)
print(idade_nova)

i = 0
while i < 3:
    print("teste")
    i = i + 1
