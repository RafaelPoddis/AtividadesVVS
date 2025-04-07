# Aluno: Rafael Poddis
# RA: 159329
# 1 - Crie testes automatizados no pytest para uma implementação de validador de endereço de e-mail
from get_email import get_email

def test_email():
    assert get_email("normal@email.com")

def test_email_with_numbers():
    assert get_email("fulano123@email.com")

def test_short_email():
    assert get_email("a@b.com")

def test_email_without_domain():
    assert not get_email("pessoa@")

def test_email_no_end():
    assert not get_email("pessoa@email")

def test_email_without_at():
    assert not get_email("pessoaemail.com")