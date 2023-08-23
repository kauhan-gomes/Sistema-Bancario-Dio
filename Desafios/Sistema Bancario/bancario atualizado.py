import textwrap

def menu():
    menu = """
    ************** Menu **************
    (1) Deposito
    (2) Saque
    (3) Extrato
    (4) Novo Usuario
    (5) Nova Conta
    (0) Sair   
    => """
    return input(menu)

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Deposito: R$ {valor:.2f}\n"
        print("Depósito bem sucedido!")
    else:
        print("Operação falhou! Valor informado é invalido")
    return saldo, extrato

def saque(*, saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES):
    
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou por falta de Saldo!")
    elif excedeu_limite:
        print("Operação falhou! Valor excede o limite!")
    elif excedeu_saques:
        print("Operação Falhou! Número maximo de saques excedidos!")
        
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque de: R$ {valor:.2f}\n"
        print("Saque bem sucedido, parabéns!!!!")
        numero_saques += 1
        
    else: 
        print("Operação Falhou! Valor informado é invalido")
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n======================= Extrato =======================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\n Saldo: R$ {saldo:.2f}")
    print("=====================================================================")

def criar_usuario(usuarios):
    cpf = input("Inform o CPF(Somente numeros): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('Já existe usuario com este CPF!')
        return
    nome = input("Informe seu nome completo: ")
    endereco = input("Informe seu endereço (logradouro, numero - Bairro - cidade/sigla do estado):")
    usuarios.append({"nome": nome, "cpf": cpf, "endereco": endereco})
    print("\nUsuario criado com sucesso, parabéns\n")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuario, sem pontos: ")
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print("\n Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuarios": usuario}
    print("\nUsuario não encontrado!")


def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []


    while True:
        opcao = menu()

        if opcao == "1":
            valor = float(input("Digite o valor do deposito: "))
            saldo, extrato = depositar(saldo, valor, extrato)
                    
        elif opcao == "2":
            valor = float(input("Informe o Valor de Saque: "))

            saldo, extrato =saque(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,numero_saques=numero_saques,
                LIMITE_SAQUES=LIMITE_SAQUES
            )

        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato)
        elif opcao == "4":
            criar_usuario(usuarios)
        elif opcao == "5":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)
            
        elif opcao == "0":
            break
        else:
            print("Operação invalida, por favor selecione novamente a operação desejada!")

main()