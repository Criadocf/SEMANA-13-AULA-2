nome = []
altura_l = []
maior = 0

def media(m):
  s = 0
  for c in m:
    s += c
  return s/len(m)


for i in range(12):
  nome.append(str(input()))
  altura_l.append(float(input()))
  if altura_l[i] > maior:
    maior = altura_l[i]
print('JOGADOR MAIS ALTO DO TIME')
indice_maior = altura_l.index(max(altura_l))   ##CRIO UMA VARIÁVEL PRA LER OS ÍNDICES DA LISTA
print(f'{nome[indice_maior]}') #altura E CRIAR UMA RELAÇÃO, PRA PODER ACHAR O NOME RELATIVO ÀQUELA NOTA.
print(f'{max(altura_l):.2f}')
print('ALTURA MÉDIA DO TIME')
ch = media(altura_l)
print(f'{ch:.2f}')
print('JOGADORES MAIS ALTOS QUE A MÉDIA DO TIME')
for m in range(12):
  altura1 = altura_l[m]
  if altura1 > ch:
    print(f'{nome[m]}')
    print(f'{altura_l[m]:.2f}')