'''
    Crie um programa que leia quanto dinheiro uma pessoa tem na carteira 
    e mostre quantos dólares ela pode comprar.
    
    API utilizada: AwesomeAPI (https://docs.awesomeapi.com.br/)
    Referência: Canal Daniel Antunes (@antunesdev)
'''
import requests

def obter_cotacao_dolar():
    """
    Busca a cotação do dólar em tempo real via API.
    
    Returns:
        float: Valor da cotação USD/BRL
        None: Em caso de erro na requisição
    
    API: https://economia.awesomeapi.com.br/last/USD-BRL
    """
    try:
        url = 'https://economia.awesomeapi.com.br/last/USD-BRL'
        resposta = requests.get(url)
        dados = resposta.json()
        return float(dados['USDBRL']['bid'])
    except Exception as e:
        print(f'⚠️  Erro ao buscar cotação: {e}')
        print('📌 Usando cotação padrão: R$ 5.50')
        return 5.50

def main():
    try:
        cotacao_dolar = obter_cotacao_dolar()
        
        print('\n' + '='*50)
        print('          CONVERSOR DE REAL PARA DÓLAR')
        print('='*50)
        print(f'  💵 Cotação atual: R$ {cotacao_dolar:.2f}')
        print('='*50)
        
        # Validação de entrada
        while True:
            try:
                entrada = input('\n  Digite o valor em reais: R$ ')
                real = float(entrada)
                
                if real < 0:
                    print('  ❌ Valor não pode ser negativo!')
                    continue
                    
                break
            except ValueError:
                print('  ❌ Por favor, digite apenas números!')
        
        dolar = real / cotacao_dolar
        
        print('\n' + '-'*50)
        print(f'  ✅ R$ {real:.2f}  →  US$ {dolar:.2f}')
        print('-'*50 + '\n')
        
    except KeyboardInterrupt:
        print('\n\n  ⚠️  Programa interrompido pelo usuário.')
        print('  👋 Até logo!\n')
    
if __name__ == '__main__':
    main()