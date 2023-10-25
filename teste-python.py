print("""
    Descubra o decimo termo e o fatorial de um termo:
    by: Gerson Alves  
""")

print("\n")

termo = int(input("Termo: "))
razao = int(input("Razão: "))
decimo = termo + 10 * razao
variavel = termo
while variavel != decimo:
    print(variavel, end=" -> ")
    variavel += razao
print("Fim!")
