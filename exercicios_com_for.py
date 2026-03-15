# Imprimir os números de 1 a 20

for i in range(1, 21):
    print(i)


# Somar os números de 1 a 50

soma = 0 
for i in range(1, 51):
    soma += i
print(soma)


# Imprimir números pares de 2 a 100

for i in range(2 , 101, 2):
    print(i)


# Imprimir números ímpares de 1 a 99

for i in range(1 , 100, 2):
    print(i)


# Imprimir a tabuada do 7

for i in range(1, 11):
    print(f"7 x {i} = {7*i}")


# Calcular o fatorial de 6

fatorial = 1
for i in range(1, 7):
    fatorial *= i
print(fatorial)


# Imprimir os elementos de uma lista

lista = ["maçã", "banana", "laranja"]
for fruta in lista:
    print(fruta)


# Contar quantas vogais existem em um string

texto = "python é divertido"
vogais = "aeiou"
contador = 0 
for letra in texto.lower():
    if letra in vogais:
        contador += 1
print(contador)


# Imprimir os quadrados de 1 a 10

for i in range(1, 11):
    print(i**2)


# Imprimir a soma de números múçtiĺos de 3 até 30

soma = 0 
for i in range(1, 31, 3):
    soma +=i
print(soma)