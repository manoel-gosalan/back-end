'''
    Escreva um programa que leia a largura e altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².
'''
def main ():
    
    # Entrada de dados:
    altura = float(input('Altura da parede: '))
    largura = float(input('Largura da parede: '))
    
    # Tratamento de dados
    if altura <= 0 or largura <= 0:
        print('Valores invalidos por favor verifique novamene')
        return # Para a funcao
    
    #Calculo da função principal
    area_total = altura * largura
    litros = area_total / 2
    
    
    print(f'Analisando a altura da sua parede de: {altura} m², e {largura}m² de largura.')
    print(f'a area total da parede e de {area_total}m²')
    print(f'Sera preciso {litros}L de tinta para pintar a parede toda')
    
    
    
if __name__ == '__main__':
    main() 