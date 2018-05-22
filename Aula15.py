#%% ----------------- DESAFIO 66 ------------------------
soma = 0
cont = 0
while True:
  novo =  int(input('Digite um numero (999 para parar): '))
  if novo == 999:
    break
  soma += novo
  cont += 1   
print(f'A soma dos {cont} valores é {soma}')


#%% ----------------- DESAFIO 67 ------------------------
numero = 0
while True:
  numero = int(input('Deseja ver a tabuada de qual numero?'))
  print('----------------------------------')
  if numero < 0:
    break
  for i in range(0,11):
    print(f'{numero} x {i} = {numero*i}')
  print('----------------------------------')
print('Encerrado')


#%% ----------------- DESAFIO 68 ------------------------
from random import *
print('------------- PAR OU IMPAR -----------')
n_vitorias = 0
while True:
  pc = randint(0,10)
  escolha = input('Par ou impar [P/I]?')
  jogador = int(input('Entre com um numero: '))
  soma = pc+jogador
  print(f'Voce jogou {jogador} e o computador {pc}.\nTotal = {soma}')
  if soma%2 == 0:
    jogo = 'P'
  else:
    jogo = 'I'
  if escolha == jogo:
    n_vitorias += 1
    print(f'Voce VENCEU')
    print('JOGAR NOVAMENTE...')
  else:
    print(f'Voce PERDEU')
    break
print(f'Voce ganhou {n_vitorias} vezes')


mulheres20 = 0
homens = 0
adultos = 0

while True:
  sexo = '0'
  escolha  = '0'
  print('---------------- CADASTRO -------------------')
  while sexo != 'M' and sexo != 'F':
    sexo = input('Digite o sexo da pessoa [M/F] ' ).upper()
  idade = 'a'
  while not(idade.isnumeric()):
    idade = input('Digite a idade da pessoa: ')
  idade = int(idade)
  if idade > 18:
    adultos += 1
  if sexo == 'M':
    homens += 1
  if sexo == 'F' and idade < 20:
    mulheres20 += 1
  while escolha != 'S' and escolha != 'N':
    escolha = input('Deseja continuar? [S/N] ' ).upper()
  if escolha == 'N':
    break

print(f'\nAdultos: {adultos}')
print(f'Homens: {homens}')
print(f'Mulheres abaixo dos 20: {mulheres20}') 
          
   
     
#%% ----------------- DESAFIO 70 ------------------------
maisdemil = 0
maisbarato = '0'                    
total = 0
preco0 = 0
cont = 0
print ('--------------- LOJAO DO XXT ---------------')
while True:
  escolha = '0'                    
  nome = input('Nome produto: ')                    
  preco = int(input('Preco do produto R$ '))
  if cont == 0:
      maisbarato = nome
      preco0 = preco
      cont = 1
  else:
      if preco < preco0:
          preco0 = preco
          maisbarato = nome
  if preco > 1000:
      maisdemil += 1
  total += preco   
  while escolha != 'S' and escolha != 'N':
      escolha = input('Deseja continuar? [S/N]').upper()
  if escolha == 'N':
      break
print(f'Total: {total}\nMais de R$ 1000: {maisdemil}\nProduto mais barato: {maisbarato}')
  
  
#%% -------------- DESAFIO 71 -----------------
print('------------- CAIXA DA GALERA -------------') 
while True:
    print('==================================')
    escolha = '0'
    valor = int(input('Qual valor deseja sacar? R$ '))
    c50 = valor//50
    c20 = (valor - c50*50)//20
    c10 = (valor - c50*50 - c20*20)//10
    c5 = (valor - c50*50 - c20*20 - c10*10)//5
    c2 = (valor - c50*50 - c20*20 - c10*10 - c5*5)//2
    c1 = c5 = (valor - c50*50 - c20*20 - c10*10 - c5*5 - c2*2)
    
    if c50 != 0:
        print(f'Total de {c50} cedulas de R$ 50')
    if c20 != 0:
        print(f'Total de {c20} cedulas de R$ 20')
    if c10 != 0:
        print(f'Total de {c10} cedulas de R$ 10')
    if c5 != 0:
        print(f'Total de {c5} cedulas de R$ 5')
    if c2 != 0:
        print(f'Total de {c2} cedulas de R$ 2')
    if c1 != 0:
        print(f'Total de {c1} cedulas de R$ 1')
        
    while escolha != 'S' and escolha != 'N':
        escolha = input('Deseja continuar? [S/N]').upper()
    if escolha == 'N':
        break
    print('==================================')
print('--------------------- ENCERRADO ------------------')
