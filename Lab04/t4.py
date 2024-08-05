
# recorrência:
# z[i,j] = max([i+1, 0], min(dados[i], proc[j]) + z[i+1][j+1])

def print_matriz(matriz):
    for line in matriz:
        for num in line:
            print(f'{num:3}', end=' ')
        print()

def PD_dados(dados, proc):
    matriz = [[9] * len(dados) for _ in range(len(dados))]
    d = len(dados)
    # caso base:
    # não fazemos reboot no último dia
    for line in range(d):
        matriz[line][d-1] = min(dados[d-1], proc[line])
    
    for col in range(d-2, -1, -1):      # não passa pela última coluna
        for line in range(d):
            if line > col:
                matriz[line][col] = 0
            else:
                reboot = matriz[0][col+1]
                n_reboot = min(dados[col], proc[line]) + matriz[line+1][col+1]
                matriz[line][col] = max(reboot, n_reboot)
    return matriz[0][0], matriz

def extrai_caminho(matriz):
    caminho = [0]
    i, j = 0, 0
    while i < len(matriz)-1 and j < len(matriz)-1:
        if matriz[i][j] != matriz[0][j+1]:
            i += 1
            j += 1
        else:
            i = 0
            j += 1
        if i == 0: caminho.append(j)
    return caminho

n = int(input())
dados = list(map(int, input().split()))
proc = list(map(int, input().split()))
max_val, mat = PD_dados(dados, proc)
print(max_val)
print(*extrai_caminho(mat))