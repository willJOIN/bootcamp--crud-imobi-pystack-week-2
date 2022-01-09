nome = "Caio"

# Saída de Dados
# Print data type
print(type(nome))

# Concatenação de String
print("Olá" + nome + ", tudo bem?")

# Print Format de String
print(f"Olá {nome}, tudo bem?")

# Entrada de Dados
nome = input("Digite seu nome: ")
print(f"Olá {nome}, sua idade é {idade}")

# Soma e cast int
n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
print(n1 + n2)

# Operadores Aritméticos
# Soma +
# Divisão /
# Divisão por inteiro, ou sem casas decimais //
# Exponenciação **
# Resto da Divisão ou Módulo %
# Raíz quadrada importar math e usar sqrt ou elevar a 1/2

# Operadores Relacionais
# Atribuição =
# Comparação ==
# Menor <
# Maior >
# Menor e igual <=
# Maior e igual >=

# Operadores Lógicos
if 1 == 2:
    print('if')
elif 2 == 3:
    print('elif')
else:
    print('else')

nota1 = float(input('Digite uma nota: '))
nota2 = float(input('Digite outra nota: '))
media = (nota1 + nota2) / 2
if media >= 6:
    print('APROVADO')
elif media >= 4 and media < 6:
    print('RECUPERAÇÃO')
elif media < 4:
    print('REPROVADO')

# Match Case, substituto do Switch Case no Python


def f(x):
    match x:
        case 'a':
            return 1
        case 'b':
            return 2
        case _:
            return 0


# Laço While
x = 0
while x < 100:
    print(x)
    continue  # Volta pro topo do loop e ignora as próximas linhas
    x += 1  # Incrementa um a x
    sleep(0.5)  # Esperar meio segundo

# Print tabuada do 5 inteira
x = 0
while x < 10:
    print(f"5 * {x} = {x * 5}")
    x += 1

# Começa no 2, vai até 10, com step de 2 em 2
for i in range(2, 10, 2):
    print(i)

for i in range(0, 3):
    for j in range(0, 3):
        print(f"{i} x {j} = {i * j}")

for i in range(1, 11):
    print(f'==========[TABUADA DO {i}===========')
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")

# Listas
notas = [6, 7, 8, 2, 9, 3]
#        0  1  2  3  4  5
# Adiciona 8 na posição 6
notas.append(8)
# Remove último da lista
notas.pop()
# Print tamanho
print(len(notas))

lista = []
while True:
    nota = int(input('Digite uma nota ou -1 para sair: '))
    if nota == -1:
        break
    else:
        lista.append(nota)
print(lista)

soma = 0
for nota in lista:
    soma += nota
print("Soma: " + nota)
print("Média: " + nota / len(lista))

# Dicionário
pessoa = {'nome': 'Caio Sampaio',
          'idade': 21,
          'cidade': 'Franca'}

print(pessoa['cidade'])
