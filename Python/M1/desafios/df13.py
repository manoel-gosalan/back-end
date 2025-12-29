"""
Calculadora de aumento salarial
Aplica aumento de 15% e exibe o novo salário
"""

# Constante no topo facilita a manutenção
PERCENTUAL_AUMENTO = 0.15


def calcula_aumento(salario):
    """
    Calcula o salário com aumento aplicado.
    
    Args:
        salario (float): Salário atual do funcionário
    
    Returns:
        float: Salário com aumento de 15%
    """
    return salario * (1 + PERCENTUAL_AUMENTO)


def obter_salario():
    """
    Solicita e valida o salário do funcionário.
    
    Returns:
        float: Salário válido informado pelo usuário
    """
    while True:
        try:
            salario = float(input('Digite o salário do funcionário: € '))
            if salario < 0:
                print('⚠️  Salário não pode ser negativo. Tente novamente.')
                continue
            return salario
        except ValueError:
            print('⚠️  Por favor, digite um valor numérico válido.')


def main():
    """Função principal do programa."""
    salario_atual = obter_salario()
    salario_novo = calcula_aumento(salario_atual)
    valor_aumento = salario_novo - salario_atual
    
    print(f'\n💰 Salário atual: R$ {salario_atual:.2f}')
    print(f'📈 Aumento ({PERCENTUAL_AUMENTO*100:.0f}%): € {valor_aumento:.2f}')
    print(f'✨ Novo salário: R$ {salario_novo:.2f}')


if __name__ == '__main__':
    main()