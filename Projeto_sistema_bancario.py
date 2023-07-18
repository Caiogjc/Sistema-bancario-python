
menu = """"

   #### BANCO CG #####

    [1] Saque
    [2] Deposito
    [3] Extrato
    [4] Saldo
    [0] Cancelar Operacao
  
"""

saldo = 0
extrato = ""
quantidade_saque = 0
limite_qtd_saque = 3
LIMITE_SAQUE = 500





while True:



    opcao = input(menu)


    if opcao == "1":
        valor = float(input("Digite o valor do seu saque: "))


        if valor < 0:
            print("Digite um valor valido")

        
        elif valor > LIMITE_SAQUE:
            print("Limite de saque nao permitido")


        elif valor > saldo:
            print("Saldo insuficiente")    

        elif quantidade_saque == limite_qtd_saque:
            print("Voce passou do limite de saque diario")    

        elif valor < saldo:
            saldo = saldo - valor
            extrato += f"Saque: R$ {valor: .2f}\n"
            quantidade_saque +=  1

            print("Saque realizado!")
    

    elif opcao == "2":
        valor = float(input("Digite o valor do deposito: "))

        if valor < 0:
            print("Digite um valor valido")
            

        else:
            saldo += valor
            extrato += f"Deposito: R$ {valor: .2f}\n"
            print("Deposito realizado!")

    elif opcao == "3":

        
        print("========================\n")
        print("Conta sem movimentacao" if not extrato else extrato)
        print(extrato)
        print("\n========================")



    elif opcao == "4":

        print("############")
        print(f"Saldo atual: R${saldo: .2f}")
        print("############")


    elif opcao == "0":
        print("Operacao Encerrada!")
        break



    else:
        print("Opcao invalida, digite novamente")    

#primeiro projeto


        

