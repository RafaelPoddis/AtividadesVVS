# Aluno: Rafael Poddis
# RA: 159329
# 1 - Crie testes automatizados no pytest para uma implementação de validador de endereço de e-mail

import re

def get_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email) is not None