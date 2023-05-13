import random
import string

print('Bem vindo ao gerador de senhas')

#string com todas as letras
letras = string.ascii_letters
#string com todos os numeros
digitos = string.digits
#string com todos os caracteres especiais
caractes_especiais = string.punctuation

#concatenar string
alfabeto = letras + digitos + caractes_especiais

numero = input('Insira a quantidade de senhas a serem geradas: ')
numero = int(numero)

tamanho = input("Insira o tamanho que a(s) senha(s) devem ter: ")
tamanho = int(tamanho)

print('\nAqui está todas as senhas geradas:')

for sna in range(numero):
    senhas = ''
    for c in range(tamanho):
        senhas += random.choice(alfabeto)
    print(senhas)