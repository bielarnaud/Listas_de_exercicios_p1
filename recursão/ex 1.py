def cont_parent (sent, cont):
  # caso base é não ter parenteses
  if '(' not in sent and ')' not in sent:
    return cont
  
  else:
    # ( é positivo
    if sent[0] == '(':
      cont += 1
    # ) é negativo 
    elif sent[0] == ')':
      cont += -1
    
    #reduzindo a string e retornando a recursão
    sent = sent[1:]
    return cont_parent(sent, cont)


# inicio do código!
n = int(input())
for i in range(n):
  sent = input()
  contador = 0
  contador = cont_parent (sent, contador)

  #organizando os prints
  if contador == 0:
    print('Essa sentença está com os parênteses balanceados, HOORAY!')
  
  elif contador > 0:
    print('A quantidade de parênteses \'(\' está maior que a de \')\', vamos descartá-la')
  
  elif contador < 0:
    print('A quantidade de parênteses \')\' está maior que a de \'(\', vamos descartá-la')