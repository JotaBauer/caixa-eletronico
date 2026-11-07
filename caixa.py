i = 10
saldo=500.00
deposito=0
saque=0
op=0

while i != 5:
    print('==== CAIXA ELETRÔNICO ====')

    print('1 - Consultar Saldo')
    print('2 - Realizar depósito')
    print('3 - Realizar Saque')
    print('4 - Consultar quantidade de operações')
    print('5 - Encerrar')

    i = int(input('Escolha uma opção: '))

    if i == 1:
        print(f'Seu saldo é R${saldo:.2f}')

    elif i == 2:
        deposito = float(input('Quanto deseja depositar? '))
        if deposito <= 0 :
            print('Essa quantia é indisponível')
        else:
            print(f'R${deposito} depositados com sucesso')
            saldo += deposito
            op+=1

    elif i == 3:
        saque = float(input('Quanto deseja sacar? '))
        if saque <= 0 :
            print('Essa quantia é indisponível')
        elif saque > saldo:
            print('Você não tem essa quantia de saldo')
        else:
            print('Saque realizado com sucesso')
            saldo -= saque
            op+=1

    elif i == 4:
        print(f'Foram realizadas {op} operações')

#fazendo o segundo commit requerido pela atv