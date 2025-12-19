''' 
==================================================
EXERCÍCIO 01 - PRINT E VARIÁVEIS
==================================================
Autor: Manoel Gosalan 
Data: 18/12/2024
Objetivo: 
    # - O que é uma variável
    # - Como criar e usar variáveis
    # - Como usar o comando print()
==================================================

'''
# --------------------------------------------------
# 1. PRINT BÁSICO
# --------------------------------------------------
# O print() mostra informações na tela

print('Olá Mundo')
print('Bem-vindo ao Python!')

# --------------------------------------------------
# 2. PRINT COM STRINGS (TEXTOS)
# --------------------------------------------------
# Strings são textos entre aspas (simples ou duplas)

print('7' + '4')  # Junta textos: '7' e '4' = '74'
print('Python' + ' ' + 'é' + ' ' + 'incrível')

# --------------------------------------------------
# 3. PRINT COM NÚMEROS
# --------------------------------------------------
# Sem aspas, Python entende como números e faz cálculos

print(7 + 4)  # Soma: 11
print(10 - 3)  # Subtração: 7
print(5 * 2)  # Multiplicação: 10
print(20 / 4)  # Divisão: 5.0

# --------------------------------------------------
# 4. O QUE É UMA VARIÁVEL?
# --------------------------------------------------
# Variável é como uma caixa que guarda informações
# Você dá um nome para a caixa e coloca algo dentro

nome = 'Carlos'  # Variável 'nome' guarda o texto 'Carlos'
idade = 25  # Variável 'idade' guarda o número 25

# Agora podemos usar essas variáveis
print(nome)
print(idade)

# --------------------------------------------------
# 5. CRIANDO E USANDO VARIÁVEIS
# --------------------------------------------------

# Variáveis com textos (strings)
cidade = 'Tokyo'
pais = 'Japão'
empresa = 'Sony'

print(cidade)
print(pais)
print(empresa)

# Variáveis com números
ano = 2024
dia = 18
temperatura = 23

print(ano)
print(dia)
print(temperatura)

# --------------------------------------------------
# 6. OPERAÇÕES COM VARIÁVEIS
# --------------------------------------------------

# Podemos fazer contas com variáveis
numero1 = 10
numero2 = 5

print(numero1 + numero2)  # 15
print(numero1 - numero2)  # 5
print(numero1 * numero2)  # 50
print(numero1 / numero2)  # 2.0

# Podemos juntar textos de variáveis
primeiro_nome = 'Takeshi'
ultimo_nome = 'Yamamoto'

print(primeiro_nome + ' ' + ultimo_nome)  # Takeshi Yamamoto

# --------------------------------------------------
# 7. VARIÁVEIS PODEM MUDAR DE VALOR
# --------------------------------------------------

pontos = 0
print(pontos)  # 0

pontos = 10
print(pontos)  # 10

pontos = 100
print(pontos)  # 100

# --------------------------------------------------
# 8. PRINT COM MENSAGENS E VARIÁVEIS
# --------------------------------------------------

usuario = 'Rafael'
score = 850

# Jeito 1: Concatenar (juntar) com +
print('Jogador: ' + usuario)
print('Pontuação: ' + str(score))  # str() converte número para texto

# Jeito 2: Usar vírgula (mais fácil!)
print('Jogador:', usuario)
print('Pontuação:', score)

# Jeito 3: f-string (o melhor jeito!)
print(f'Jogador: {usuario}')
print(f'Pontuação: {score}')
print(f'{usuario} fez {score} pontos!')

# --------------------------------------------------
# 9. MÚLTIPLAS VARIÁVEIS
# --------------------------------------------------

# Criar várias variáveis de uma vez
x, y, z = 10, 20, 30

print(x)  # 10
print(y)  # 20
print(z)  # 30

# Variáveis com o mesmo valor
a = b = c = 100

print(a)  # 100
print(b)  # 100
print(c)  # 100

# --------------------------------------------------
# 10. REGRAS PARA NOMES DE VARIÁVEIS
# --------------------------------------------------

# ✅ CORRETO
nome_completo = 'João Silva'
idade2 = 30
_privado = 'secreto'
numeroTelefone = '123456'

# ❌ ERRADO (não use!)
# 2idade = 30  # Não pode começar com número
# nome-completo = 'João'  # Não pode ter traço
# nome completo = 'João'  # Não pode ter espaço

# --------------------------------------------------
# FIM DO EXERCÍCIO 01
# --------------------------------------------------