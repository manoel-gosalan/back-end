'''
Faça um script que leia algo na tela e mostre o sey tipo primitivo e todas as informações possiveis sobre ele.
'''

digitacao_do_usuario = input('Digite algo: ')

print(f'o tipo primitivo de {digitacao_do_usuario} é: {type(digitacao_do_usuario)}')
print(f'    É numérico? {digitacao_do_usuario.isnumeric()}')
print(f'    É alfabético? {digitacao_do_usuario.isalpha()}')
print(f'    É alfanumérico? {digitacao_do_usuario.isalnum()}')
print(f'    Está em maiúscula? {digitacao_do_usuario.isupper()}')
print(f'    Está em minúscula? {digitacao_do_usuario.islower()}')
print(f'    Começa com maiúscula? {digitacao_do_usuario.istitle()}')
print(f'    Só tem espaços? {digitacao_do_usuario.isspace()}')


