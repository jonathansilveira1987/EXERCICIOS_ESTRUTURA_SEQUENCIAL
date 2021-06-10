# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que 
# calcule seu peso ideal, utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7
# Desenvolvido por Jonathan Silveira - Instagram: @jonathandev01

s = int(input('Digite seu sexo (1) para homem (2) para mulher: '))
if s == 1:
    ah = float(input('Digite sua altura: '))
    f = float(72.7 * ah)
    pi = float(f - 58)
    print ('Seu peso ideal é: ' pi)
elif s == 2:
    am = float(input('Digite sua altura: '))
    f = float(62.1 * am)
    pi = float(f - 44.7)
    print('Seu peso ideal é: ', pi 'quilos')