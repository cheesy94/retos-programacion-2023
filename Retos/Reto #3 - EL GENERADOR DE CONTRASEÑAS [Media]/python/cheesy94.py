# Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
# - Longitud: Entre 8 y 16.
# - Con o sin letras mayúsculas.
# - Con o sin números.
# - Con o sin símbolos.

import random

# minus: 97-122
# mayus: 65-90
# nums: 48-57
# symbols: 33-47,58-64,91-96,123-126


def generate_pass(length, uppercase, numbers, symbols):
    
    password = ""
    
    pool = list(range(97,123))
    
    if uppercase:
        pool.extend(list(range(65,91)))
        
    if numbers:
        pool.extend(list(range(48,58)))
    
    if symbols:
        pool.extend(list(range(33,48)))
        pool.extend(list(range(58,65)))
        pool.extend(list(range(91,97)))
        pool.extend(list(range(123,127)))
    
    for c in range(length):
        password += chr(random.choice(pool))
    
    return password


length = 16
mayus = True
nums = True
symb = True

print(generate_pass(length,mayus,nums,symb))