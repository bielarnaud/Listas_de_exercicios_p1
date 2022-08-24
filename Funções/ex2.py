#definindo as silabas do Hospital!
silabas_hosp = ['shi', 'chi', 'ko', 'ku', 'ya', 'ma']

silabas_lembradas = []
silabas_faltantes = silabas_hosp


#definindo as funções
def separador_silabas(palavra):
  silabas = []
  silaba = ''

  for letra in palavra:
    
    if letra in ['a','e','i','o','u']:
      silaba = silaba + letra
      silabas.append(silaba)
      silaba = ''
    else:
      silaba = silaba + letra

  return silabas

def vericar_silabas_lembradas(silabas):
  silabas_lembradas_palavra = []

  for silaba in silabas:
    if silaba in silabas_faltantes:
      silabas_lembradas_palavra.append(silaba)
      silabas_faltantes.remove(silaba)
  
  return silabas_lembradas_palavra


#criando o laço
while len(silabas_lembradas) != 6:
  palavra = input()
  
  silabas = separador_silabas(palavra)

  silabas_lembradas_palavra = vericar_silabas_lembradas(silabas)

  #verificando a ordem
  ordem = False
  if len(silabas) == len(silabas_lembradas_palavra):
    if palavra in 'shichikokuyama':
      ordem = True


  #add as silabas lembradas da palavra asilabas lembradas
  for silaba in silabas_lembradas_palavra:
    silabas_lembradas.append(silaba)
  

  silabas_lembradas_print = ', '.join(silabas_lembradas_palavra)
  #prints
  if ordem == True and len(silabas) > 1:
    print(f'A palavra {palavra} está toda no nome do hospital. Acertou em cheio, Totoro!')
    
  elif len(silabas_lembradas_palavra) == 0:
    print('Infelizmente nenhuma dessas sílabas me lembrou do nome do hospital, Totoro.')
    
  elif  len(silabas_lembradas_palavra) == 1:
    print(f'Lembrei! A sílaba {silabas_lembradas_print} está no nome do hospital. Obrigada, Totoro!')
  
  elif  len(silabas_lembradas_palavra) > 1:
    print(f'Lembrei! As sílabas: {silabas_lembradas_print} estão no nome do hospital. Obrigada, Totoro!')

print('Conseguimos lembrar o nome do hospital shichikokuyama, agora é só pegar o Catbus e ir até lá!')
