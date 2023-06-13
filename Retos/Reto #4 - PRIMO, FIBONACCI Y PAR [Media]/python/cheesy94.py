# Escribe un programa que, dado un número, compruebe y meustre si es primo, fibonacci y par.

def is_prime(number):
    
    for i in range(2,int(number/2)+1):    
        if is_prime(i) and number%i==0:
            return False
        
    return True

def is_fibonacci(number):
    
    fib1 = 1
    fib2 = 1
    
    while fib2<number:
        temp = fib1+fib2
        fib1 = fib2
        fib2 = temp
    
    return fib2 == number



number = 7

prime_str = "es primo," if is_prime(number) else "no es primo,"
fibo_str = "es fibonacci" if is_fibonacci(number) else "no es fibonacci,"
pair_str = "es par" if number%2==0 else "es impar"

print(number,prime_str,fibo_str,"y",pair_str)