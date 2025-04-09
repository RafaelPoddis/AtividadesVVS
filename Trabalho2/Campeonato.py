from typing import Literal

categorias = Literal["infantil", "juvenil", "adulto"]
categorias_real = ["infantil", "juvenil", "adulto"]

class Pessoa():
    __idade: int
    __categoria: categorias
    __tempo: int
    __termo: bool

    def __init__(self, idade: int, categoria: categorias, tempo: int, termo: bool):
        self.__categoria = categoria
        self.__idade = idade
        self.__tempo = tempo
        self.__termo = termo

    def registro_pessoa(self) -> bool:
        if self.__idade < 10 or self.__idade > 60: return False
        if self.__categoria not in categorias: return False
        if self.__categoria == "infantil" and self.__idade > 14: return False
        if self.__categoria == "juvenil" and self.__idade < 15: return False
        if self.__categoria == "juvenil" and self.__idade > 17: return False
        if self.__categoria == "adulto" and self.__idade < 18: return False
        if self.__tempo < 30 or self.__tempo > 180: return False
        return self.__termo