menu = """
[D] Depositar
[S] Sacar
[E] Extrato
[Q] Sair

Digite aqui: """

N_LIMITE_SAQUES_DIARIOS = 3
saldo = 0
limite_saque = 500
extrato = ""
n_saques = 0

while True:
    opcao = input(menu)

    if opcao in ["s", "S"]: #Sacar
        valor = float(input("Informe o valor do saque: "))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite_saque
        excedeu_saques = n_saques >= N_LIMITE_SAQUES_DIARIOS
        if excedeu_saldo:
            print(f"Saque falhou! Você não tem saldo suficiente. Saldo R${saldo:.2f}")
        elif excedeu_limite:
            print("Saque falhou! Você ultrapassou o valor de saque de R$500.00")
        elif excedeu_saques:
            print("Saque falhou! Você atingiu o limite de saques diários.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque R${valor:.2f}\n"
            n_saques += 1
        else:
           print("Saque falhou! O valor informado é inválido.")

    elif opcao in ["d", "D"]: #Depositar
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito R${valor:.2f}\n"
        else:
            print("Deposito falhou! O valor informado é inválido.")

    elif opcao in ["e", "E"]: #Extrato
        print("\n================ EXTRATO ================")
        if not extrato:
            print("Não foram realizadas movimentações na conta.")
            print(f"\nSaldo: R${saldo:.2f}")
            print("=========================================")
        else:
            print(extrato)
            print(f"\nSaldo: R${saldo:.2f}")
            print("=========================================")

    elif opcao in ["q", "Q"]: #Sair
        break
    else:
        print("Operação inválida! Selecione novamente.")