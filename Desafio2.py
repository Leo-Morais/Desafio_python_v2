menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Criar Usuário
[5] Criar Nova Conta
[0] Sair

=> """

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Valor de R$ {valor} foi depositado\n"
        print("Deposito realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):

    if valor <= limite and valor <= saldo and numero_saques < limite_saques:
        saldo -= valor
        numero_saques += 1
        extrato += f"Saque de R$ {valor} realizado.\n"
        print("Saque realizado com sucesso!")

    elif valor > limite:
        print("Saque maior que o limite de R$500.")

    elif numero_saques == limite_saques:
        print("Limite de saque diário atingido.")

    else:
         print("Valor de saque maior que valor do saldo.")
    
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, /, *, extrato):
    if extrato != "":
        print(extrato)
        print(f"saldo total de: R${saldo:.2f}")
    else:
        print("Não foram realizadas movimentações")

def criar_usuario(usuarios):
    cpf = input("Digite seu cpf: ")
    usuario = filtar_usuario(cpf, usuarios)

    if usuario:
        print("Usuário já existente")
        return

    nome = input("Digite seu nome: ")
    data_nascimento = input("Digite sua data de nascimento(dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("Usuário criado com sucesso")

def filtar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Digite seu cpf: ")
    usuario = filtar_usuario(cpf, usuarios)

    if usuario:
        print("Conta criada com sucesso")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuarios": usuario}
    else:
        print("Usuário não encontrado")

def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    usuarios = []
    AGENCIA = "0001"
    conta = []

    while True:
        opcao = int(input(menu))
        
        if opcao == 1:

            valor =  float(input("digite o valor que deseja depositar: "))
            saldo, extrato = depositar(saldo, valor, extrato)
        
        elif opcao == 2:

            valor = float(input("Digite o valor que deseja sacar: "))
            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES
            )
        
        elif opcao == 3:
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == 4:
            criar_usuario(usuarios)

        elif opcao == 5:
            numero_conta = len(conta) +1
            criar_conta(AGENCIA,numero_conta, usuarios)
            if conta:
                conta.append(conta)

        elif opcao == 0:
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada")

main()