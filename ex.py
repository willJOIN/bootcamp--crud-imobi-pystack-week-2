pessoas = []

opc = 'S'

while opc == 'S':
    print(f"Temos no arquivo {len(pessoas)} pessoas cadastradas.")
    for p in pessoas:
        print(f"{p['nome']} mora em {p['cidade']} e tem {p['idade']} anos")
    print("================")

    opc = input("Deseja cadastrar uma nova pessoa? (S/N)")
    if (opc == 'N'):
        break
    elif (opc == 'S'):
        n = {}
        n['nome'] = input("Digite o nome: ")
        n['idade'] = input("Digite a idade: ")
        n['cidade'] = input("Digite a cidade onde vive: ")
        pessoas.append(n)
        print("================")
