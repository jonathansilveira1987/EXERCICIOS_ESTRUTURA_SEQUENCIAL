# 12. Tendo como dados de entrada a altura de uma pessoa
# construa um algoritmo que calcule seu peso ideal, 
# usando a seguinte fórmula: (72.7*altura) - 58
# Desenvolvido por Jonathan Silveira - Instagram: @jonathandev01

a = float (input('Digite a altura: '))
pi = ((72.7 * a) - 58)
print ('Seu peso ideal é: '), round((72.7*pi)-58, 2), 'kg')