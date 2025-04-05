# Aluno: Rafael Poddis
# RA: 159329
# 1 - Crie testes automatizados no pytest para uma implementação de validador de endereço de e-mail

import re

def get_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email) is not None

def test_valid_email():
    assert get_email("fulano123@email.com")
    assert get_email("alguem@email.com")

def test_invalid_email():
    assert not get_email("fulano123email.com.br")
    assert not get_email("alguememail.com")
    assert not get_email("pessoa@email")