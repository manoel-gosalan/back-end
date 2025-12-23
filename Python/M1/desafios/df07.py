'''
    Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
'''
def main():

# Entrada de Dados
    nota_1 = float(input('Primeira nota: '))
    nota_2 = float(input('Segunda nota: '))

# Cálculos
    media = (nota_1 + nota_2) / 2
    
# Saída Formatada
    print('\n' + '=' * 50)
    print(f'Analisando as notas {nota_1} e {nota_2}')
    print(f'Sua média é: {media}')
    print('\nFIM DO PROGRAMA')
    
    print('=' * 50)

if __name__ == '__main__':
    main()
    