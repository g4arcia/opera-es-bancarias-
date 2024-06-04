
def menu():
    menu = """ \n
    /////////////////////////MENU/////////////////////////    

    [d]\t Depositar
    [s]\t Sacar
    [nc]\t nova conta
    [lc]\t listar contas
    [nu]\t novo usuario
    [e]\t Extrato
    [q]\t Sair

    => """
    
    
def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f'deposito:\tR$ {valor: .2f}'
        print("deposito realizado com susesso!!")
    else:
        print("XXX Operação falhou! o valor informado é invalid0! XXX")
    return saldo, extrato 

def sacar(*, saldo, valor, extrato, limite, numero_de_saques, limite_de_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_de_saques > limite_de_saques

    if excedeu_saldo:
        print("\nXXX Operação falhou! Você nao tem saldo suficiente. XXX")

    elif excedeu_saques:
        print('XXX Operação falhou! Número máximo de saques excedido')

    elif excedeu_limite:
        print('XXX Operação falhou! Número máximo de saques excedido. XXX')

    elif valor > 0:
        saldo -= valor 
        extrato += f"saque:\t\tR$ {valor: .2f}\n"
        numero_de_saques += 1 
        print('\n Saque realizado com sucesso!')

    else:
        print('\nXXX Operação falhou! O valor informado é invalido XXX')

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):

    print('\n================ EXTRATO ===================')
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo: .2f}")
    print('==============================================')
    
def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario ['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_usuario(usuarios):
    cpf = input('Informe o CPF(somente número): ')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('XXX Já existe um usuário com esse CPF! XXX')
        return
    nome = input('Informe o seu nome completo')
    data_nascimento = input('informe sua data nascimento(dd/mm/aaaa)')
    endereco = input('informe o endereço(logradouro, nro - bairro - cidade/sigla estado): )')

    usuarios.apepend({'nome': nome, 'data de nascimento': data_nascimento, 'cpf':cpf, 'endereco': endereco})

    print('=== Usuário criado com sucesso! ===')

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input('informe o CPF do usuário: ') 
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('/n=== Contacriada com sucesso!===')
        return {'agencia':agencia, 'numero_conta': numero_conta , 'usuario': usuario}

    print('\n XXX Uauário não econtrado, luxo de criação de conta encerrado! XXX')
    
def listar_contas(contas):
     for conta in contas:
         linha = f"""\
         Agência:\t\t{conta['agencia']}
         C/C:\t\t{conta['numero_conta']}
         Titular:\t{conta['usuario']['nome']}
    
        """
     print('=' * 100)

def main():
    limite_saques = 3
    agencia = "0001"

    saldo = 0
    limite = 0
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()
    
        if opcao == "d":
           valor = float(input("informe o valor do deposito"))
        
        elif valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")
        
        if opcao == "s":
            valor = float(input('informe o valor do saque: '))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_de_saques=limite_saques,
            )
        
        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)
        
        elif opcao == 'nc':
            numero_conta = len(contas)
            conta =criar_conta(agencia, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == 'lc':
            listar_contas(contas)
        
        elif opcao == 'q':
            break

        else:
            print('Operação inválida, por favor selecione novamemte a operação desejada.')