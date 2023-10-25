termo = int(input("Termo: "))
razao = int(input("Razão: "))
decimo = termo + 10 * razao
variavel = termo
while variavel != decimo:
    print(variavel, end=" -> ")
    variavel += razao
print("Fim!")

soma = 1
fatorial = 1
while soma <= termo:
    fatorial *= soma
    soma += 1
print("O fatorial de {} é {}.".format(termo, fatorial))
