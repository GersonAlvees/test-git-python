termo = int(input("Termo: "))
razao = int(input("Razão: "))
decimo = termo + 10 * razao
variavel = termo

print("\n")

while variavel != decimo:
    print(variavel, end=" -> ")
    variavel += razao
print("Fim!")

print("\n")

soma = 1
fatorial = 1
while soma <= termo:
    fatorial *= soma
    soma += 1
print("O fatorial de {} é {}.".format(termo, fatorial))
