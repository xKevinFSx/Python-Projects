import random

while True:

    jogador = input('\nDigite uma opção:\n \nP para pedra \nA para papel \nT para tesoura\n')
    computador = random.choice(['P', 'A', 'T'])

    print(computador)

    #P < A, P > T, A < T

    if jogador == computador:
        print('\nEmpate!\n')

    if jogador == 'P' and computador == 'A':
        print('\nComputador venceu!\n') 

    if jogador == 'P' and computador == 'T':
        print('\nVocê venceu!\n') 

    if jogador == 'A' and computador == 'T':
        print('\nComputador venceu!\n') 
                
    if computador == 'P' and jogador == 'A':
        print('\nVocê venceu!\n')
                
    if computador == 'P' and jogador == 'T':
        print('\nComputador venceu!\n')
                
    if computador == 'A' and jogador == 'T':
        print('\nVocê venceu!\n')
            
    print('Deseja jogar novamente? (S/N)')
    
    resp = input()
    if resp == 'N':
        break
    
    
    
