def ehPrimo(numero):
    i = 2
    while i < numero:
        if numero % i == 0:
            return False
        i += 1
        return True
    
inicio = int(input("Digite o início do intervalo: "))
fim = int(input("Digite o fim do intervalo: "))

contador = 0

menorPrimo = 0
maiorPrimo = 0

numero = inicio

while numero <= fim:
    if ehPrimo(numero):
        contador += 1
        if menorPrimo == 0:
            menorPrimo = numero

        maiorPrimo = numero
    numero += 1

print("Quantidade de números primos: ", contador)

if contador > 0:
    print("Menor número primo: ", menorPrimo)
    print("Maior número primo: ", maiorPrimo)
else: 
    print("Não há números primos nesse intervalo.")
    





