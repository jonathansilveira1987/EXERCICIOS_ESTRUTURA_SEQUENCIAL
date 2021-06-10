# 12. Tendo como dados de entrada a altura de uma pessoa
# construa um algoritmo que calcule seu peso ideal, 
# usando a seguinte fórmula: (72.7*altura) - 58
# Desenvolvido por Jonathan Silveira - Instagram: @jonathandev01

a = float(input('Digite sua altura: '))
f = float(72.7 * a)
pi = float(f - 58)
print(pi)