# Escribe un programa que, dado un número, compruebe y meustre si es primo, fibonacci y par.

def prime(number):
    
    for i in range(2,int(number/2)+1):    
        if prime(i) and number%i==0:
            return False
        
    return True

def fibonacci(index):
    
    if index<2:
        return 1
    
    return fibonacci(index-1)+fibonacci(index-2)

def is_fibonacci(number):
    
    index = 0
    
    while fibonacci(index)<number:
        index += 1
    
    return fibonacci(index) == number



number = 2

prime_str = "es primo," if prime(number) else "no es primo,"
fibo_str = "es fibonacci" if is_fibonacci(number) else "no es fibonacci,"
pair_str = "es par" if number%2==0 else "es impar"

print(number,prime_str,fibo_str,"y",pair_str)