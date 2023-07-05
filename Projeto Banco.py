menu = """
[d] Depositar
[s] Sacar 
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Digite o valor a ser depositado: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Valor inválido para depósito.")

    elif opcao == "s":
        valor = float(input("Digite o valor a ser sacado: "))
        if valor > 0:
            if saldo >= valor and numero_saques < LIMITE_SAQUES and valor <= limite:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                numero_saques += 1
                print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
            elif saldo < valor:
                print("Saldo insuficiente para realizar o saque.")
            elif numero_saques >= LIMITE_SAQUES:
                print("Limite máximo de saques diários atingido.")
            elif valor > limite:
                print("Limite máximo de saque por transação é de R$ 500.00.")
        else:
            print("Valor inválido para saque.")

    elif opcao == "e":
        print("Extrato:")
        if extrato == "":
            print("Não foram realizadas movimentações.")
        else:
            print(extrato)
        print(f"Saldo atual: R$ {saldo:.2f}")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
