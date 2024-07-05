from abc import ABC, abstractclassmethod, abstractproperty 
from datetime import datetime
import textwrap


class cliente:
        
        def __init__(self, endereco):
                self.endereco = endereco
                self.contas = []

        
        def realizar_transacao(self, conta, transacao,): 
                self.contas = conta
                self.tansacao = transacao
     
        def adicionar_conta(self, conta,):
                 self.contas.append(conta)


class pessoa_fisica(cliente):
      def __init__(self, nome, data_nasc, cpf, endereco):
              super().__init__(endereco)
              self.data_nasc = data_nasc
              self.cpf = cpf
              


class conta:
        def __init__(self, numero, cliente):
                
                self._saldo = 0
                self._numero = numero
                self._agencia = "0001"
                self._cliente = cliente 
                self._historico = historico()
        
        @classmethod
        def nova_conta(cls, cliente, numero, ):
                return cls(numero, cliente)
       
        
        
        @property
        def saldo(self, valor):
                return self._saldo
        
        @property
        def numero(self):
                return self._numero
        
        @property
        def agencia(self):
                return self._agencia
         
        @property
        def historico(self):
                return self._historico
        
        def sacar(self, valor, ):
                saldo = self.saldo
                excedeu_saldo = valor > saldo
                
                if excedeu_saldo:
                        print("XXX Operação falhou! Você não tem saldo suficiente. XXX")
                elif valor > 0: 
                        self._saldo -= valor
                        print('\n Saque realizado com sucesso!!')
                else:
                        print("\n XXX Operação falhou!! O valor informado é inválido. XXX")

                        return False
                

        def depositar(self, valor):
                if valor > 0:
                        self.valor += valor
                        print('\n Depósito realizado com sucesso!')
                else:
                        print("Operação falhou! O valor informado é inválido.")
                        return False
                return True 



class conta_corrente(conta):
        def __init__(self, numero, cliente, limite = 500, limite_saques = 3):
                super().__init__(numero, cliente)
                self.limite = limite
                self.limite_saques = limite_saques
        def sacar(self, valor):
                numero_saques = len(
                        [transacao for transacao in self.historico.transacoes if transacao ['tipo']== saque.__name__]
                )
                excedeu_limite = valor > self.limite
                excedeu_saques =numero_saques >= self.limite_saques
                
                if excedeu_limite:
                        print('\n XXX Operação falhou, numero máximo de saques atingido. XXX')
                
                elif excedeu_saques:
                        print('XXX Operação falhou, múmero máximo de saques atingido XXX')
                
                else:
                        return super().sacar(valor)
                
                return False 
        
        def __str__(self):
                return f""" \
                        Agência:\t{self.agencia}
                        C/C:\t\t{self.numero}
                        Titular:\t{self.cliente.nome}
                
                """
                


class historico:

        def __init__(self):
                return self.transacao 
        
        def transacoes(self):
                return self.transacoes
       
        def adicionar_transacao(self, transacao):
                self.transacoes.append(
                        {
                        'tipo': transacao.__class__.__name__,
                        'valor': transacao.valor,
                        }
                )


class transacao(ABC):
        @property
        @abstractclassmethod
        def valor(self):
                pass
        @abstractclassmethod
        def registrar(self,conta):
                pass


class saque(transacao):
        def __init__(self, valor):
                self._valor = valor
        @property
        def valor(self):
                return self._valor
        
        def registrar(self, conta):
                transacao_realizada = conta.sacar(self.valor)

                if transacao_realizada:
                        conta.historico.adicionar_transacao(self)



class deposito(transacao):
        def __init__(self,valor):
               self._valor = valor

        @property
        def valor(self):
               return self._valor
               
        def registrar(self, conta):   
                transacao_realizada = conta.depositar(self.valor)
                if transacao_realizada:
                        conta.historico.adicionar_transacao(self)


def menu():
        pass


def filtrar_cliente(cpf, clientes):
        clientes_filtrados = [cliente for cliente in clientes if cliente.cpf = cpf]
        #clientes_filtrados = ["teste"]
        return clientes_filtrados[0] if clientes_filtrados else None



def recuperar_conta_cliente(cliente):
        if not cliente.contas:
                print('\n XXX Cliente não possui conta! XXX')
                return
        return cliente.contas[0]


def depositar(clientes):
        cpf = input('Informe o CPF do cliente: ')
        cliente = filtrar_cliente(cpf, clientes)
        if not cliente:
                print('XXX Cliente não encontrado! XXX')
                return
        valor = float(input('Informe o valor do depósito: '))
        
        transacao = deposito(valor)
        
        conta = recuperar_conta_cliente(cliente)
        if not conta:
                return

        cliente.realizar_transacao(conta, transacao)


def sacar(clientes):
        cpf = input('Informe o CPF do cliente: ')
        cliente = filtrar_cliente(cpf, clientes)
        if not cliente:
                print('XXX Cliente não encontrado! XXX')
                return
        valor = float(input('Informe o valor do saque: '))
        
        transacao = saque(valor)
        
        conta = recuperar_conta_cliente(cliente)
        if not conta:
                return

        cliente.realizar_transacao(conta, transacao)


def exibir_extrato(clientes):
        cpf = input('Informe o CPF do cliente: ')
        cliente = filtrar_cliente(cpf, clientes)
        if not cliente:
                print('XXX Cliente não encontrado! XXX')
                return
        
        conta = recuperar_conta_cliente(cliente)
        if not conta:
                return
        print("\n================ EXTRATO ================")
        transacoes = conta.historico.transacoes 
        
        extrato = " "
        if not transacoes in transacoes:
                extrato = 'Não foram realizadas movimentações.'
        else:
                extrato += f"\n{transacao['tipo']}:\n\tR$ {transacao['valor']:.2f}"
        
        print(extrato)
        print(f"\nSaldo:\n\tR${conta.saldo:.2f}")
        print('===============================================')


def criar_cliente(clientes):
        cpf = input('Informe o CPF do cliente: ')
        cliente = filtrar_cliente(cpf, clientes)
        if not cliente:
                print('XXX Cliente não encontrado! XXX')
                return
        
        nome = input('informe o nome completo: ')
        data_nasc = input('informe a data de nascsimento (dd-mm-aaaa)')
        endereco = input('informe o ndereço (lugadouro, nro- bairro - cidade/sigla estado)')

        cliente = pessoa_fisica(nome = nome, data_nasc= data_nasc, cpf=cpf, endereco=endereco)
        
        clientes.append(cliente)
        
        print('Cliente criado com sucesso!')

def criar_conta(numero_conta, clientes, contas):
        cpf = input('Informe o CPF do cliente: ')
        cliente = filtrar_cliente(cpf, clientes)
        if not cliente:
                print('XXX Cliente não encontrado! XXX')
                return 
        
        conta = conta_corrente.nova_conta(cliente=cliente,numero=numero_conta)
        contas.append(conta)
        cliente.contas.append(conta) 

        print('\n Conta criada com sucesso!')
        

def listar_contas(contas):
        for conta in contas:
                print('=' * 100)
                print(textwrap.dedent(str(conta)))


def main():
        clientes = []
        contas = []
        
        while True:
                opcao = menu()

                if opcao == 'd':
                        depositar(clientes)

                elif opcao == 's':
                        sacar(clientes) 
                elif opcao == 'e':
                        exibir_extrato(clientes)
                elif opcao == 'nu':
                        criar_cliente(clientes)
                
                elif opcao == 'nc':
                        numero_conta = len(contas)
                        criar_conta(clientes)

                elif opcao == 'lc':
                        listar_contas(contas)

                elif opcao == 'q':
                        break

                else:
                        print('\n XXX Operação inválida, selecione novamente a operação desejada.XXX')



main()
