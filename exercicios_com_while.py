# Imprimir números de 1 a 10. 

i = 1
while i <= 10:
    print(i)
    i +=1

# Somar números de 1 a 100. 

i = 1
soma = 0
while i <= 100:
    soma += 1
    i += 1
print(soma)

# Imprimir números pares menores que 20. 

i = 2 
while i < 20:
    print(i)
    i += 2

# Calcular o fatorial de 5. 

n = 5
fatorial = 1
while n > 0:
    fatorial *= n
    n -= 1
print(fatorial)

# Conta números ímpares de 1 a 50. 

i = 1
contador = 0
while i <= 50:
    if i % 2 != 0:
        contador += 1
    i += 1
print(contador)

# Somar apenas números positivos digitados pelo usuário até digitar 0. 

soma = 0 
n = int(input("Digite um número (0 para sair): "))
while n != 0:
    if n > 0:
        soma += n 
    n = int(input("Digite um número (0 para sair): "))

# Imprimir a tabuada de um número qualquer. 

n = 7
i = 1
while i <= 10:
    print(f"{n} x {i} = {n*i}")
    i += 1

# Encontrar o primeiro múltiplo de 7 maior que 50. 

i = 51
while i % 7 != 0:
    i += 1
print(i)

# Reduzir um número até chegar a 1, dividindo por 2 se par ou multiplicando 3+1 se ímpar(Collatz). 

n = 10
while n != 1:
    print(n)
    if n % 2 ==0:
        n //=2
    else:
        n = 3*n +1
print(n)

# Imprimir números de 10 a 1. 

i = 10
while i > 0:
    print(i)
    i -= 1

# Contar quantos dígitos tem um número. 

n = 12345 
contador = 0
while n != 0:
    n //=10
    contador += 1
print(contador)

# Somar números pares de 1 a 50. 

i = 2
soma = 0
while i <= 50:
    soma += i 
    i +=2
print(soma)

# Imprimir todos os divisores de um número. 

n = 12
i = 1
while i <= n:
    if n % i == 0:
        print(i)
    i += 1

# Gerar sequência de Fibonacci até passar de 100. 

a, b = 0, 1
while a <= 100:
    print(a)
    a, b = b, a+b

# Continuar pedindo senha até o usuário acertar. 

senha = "1234"
entrada = ""
while entrada != senhar:
    entrada = input("Digite a senha: ")
print("Senha correta!")

# Imprimir números múltiplos de 3 até 30. 

i = 3
while i <= 30:
    print(i)
    i += 3

# Somar números ímpares até chegar a 100. 

i = 1
soma = 0
while i <= 100:
    soma += i
    i += 2
print(soma)

# Reduzir um número até que seja menor que 10. 

n = 345
while n >= 10:
    n //=10
print(n)

# Pedir números ao usuário até ele digitar negativo. 

n = int(input("Digite um número: "))
while n >= 0:
    n = int(input("Digite um número: "))
print("Número negativo digitado, fim!")

# Imprimir os números de 1 a 10, mas parar se chegar a 5. 

i= 1
while i <= 10:
    if i == 5:
        break
    print(i)
    i += 1