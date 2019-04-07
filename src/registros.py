class Registro:

    __slots__ = ['ano', 'placa', 'dono', 'modelo', 'ordemCadastro']

    def __init__(self, ano, placa, dono, modelo, ordemCadastro):
        self.ano = ano
        self.placa = placa
        self.dono = dono
        self.modelo = modelo
        self.ordemCadastro = ordemCadastro
    
    def __gt__(self, outro):
        if(self.ano == outro.ano):
            return self.placa < outro.placa # Ordenar em ordem alfabetica das placas

        return self.ano > outro.ano # Maior ano vem primeiro
    
    def __lt__(self, outro):
        if(self.ano == outro.ano):
            return self.placa > outro.placa # Ordenar em ordem nao-alfabetica das placas

        return self.ano < outro.ano # Maior ano vem depois