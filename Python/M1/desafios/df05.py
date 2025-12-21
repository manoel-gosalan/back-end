'''
    Faça um programa que leia um número inteiro e mostre na tela o seu antecessor e sucessor
'''

def main():
    # Entrada de dados
    numero = int(input('Digite um valor: '))
    
    # Cálculos
    antecessor = numero - 1
    sucessor = numero + 1
    
    # Saída formatada
    print('\n' + '=' * 50)
    print(f'Analisando o valor {numero}')
    print(f'Seu antecessor é {antecessor}')
    print(f'Seu sucessor é {sucessor}')
    print('\nFIM DO PROGRAMA')
    print('=' * 50)

if __name__ == '__main__':
    main()
