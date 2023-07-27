#!/bin/python

# Desafio 1: criando um sistema bancario simples com Python

menu = """
    ************************************
    **           Bem Vindo!           **
    ************************************
    **	[1] - Deposito                **
    **	[2] - Saque                   **
    **	[3] - Extrato                 **
    **	[4] - Sair                    **
    **                                **
    ************************************
    """

saldo = 500.0
limite = 500.0
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
valor_saque = 0.0
valor_a_depositar = 0.0
numero_deposito = 0

while True:

    print(menu)
    opcao = int(input(">> "))

    if opcao == 1:
        
        valor_a_depositar = float(input("Informe o valor a ser depositado: "))

        if valor_a_depositar > 0.0:
            numero_deposito += 1
            saldo += valor_a_depositar
            extrato += f"Deposito-{numero_deposito}: R$ {valor_a_depositar:.2f}, \n"
        else:
            print("Valor deve ser maior que R$ 0.00.\n\n")

        print(f"Saldo Atualizado: R$ {saldo:.2f}.\n\n")

    elif opcao == 2:
        valor_saque = float(input("Informe o valor a sacar: "))
        
        if valor_saque <= 0.0:
            print(f"Valor deve ser maior que R$ 0.00.\n\n")

        elif not numero_saques < LIMITE_SAQUES:
            print("Limite de saques diarios excedido!\nVolte amanha!\n\n")

        elif valor_saque > limite: 
            print("Valor limite excedido.\n\n") 

        elif saldo < valor_saque:
            print("Saldo insuficiente para completar a operacao.\n\n")
            
        else:    
            saldo -= valor_saque
            numero_saques += 1
            extrato += f"Saque-{numero_saques}: R$ {valor_saque:.2f}, \n"
            print("Operacao efetuada com sucesso!")
            print(f"Saldo Atualizado: R$ {saldo:.2f}.\n\n")                
        
    elif opcao == 3:
        print("============= Extrato ==============")
        print("Nao foram realizadas movimentacoes.\n" if not extrato else extrato) 
        print("====================================")
        print(f"SALDO: R$ {saldo:.2f}.")
        print("------------------------------------\n\n")

    elif opcao == 4:
        break;

    else:
        print("Erro! Operacao nao reconhecida pelo systema.\n\n")
