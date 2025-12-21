"""
==============================================================================
OPERADORES ARITMÉTICOS EM PYTHON - DIRETO AO PONTO
==============================================================================
Data: 20/12/2024
Objetivo: Dominar os 7 operadores aritméticos e ordem de precedência
==============================================================================
"""


print("=" * 70)
print("🚀 OPERADORES ARITMÉTICOS DO PYTHON")
print("=" * 70)

# ==============================================================================
# 1. ADIÇÃO (+)
# ==============================================================================
print("\n" + "=" * 70)
print("1️⃣  ADIÇÃO (+)")
print("=" * 70)

a = 10
b = 5
resultado = a + b

print(f"{a} + {b} = {resultado}")

# Com floats
preco1 = 15.50
preco2 = 8.30
total = preco1 + preco2

print(f"{preco1} + {preco2} = {total}")

# ==============================================================================
# 2. SUBTRAÇÃO (-)
# ==============================================================================
print("\n" + "=" * 70)
print("2️⃣  SUBTRAÇÃO (-)")
print("=" * 70)

x = 20
y = 8
resultado = x - y

print(f"{x} - {y} = {resultado}")

# Com negativos
saldo = 100
despesa = 150
resultado = saldo - despesa

print(f"{saldo} - {despesa} = {resultado}")

# ==============================================================================
# 3. MULTIPLICAÇÃO (*)
# ==============================================================================
print("\n" + "=" * 70)
print("3️⃣  MULTIPLICAÇÃO (*)")
print("=" * 70)

preco = 25
quantidade = 4
total = preco * quantidade

print(f"{preco} × {quantidade} = {total}")

# Com floats
base = 5.5
multiplicador = 3
resultado = base * multiplicador

print(f"{base} × {multiplicador} = {resultado}")

# ==============================================================================
# 4. DIVISÃO (/) - SEMPRE retorna float
# ==============================================================================
print("\n" + "=" * 70)
print("4️⃣  DIVISÃO (/) - SEMPRE retorna FLOAT")
print("=" * 70)

dividendo = 10
divisor = 2
resultado = dividendo / divisor

print(f"{dividendo} / {divisor} = {resultado} (tipo: {type(resultado).__name__})")

# Divisão não exata
a = 10
b = 3
resultado = a / b

print(f"{a} / {b} = {resultado:.4f}")

# ==============================================================================
# 5. DIVISÃO INTEIRA (//) - Retorna apenas a parte inteira
# ==============================================================================
print("\n" + "=" * 70)
print("5️⃣  DIVISÃO INTEIRA (//) - Só a parte inteira")
print("=" * 70)

dividendo = 10
divisor = 3
resultado = dividendo // divisor

print(f"{dividendo} // {divisor} = {resultado} (tipo: {type(resultado).__name__})")

# Comparando / com //
a = 17
b = 5

print("\nComparação:")
print(f"{a} / {b} = {a / b:.2f}")
print(f"{a} // {b} = {a // b}")

# ==============================================================================
# 6. MÓDULO (%) - Resto da divisão
# ==============================================================================
print("\n" + "=" * 70)
print("6️⃣  MÓDULO (%) - Resto da divisão")
print("=" * 70)

dividendo = 17
divisor = 5
resto = dividendo % divisor

print(f"{dividendo} % {divisor} = {resto}")
print(f"Porque: {dividendo} = ({divisor} × {dividendo // divisor}) + {resto}")

# Outros exemplos
print(f"\n10 % 3 = {10 % 3}")
print(f"20 % 7 = {20 % 7}")
print(f"15 % 4 = {15 % 4}")

# ==============================================================================
# 7. POTENCIAÇÃO (**) - Elevar a uma potência
# ==============================================================================
print("\n" + "=" * 70)
print("7️⃣  POTENCIAÇÃO (**)")
print("=" * 70)

base = 2
expoente = 3
resultado = base ** expoente

print(f"{base} ** {expoente} = {resultado}")
print(f"(que é o mesmo que {base} × {base} × {base})")

# Outros exemplos
print(f"\n5 ** 2 = {5 ** 2}")
print(f"3 ** 4 = {3 ** 4}")
print(f"10 ** 3 = {10 ** 3}")

# Raiz quadrada (potência fracionária)
numero = 16
raiz = numero ** 0.5
print(f"\n{numero} ** 0.5 = {raiz} (raiz quadrada de {numero})")

# ==============================================================================
# 8. ORDEM DE PRECEDÊNCIA
# ==============================================================================
print("\n" + "=" * 70)
print("⚡ ORDEM DE PRECEDÊNCIA (MUITO IMPORTANTE!)")
print("=" * 70)

print("""
ORDEM DE EXECUÇÃO (do MAIS prioritário para o MENOS):

1º lugar: **        (potenciação)
2º lugar: *, /, //, %    (multiplicação, divisões, módulo)
3º lugar: +, -       (adição, subtração)

REGRA DE OURO: Use parênteses () quando tiver dúvida!
Os parênteses têm prioridade sobre TUDO.
""")

# ==============================================================================
# EXEMPLOS DE PRECEDÊNCIA
# ==============================================================================
print("\n" + "=" * 70)
print("📚 EXEMPLOS DE PRECEDÊNCIA")
print("=" * 70)

# Exemplo 1
calculo = 2 + 3 * 4
print(f"\n1. Sem parênteses:")
print(f"   2 + 3 * 4 = {calculo}")
print(f"   Execução: 2 + (3 * 4) = 2 + 12 = {calculo}")

calculo2 = (2 + 3) * 4
print(f"\n2. Com parênteses:")
print(f"   (2 + 3) * 4 = {calculo2}")
print(f"   Execução: (5) * 4 = {calculo2}")

# Exemplo 2
calculo3 = 10 - 2 * 3
print(f"\n3. Outro exemplo:")
print(f"   10 - 2 * 3 = {calculo3}")
print(f"   Execução: 10 - (2 * 3) = 10 - 6 = {calculo3}")

# Exemplo 3 - Potenciação tem prioridade
calculo4 = 2 + 3 ** 2
print(f"\n4. Com potenciação:")
print(f"   2 + 3 ** 2 = {calculo4}")
print(f"   Execução: 2 + (3 ** 2) = 2 + 9 = {calculo4}")

# Exemplo 4 - Expressão complexa
calculo5 = 10 + 5 * 2 ** 3 - 8 / 2
print(f"\n5. Expressão complexa:")
print(f"   10 + 5 * 2 ** 3 - 8 / 2 = {calculo5}")
print(f"   Passo a passo:")
print("   → 2 ** 3 = 8")
print(f"   → 5 * 8 = 40")
print(f"   → 8 / 2 = 4.0")
print(f"   → 10 + 40 - 4.0 = {calculo5}")

# Exemplo 5 - Divisão inteira e módulo
calculo6 = 17 // 5 + 17 % 5
print(f"\n6. Com // e %:")
print(f"   17 // 5 + 17 % 5 = {calculo6}")
print(f"   Execução: (17 // 5) + (17 % 5) = 3 + 2 = {calculo6}")

# Exemplo 6 - Mesma precedência (esquerda para direita)
calculo7 = 20 / 4 * 2
print(f"\n7. Mesma precedência (executa da esquerda pra direita):")
print(f"   20 / 4 * 2 = {calculo7}")
print(f"   Execução: (20 / 4) * 2 = 5.0 * 2 = {calculo7}")

calculo8 = 20 * 4 / 2
print(f"   20 * 4 / 2 = {calculo8}")
print(f"   Execução: (20 * 4) / 2 = 80 / 2 = {calculo8}")

# ==============================================================================
# DICAS DE PRECEDÊNCIA
# ==============================================================================
print("\n" + "=" * 70)
print("💡 DICAS PRÁTICAS")
print("=" * 70)

print("""
✅ SEMPRE use parênteses quando:
   - Tiver mais de 2 operadores diferentes
   - Quiser deixar o código mais legível
   - Tiver qualquer dúvida

❌ Evite escrever expressões muito complexas em uma linha
   - Quebre em variáveis intermediárias
   - Facilita debug e leitura

Exemplos:

❌ RUIM (difícil de entender):
resultado = valor * taxa ** 2 + desconto / 100 * valor - taxa

✅ BOM (claro e legível):
taxa_ajustada = taxa ** 2
percentual_desconto = desconto / 100
resultado = valor * taxa_ajustada + (percentual_desconto * valor) - taxa
""")

# ==============================================================================
# TABELA RESUMO
# ==============================================================================
print("\n" + "=" * 70)
print("📋 TABELA RESUMO")
print("=" * 70)

print("""
Operador | Nome              | Exemplo    | Resultado | Tipo Retorno
---------|-------------------|------------|-----------|-------------
+        | Adição            | 5 + 3      | 8         | int/float
-        | Subtração         | 5 - 3      | 2         | int/float
*        | Multiplicação     | 5 * 3      | 15        | int/float
/        | Divisão           | 5 / 2      | 2.5       | float (SEMPRE)
//       | Divisão Inteira   | 5 // 2     | 2         | int
%        | Módulo (Resto)    | 5 % 2      | 1         | int
**       | Potenciação       | 5 ** 2     | 25        | int/float

PRECEDÊNCIA (maior → menor):
1. **
2. *, /, //, %
3. +, -
""")

print("=" * 70)
print("✅ FIM DO EXERCÍCIO")
print("=" * 70)
