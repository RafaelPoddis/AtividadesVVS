class Pessoa():
    idade: int
    categoria: str
    tempo: int
    termo: bool

    def __init__(self, idade: int, categoria: str, tempo: int, termo: bool):
        self.categoria = categoria
        self.idade = idade
        self.tempo = tempo
        self.termo = termo

def registro_pessoa(pessoa: Pessoa) -> bool:
    if pessoa.idade < 10 or pessoa.idade > 60: return False
    if pessoa.categoria != "infantil" or pessoa.categoria != "juvenil" or pessoa.categoria != "adulto": return False
    if pessoa.categoria == "infantil" and pessoa.idade > 14: return False
    if pessoa.categoria == "juvenil" and (pessoa.idade < 15 or pessoa.idade > 17): return False
    if pessoa.categoria == "adulto" and pessoa.idade < 18: return False
    if pessoa.tempo < 30 or pessoa.tempo > 180: return False
    return pessoa.termo