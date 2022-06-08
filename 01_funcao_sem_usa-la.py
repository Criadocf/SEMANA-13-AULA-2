def comprimento(n):
  qtd_elementos = 0
  for c in n:
    qtd_elementos += 1
  return qtd_elementos


def inverso(n): # [1,2,3,4,5,6]
  lista_inversa = []
  for c in n:
    lista_inversa.insert(0, c)
  return lista_inversa

def minimo(n):
  menor = 9999999
  for c in n:
    if c < menor:
      menor = c
  return menor

def maximo(n):
  maior = -9999
  for c in n:
    if c > maior:
      maior = c
  return maior

def soma(n):
  somatorio = 0
  for c in n:
    somatorio += c
  return somatorio

lista = []
while True:
  w = int(input())
  if w == 0:
    break
  lista.append(w)

c = comprimento(lista)
i = inverso(lista)
mi = minimo(lista)
ma = maximo(lista)
s = soma(lista)

def main():
    print(f'{lista}\n{c}\n{i}\n{mi}\n{ma}\n{s}')

if __name__=='__main__':
  main()
  