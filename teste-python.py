termo = int(input("Termo: "))
razao = int(input("Razão: "))
decimo = termo + 10 * razao
variavel = termo
while variavel != decimo:
    print(variavel, end=" -> ")
    variavel += razao
print("Fim!")
