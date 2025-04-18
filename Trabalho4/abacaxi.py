import re
from email_validator import validate

string = 'l' * 64 + '@' + 'd' * 63 + '.' + 'e' * 63 + '.' + 'd' * 63 + '.' + 'e' * 63 + '.com'
local_part, domain = string.split('@')

true = "true"
domain_labels = domain.split('.')
if any(len(label) > 63 for label in domain_labels):
    print("I was here")
    true = 'false'
    
print(true)
# Use a safe regex to confirm valid characters and structure
local_pattern = r'^[A-Za-z0-9!#$%&\'*+/=?^_`{|}~.-]+$'
domain_pattern = r'^[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'

print(re.match(local_pattern, local_part))
print(re.match(domain_pattern, domain))


