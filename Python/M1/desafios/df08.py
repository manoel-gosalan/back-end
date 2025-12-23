def formatar_numero(numero):
    """Remove .0 se o número for inteiro."""
    return int(numero) if numero == int(numero) else numero

def main():
    metros = float(input('Digite a distância em metros: '))
    
    conversoes = {
        'km': metros / 1000,
        'hm': metros / 100,
        'dam': metros / 10,
        'dm': metros * 10,
        'cm': metros * 100,
        'mm': metros * 1000
    }
    
    nomes = {
        'km': 'quilômetros',
        'hm': 'hectômetros',
        'dam': 'decâmetros',
        'dm': 'decímetros',
        'cm': 'centímetros',
        'mm': 'milímetros'
    }
    
    print('\n' + '='*50)
    print(f'A medida de {formatar_numero(metros)} metros corresponde a:')
    print('='*50)
    for unidade, valor in conversoes.items():
        print(f'{formatar_numero(valor)} {unidade}   ({nomes[unidade]})')
    print('='*50)

if __name__ == '__main__':
    main()
