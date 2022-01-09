# Tipos de Dados

################
# Saída de Dados
nome = "William"
# Print Tipo de Dado
print(type(nome))
# Print Tamanho do Dado
print(len(nome))
# Concatenação de String
print("Olá" + nome + ", tudo bem?")
# Print Format de String
print(f"Olá {nome}, tudo bem?")
###############################

##################
# Entrada de Dados
nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
print(f"Olá {nome}, sua idade é {idade}.")
""" Exemplo:
Soma com Cast Int """
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
print("A soma do primeiro número com o segundo é:" + n1 + n2)
#############################################################

########################
# Operadores Aritméticos
n1 = 1
n2 = 2
# Soma 
print(n1 + n2)
# Divisão 
print(n1 / n2)
# Divisão por inteiro ou sem casas decimais 
print(n1 // n2)
# Resto da Divisão ou Módulo 
print(n1 % n2)
# Exponenciação 
print(n1 ** n2)
# Raíz Quadrada 
import math
n1 = 1
print(math.sqrt(n1))
print(n1 ** 0.5)
################

########################
# Operadores Relacionais
n1 = 1
n2 = 2
# Atribuição 
n1 = 1
# Comparação 
n1 == n2
n1 != n2
# Maior
n1 > n2
# Maior e Igual 
n1 >= n2
# Menor
n1 < n2
# Menor e Igual
n1 <= n2
########

####################
# Operadores Lógicos
n1 = 1
n2 = 2
n3 = 3
if n1 == n2:
    print('primeiro caso')
elif n1 == n3:
    print('segundo caso')
else:
    print('outros casos')
# Exemplo:
# Média com Cast Float
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
if media >= 6:
    print('Aprovado')
elif media >= 4 and media < 6:
    print('Recuperação')
elif media < 4:
    print('Reprovado')
# Match Case, substituto do Switch Case no Python
x = 'a'
match x:
    case 'a':
        print('Caso 1')
    case 'b':
        print('Caso 2')
#######################

#################
# Laços Temporais
# Laço While
import time
x = 0
while x < 100:
    print(x)
    x += 1  # Incrementa um a x
    time.sleep(0.5)  # Esperar meio segundo
    continue  # Volta pro topo do loop e ignora as próximas linhas
# Exemplo:
# Tabuada do 5 
x = 0
while x < 10:
    print(f"5 x {x} = {x * 5}")
    x += 1
# Laço For 
# Começa no 2, vai até 10, com step de 2 em 2
for i in range(2, 10, 2):
    print(i)
# Exemplo:
# Todas as tabuadas
for i in range(1, 11):
    print(f'==========[TABUADA DO {i}==========')
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")
#####################################

########
# Listas
notas = [6, 7, 8, 2, 9, 3]
#        0  1  2  3  4  5
# Adiciona 8 na posição 6
notas.append(8)
# Remove último da lista
notas.pop()
# Exemplo
# Manipulando notas em uma lista de notas
lista_notas = []
while True:
    nota = int(input('Digite uma nota ou -1 para sair: '))
    if nota == -1:
        break
    else:
        lista_notas.append(nota)
print('Todas as notas: ' + lista_notas)
soma = 0
for nota in lista_notas:
    soma += nota
print('Soma: ' + nota)
print('Média: ' + nota / len(lista_notas))
##########################################

############
# Dicionário
pessoa = {'nome': 'Caio Sampaio',
          'idade': 21,
          'cidade': 'Franca'}
print(pessoa['cidade'])
#######################

#########
# Funções
def main():
    primeiraFuncao()
    segundaFuncao()
def primeiraFuncao():
    pass
def segundaFuncao():
    pass
main()
######
