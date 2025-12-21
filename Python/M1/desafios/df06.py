'''
    Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
'''

def main():
    # Entrada de dados
    numero = int(input('Digite um valor: '))
    
    # Cálculos
    dobro_do_numero = numero * 2
    triplo_do_numero = numero * 3
    
    # Cálculo da raiz quadrada com tratamento para números negativos
    if numero >= 0:
        raiz_quadrada_do_numero = numero ** 0.5
        mensagem_raiz = f'Sua raiz quadrada é: {raiz_quadrada_do_numero:.2f}'
    else:
        mensagem_raiz = 'Não existe raiz quadrada real para números negativos'
    
    # Saida Formatada
    print('\n' + '=' * 50)
    print(f'Analisando o valor {numero}')
    print(f'Seu dobro é: {dobro_do_numero}')
    print(f'Seu triplo é: {triplo_do_numero}')
    print(mensagem_raiz)
    print('\nFIM DO PROGRAMA')
    print('=' * 50)

if __name__ == '__main__':
    main()