"""
Calculadora de desconto de produtos de 5%. Solicita preço e Aplica desconto configurável e exibe o novo preço
"""

# Constantes no topo - fácil de manter e modificar
PERCENTUAL_DESCONTO = 0.05

def calcular_preco_com_desconto(valor_original, desconto=PERCENTUAL_DESCONTO):
    """
    Calcula o preço final após aplicar desconto.
    
    Args:
        valor_original: Preço original do produto
        desconto: Percentual de desconto (padrão: 5%)
    
    Returns:
        Preço final com desconto aplicado
    """
    return valor_original * (1 - desconto)


def obter_valor_produto():
    """Solicita e valida o valor do produto."""
    while True:
        try:
            valor = float(input('Digite o valor do produto: € '))
            if valor < 0:
                print('⚠️  Valor não pode ser negativo. Tente novamente.')
                continue
            return valor
        except ValueError:
            print('⚠️  Por favor, digite um valor numérico válido.')


def main():
    """Função principal do programa."""
    valor_produto = obter_valor_produto()
    novo_preco = calcular_preco_com_desconto(valor_produto)
    
    economia = valor_produto - novo_preco
    
    print(f'\n💰 Preço original: € {valor_produto:.2f}')
    print(f'🎉 Desconto ({PERCENTUAL_DESCONTO*100:.0f}%): € {economia:.2f}')
    print(f'✨ Preço final: € {novo_preco:.2f}')


if __name__ == '__main__':
    main()