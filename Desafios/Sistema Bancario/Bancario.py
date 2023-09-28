menu = """
    (1) Deposito
    (2) Saque
    (3) Extrato
    (4) Sair
    
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Digite o valor do deposito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n"
        else:
            print("Operação falhou! Valor informado é invalido")
    elif opcao == "2":
        valor = float(input("Informe o Valor de Saque: "))

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
            numero_saques += 1
        
        else: 
            print("Operação Falhou! Valor informado é invalido")
    elif opcao == "3":
        print("\n======================= Extrato =======================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\n Saldo: R$ {saldo:.2f}")
        print("=====================================================================")
    elif opcao == "4":
        break

    else:
        print("Operação invalida, por favor selecione novamente a operação desejada!")



