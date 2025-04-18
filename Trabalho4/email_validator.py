import re

"""
Os ifs testados nas linhas 22, 17, 14 e 25 não podem ser verificas pois os testes não estão corretos.
Esses testes realizam as mesmas verificações 2 vezes, ou seja, mesmo que o mutatest troque um if para false, 
a segunda verificação vai continuar falhando. Sem alterar essas estruturas no código, não há como aumentar a cobertura 
das mutações.
"""
def validate(email):
    
    if not email or not isinstance(email, str):
        return False

    if '@' not in email or email.count('@') != 1:
        return False

    if len(email) > 320:
        return False
    
    local_part, domain = email.split('@')

    if not local_part or not domain:
        return False

    if len(local_part) > 64 or len(domain) > 255:
        return False

    # Local part rules
    if '..' in local_part or local_part.endswith('.') or ' ' in local_part:
        return False

    # Domain part rules
    domain_labels = domain.split('.')
    if any(len(label) > 63 for label in domain_labels):
        print("I was here")
        return False

    # Use a safe regex to confirm valid characters and structure
    local_pattern = r'^[A-Za-z0-9!#$%&\'*+/=?^_`{|}~.-]+$'
    domain_pattern = r'^[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'

    if not re.match(local_pattern, local_part):
        return False

    if not re.match(domain_pattern, domain):
        return False
    

    return True