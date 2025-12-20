"""
==============================================================================
EXERCÍCIO 02 - TIPOS PRIMITIVOS EM PYTHON
==============================================================================
Data: 18/12/2024
Objetivo: Entender e praticar os 5 tipos primitivos do Python
==============================================================================
"""

# ==============================================================================
# 1. INT (INTEIROS)
# ==============================================================================
print("=" * 50)
print("1. TRABALHANDO COM INTEIROS (int)")
print("=" * 50)

idade = 25
ano_nascimento = 1998
pontos_jogo = -10
habitantes_tokyo = 14000000

print(f"Idade: {idade}")
print(f"Ano de nascimento: {ano_nascimento}")
print(f"Pontos no jogo: {pontos_jogo}")
print(f"Habitantes de Tokyo: {habitantes_tokyo:,}")

# Operações com inteiros
soma = 10 + 5
subtracao = 10 - 3
multiplicacao = 4 * 5
divisao_inteira = 10 // 3
resto = 10 % 3
potencia = 2 ** 3

print(f"\nOperações matemáticas:")
print(f"10 + 5 = {soma}")
print(f"10 - 3 = {subtracao}")
print(f"4 * 5 = {multiplicacao}")
print(f"10 // 3 = {divisao_inteira} (divisão inteira)")
print(f"10 % 3 = {resto} (resto da divisão)")
print(f"2 ** 3 = {potencia} (potência)")

print(f"\nTipo da variável idade: {type(idade)}")

# ==============================================================================
# 2. FLOAT (PONTO FLUTUANTE)
# ==============================================================================
print("\n" + "=" * 50)
print("2. TRABALHANDO COM DECIMAIS (float)")
print("=" * 50)

preco = 199.99
temperatura = -5.5
pi = 3.14159
taxa_conversao = 0.85

print(f"Preço: R$ {preco}")
print(f"Temperatura: {temperatura}°C")
print(f"Pi: {pi}")
print(f"Taxa de conversão: {taxa_conversao}")

# Operações com float
total = 100.50 + 49.99
desconto = 199.99 * 0.10
media = (8.5 + 9.0 + 7.5) / 3

print(f"\nOperações:")
print(f"100.50 + 49.99 = R$ {total:.2f}")
print(f"Desconto de 10% em R$ 199.99 = R$ {desconto:.2f}")
print(f"Média de (8.5, 9.0, 7.5) = {media:.2f}")

# ATENÇÃO: Problema clássico de precisão!
resultado_precisao = 0.1 + 0.2
print(f"\nCUIDADO! 0.1 + 0.2 = {resultado_precisao} (problema de precisão)")

print(f"\nTipo da variável preco: {type(preco)}")

# ==============================================================================
# 3. STR (STRING)
# ==============================================================================
print("\n" + "=" * 50)
print("3. TRABALHANDO COM TEXTOS (str)")
print("=" * 50)

nome = "Rafael"
sobrenome = 'Silva'
email = "rafael@email.com"
mensagem = "Olá, mundo!"
codigo_postal = "12345-678"

print(f"Nome: {nome}")
print(f"Sobrenome: {sobrenome}")
print(f"Email: {email}")
print(f"Mensagem: {mensagem}")
print(f"CEP: {codigo_postal}")

# Operações com strings
nome_completo = nome + " " + sobrenome  # Concatenação
repetir = "Python " * 3
tamanho = len(nome)

print(f"\nOperações:")
print(f"Nome completo: {nome_completo}")
print(f"Repetir: {repetir}")
print(f"Tamanho do nome: {tamanho} caracteres")

# Acessar caracteres (índice começa em 0!)
primeira_letra = nome[0]
ultima_letra = nome[-1]
fatia = nome[0:3]

print(f"\nAcessando caracteres:")
print(f"Primeira letra: {primeira_letra}")
print(f"Última letra: {ultima_letra}")
print(f"Primeiras 3 letras: {fatia}")

# Métodos úteis de string
maiuscula = nome.upper()
minuscula = nome.lower()
substituir = email.replace("email", "gmail")
separar = "maçã,banana,laranja".split(",")

print(f"\nMétodos de string:")
print(f"Maiúscula: {maiuscula}")
print(f"Minúscula: {minuscula}")
print(f"Substituir: {substituir}")
print(f"Separar frutas: {separar}")

print(f"\nTipo da variável nome: {type(nome)}")

# ==============================================================================
# 4. BOOL (BOOLEANO)
# ==============================================================================
print("\n" + "=" * 50)
print("4. TRABALHANDO COM BOOLEANOS (bool)")
print("=" * 50)

esta_logado = True
tem_desconto = False
maior_de_idade = True

print(f"Está logado: {esta_logado}")
print(f"Tem desconto: {tem_desconto}")
print(f"Maior de idade: {maior_de_idade}")

# Comparações (retornam bool)
eh_maior = 10 > 5
eh_igual = 10 == 10
eh_diferente = 10 != 5
eh_menor_igual = 5 <= 5

print(f"\nComparações:")
print(f"10 > 5 = {eh_maior}")
print(f"10 == 10 = {eh_igual}")
print(f"10 != 5 = {eh_diferente}")
print(f"5 <= 5 = {eh_menor_igual}")

# Operadores lógicos
resultado_e = True and False
resultado_ou = True or False
resultado_nao = not True

print(f"\nOperadores lógicos:")
print(f"True and False = {resultado_e}")
print(f"True or False = {resultado_ou}")
print(f"not True = {resultado_nao}")

# Uso em condições
idade_usuario = 20
print(f"\nTeste condicional:")
if idade_usuario >= 18:
    print(f"Usuário com {idade_usuario} anos é maior de idade!")
else:
    print(f"Usuário com {idade_usuario} anos é menor de idade!")

print(f"\nTipo da variável esta_logado: {type(esta_logado)}")

# ==============================================================================
# 5. NONETYPE (NONE)
# ==============================================================================
print("\n" + "=" * 50)
print("5. TRABALHANDO COM NONE (NoneType)")
print("=" * 50)

resposta = None
usuario_logado = None

print(f"Resposta: {resposta}")
print(f"Usuário logado: {usuario_logado}")

# Verificar se é None
if usuario_logado is None:
    print("Nenhum usuário está logado no sistema!")

# Função que retorna None
def sem_retorno():
    print("Esta função não retorna nada explicitamente")

resultado_funcao = sem_retorno()
print(f"Resultado da função: {resultado_funcao}")

print(f"\nTipo da variável resposta: {type(resposta)}")

# ==============================================================================
# 6. CONVERSÃO ENTRE TIPOS (TYPE CASTING)
# ==============================================================================
print("\n" + "=" * 50)
print("6. CONVERSÃO ENTRE TIPOS (Type Casting)")
print("=" * 50)

# String para int
idade_texto = "25"
idade_numero = int(idade_texto)
calculo = idade_numero + 5

print(f"String '25' convertida para int: {idade_numero}")
print(f"Cálculo: {idade_numero} + 5 = {calculo}")

# String para float
preco_texto = "19.99"
preco_numero = float(preco_texto)

print(f"\nString '19.99' convertida para float: {preco_numero}")

# Número para string
pontos = 1000
mensagem_pontos = "Você tem " + str(pontos) + " pontos"

print(f"\nInt 1000 convertido para string: {mensagem_pontos}")

# Conversões para bool
print(f"\nConversões para bool:")
print(f"bool(0) = {bool(0)}")
print(f"bool(1) = {bool(1)}")
print(f"bool('') = {bool('')} (string vazia)")
print(f"bool('texto') = {bool('texto')}")
print(f"bool([]) = {bool([])} (lista vazia)")
print(f"bool(None) = {bool(None)}")

# ==============================================================================
# 7. CENÁRIO REAL - FORMULÁRIO DE CADASTRO
# ==============================================================================
print("\n" + "=" * 50)
print("7. CENÁRIO REAL - PROCESSAMENTO DE FORMULÁRIO")
print("=" * 50)

# Simula dados vindos de um formulário (sempre vem como string!)
nome_form = "Carlos Yamamoto"
idade_form = "28"
altura_form = "1.75"
email_form = "carlos@email.com"
aceita_termos = "True"

# Conversões necessárias
idade_convertida = int(idade_form)
altura_convertida = float(altura_form)
termos_convertido = aceita_termos == "True"

print(f"Dados do formulário:")
print(f"Nome: {nome_form} (tipo: {type(nome_form)})")
print(f"Idade: {idade_convertida} anos (tipo: {type(idade_convertida)})")
print(f"Altura: {altura_convertida}m (tipo: {type(altura_convertida)})")
print(f"Email: {email_form} (tipo: {type(email_form)})")
print(f"Aceita termos: {termos_convertido} (tipo: {type(termos_convertido)})")

# Validações
print(f"\nValidações:")
if idade_convertida >= 18:
    print("✓ Usuário é maior de idade")
else:
    print("✗ Usuário é menor de idade")

if altura_convertida >= 1.60:
    print("✓ Altura mínima atingida")
else:
    print("✗ Altura abaixo do mínimo")

if termos_convertido:
    print("✓ Termos aceitos")
else:
    print("✗ Termos não aceitos")

# ==============================================================================
# 8. PEGADINHAS CLÁSSICAS
# ==============================================================================
print("\n" + "=" * 50)
print("8. PEGADINHAS CLÁSSICAS")
print("=" * 50)

# Pegadinha 1: Concatenação vs Soma
string_numero = "5" + "3"
int_numero = 5 + 3

print(f"'5' + '3' = {string_numero} (concatenação de strings)")
print(f"5 + 3 = {int_numero} (soma de inteiros)")

# Pegadinha 2: Divisão
divisao_float = 10 / 3
divisao_int = 10 // 3

print(f"\n10 / 3 = {divisao_float} (retorna float)")
print(f"10 // 3 = {divisao_int} (retorna int)")

# Pegadinha 3: Comparar tipos diferentes
compara_string_int = ("10" == 10)
compara_string_int_convertido = (int("10") == 10)

print(f"\n'10' == 10 = {compara_string_int} (tipos diferentes)")
print(f"int('10') == 10 = {compara_string_int_convertido} (tipos iguais)")

# ==============================================================================
# FIM DO EXERCÍCIO
# ==============================================================================
