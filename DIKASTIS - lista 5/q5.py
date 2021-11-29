# sul leste norte oeste

def print_matriz(M):
    for i in range(len(M)):
        print(''.join(M[i]))
    print(end='')

def posso_mover(M, y_atual, x_atual, d):
    if d == 'sul':
        try:
            if M[y_atual + 1][x_atual] != '#' and M[y_atual + 1][x_atual] != 'F':
                return True
            else:
                return False
        except IndexError:
            return False
    elif d == 'leste':
        try:
            if M[y_atual][x_atual + 1] != '#' and M[y_atual][x_atual +1] != 'F':
                return True
            else:
                return False
        except IndexError:
            return False
    elif d == 'norte':
        try:
            if M[y_atual - 1][x_atual] != '#' and M[y_atual -1][x_atual] != 'F':
                return True
            else:
                return False
        except IndexError:
            return False
    else:
        try:
            if M[y_atual][x_atual - 1] != '#' and M[y_atual][x_atual -1] != 'F':
                return True
            else:
                return False
        except IndexError:
            return False

def movimentar(M, y_atual, x_atual, y_destino, x_destino): 
        if y_atual == y_destino and x_atual == x_destino:
            print_matriz(M)
            print('Conseguimos!!')
        elif posso_mover(M, y_atual, x_atual, 'sul'):
            M[y_atual + 1][x_atual] ='F'
            print_matriz(M)
            print('Por aqui meus amigos vamos pelo Sul\n')
            movimentar(M, y_atual + 1, x_atual, y_destino, x_destino)
        elif posso_mover(M, y_atual, x_atual, 'leste'):
            M[y_atual][x_atual + 1] ='F'
            print_matriz(M)
            print('Por aqui meus amigos vamos pelo Leste\n')
            movimentar(M, y_atual, x_atual +1, y_destino, x_destino)
        elif posso_mover(M, y_atual, x_atual, 'norte'):
            M[y_atual - 1][x_atual] ='F'
            print_matriz(M)
            print('Por aqui meus amigos vamos pelo Norte\n')
            movimentar(M, y_atual - 1, x_atual, y_destino, x_destino)
        elif posso_mover(M, y_atual, x_atual, 'oeste'):
            M[y_atual][x_atual -1] ='F'
            print_matriz(M)
            print('Por aqui meus amigos vamos pelo Oeste\n')
            movimentar(M, y_atual, x_atual -1, y_destino, x_destino)
        else:
            print('Amigos a jornada foi incrível, porém ela acaba por aqui...')


N = int(input())
linha1 = int(input())
coluna1 = int(input())
matriz = []
linha = []
x_destino = 0
y_destino = 0

for i in range(N):
    linha = []
    entrada = input()
    for i in entrada:
        linha.append(i)
    matriz.append(linha)

for linha in matriz:
    for caractere in linha:
        if caractere == 'O':
            x_destino += linha.index(caractere)
            y_destino += matriz.index(linha)

movimentar(matriz, linha1, coluna1, y_destino, x_destino)