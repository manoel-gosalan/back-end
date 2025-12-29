"""
Calculadora de aumento salarial
Aplica aumento de 15% e exibe o novo salário
"""

# Constante no topo facilita a manutenção
PERCENTUAL_AUMENTO = 0.15


def obter_salario():
    """
    Solicita e valida o salário do funcionário.
    Remove separadores de milhares antes da conversão.

    Returns:
        float: Salário válido informado pelo usuário
    """
    while True:
        try:
            entrada = input('Digite o salário do funcionário: € ')

            # Remove espaços e separadores de milhares comuns
            entrada_limpa = entrada.replace('.', '').replace(',', '.').replace(' ', '')
            """
            # Entrada do usuário → Após limpeza → Float resultante
                "1.100"      → "1100"       → 1100.0   ✅
                "1.100,50"   → "1100.50"    → 1100.50  ✅
                "1100"       → "1100"       → 1100.0   ✅
                "1100,50"    → "1100.50"    → 1100.50  ✅
                "1 100"      → "1100"       → 1100.0   ✅
                "1.265,00"   → "1265.00"    → 1265.0   ✅
            """

            salario = float(entrada_limpa)

            if salario < 0:
                print('⚠️  Salário não pode ser negativo. Tente novamente.')
                continue
            if salario < 1:  # Salário muito baixo, provavelmente erro de digitação
                print('⚠️  Salário parece muito baixo. Verifique o valor digitado.')
                continue

            return salario
        except ValueError:
            print('⚠️  Por favor, digite um valor numérico válido.')
            print('    Exemplos: 1265 ou 1265,00 ou 1.265,00')

def calcula_aumento(salario):
    """
       Calcula o Salario aumentado
       Args:
        salario (float): recebe o salario atual
    Returns:
        salario_atual (float): recebe o salario atual que é o padrão de 15%

    """

    return salario * (1 + PERCENTUAL_AUMENTO)

def main():
    """Função principal do programa."""
    salario_atual = obter_salario()
    salario_novo = calcula_aumento  (salario_atual)
    valor_aumento = salario_novo - salario_atual

    print(f'\n💰 Salário atual: R$ {salario_atual:.2f}')
    print(f'📈 Aumento ({PERCENTUAL_AUMENTO*100:.0f}%): € {valor_aumento:.2f}')
    print(f'✨ Novo salário: € {salario_novo:.2f}')


if __name__ == '__main__':
    main()