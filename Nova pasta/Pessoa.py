class Pessoa:
    
    def __init__(self, nome, idade):
        
        self.nome = nome
        self.idade = idade
        self.filhos = []

    def adicionar_filho(self, filho):
        self.filhos.append(filho)

    def resumo(self):
        
        print(f'Nome: {self.nome}')
        print(f'Idade: {self.idade}')


class Pai(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)

    def adicionar_filho(self, filho):
        super().adicionar_filho(filho)
        filho.adicionar_pai(self)

    def resumo(self):
        super().resumo()
        print('Tipo: Pai')


class Mae(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)

    def adicionar_filho(self, filho):
        super().adicionar_filho(filho)
        filho.adicionar_mae(self)

    def resumo(self):
        super().resumo()
        print('Tipo: Mãe')


class Filho(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self.pai = None
        self.mae = None

    def adicionar_pai(self, pai):
        self.pai = pai

    def adicionar_mae(self, mae):
        self.mae = mae

    def resumo(self):
        super().resumo()
        print(f'Tipo: Filho')
        if self.pai:
            print(f'Pai: {self.pai.nome}')
        if self.mae:
            print(f'Mãe: {self.mae.nome}')


pai = Pai('Pedro', 55)
mae = Mae('Marlene', 39)
filho = Filho('mateus', 12)

pai.adicionar_filho(filho)
mae.adicionar_filho(filho)

print("Resumo Genérico:")
pai.resumo()
print('\n---\n')
mae.resumo()
print('\n---\n')
filho.resumo()

print("\nResumo Especializado:")
pai.resumo()
mae.resumo()
filho.resumo()