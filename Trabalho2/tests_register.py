from Campeonato import Pessoa

def test_valid_register():
    
    pessoa = Pessoa(idade = 15, categoria = 'juvenil', tempo = 45, termo = True)

    registro = pessoa.registro_pessoa()

    assert registro

def test_invalid_age():
    pessoa = Pessoa(idade = 450, categoria = 'juvenil', tempo = 45, termo = True)

    registro = pessoa.registro_pessoa()

    assert not registro

def test_incorrect_category():

    pessoa = Pessoa(idade = 26, categoria = 'adulto', tempo = 10, termo = True)

    registro = pessoa.registro_pessoa()
    
    assert not registro


def test_incorrect_estimated_time():

    pessoa = Pessoa(idade = 26, categoria = 'adulto', tempo = 5, termo = True)

    registro = pessoa.registro_pessoa()
    
    assert not registro


def test_document_not_signed():

    pessoa = Pessoa(idade = 26, categoria = 'adulto', tempo = 150, termo = False)

    registro = pessoa.registro_pessoa()
    
    assert not registro