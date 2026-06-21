lista = list()

while True:
    nome = str(input("Digite o nome do aluno: "))
    nota1 = float(input("Digite a primeira nota do aluno: "))
    nota2 = float(input("Digite a segunda nota do aluno: "))
    lista.append([nome, nota1, nota2])

    continuar = input("Deseja continuar? S/N: ")
    if continuar.upper() == "N":
        break
    elif continuar.upper() == "S":
        continue

print ('-='*30)
print (f"{'Nº':<5} | {'Nome':<10} | {'Média':<10}")

for i, a in enumerate(lista):
    print (f"{i:<5} | {a[0]:<10} | {((a[1]+a[2])/2):<10.2f}")

while True:
    aluno = input("Digite o nome do aluno que você quer ver as notas (999 interrompe): ")
    if aluno == "999":
        break

    for c in lista:
        if aluno.upper() == c[0].upper():
            print (f"As notas de {aluno} foram {c[1]}, {c[2]}")