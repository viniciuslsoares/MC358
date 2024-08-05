def print_saida(out):
    # Imprime intervalos
    print(len(out))
    if len(out) != 0:
        for i in out:
            print(*i)

def intervalos(S, V):
    ini = 0
    fim = V
    Si = []
    out = []
    
    # Itera enquanto ini menor que fim
    while ini < fim:

        # Seleciona todos os intervalos que começam antes do início
        # Si = [i for i in S if i[0] <= ini]
        for i in S:
            if i[0] <= ini:
                Si.append(i)
            # Como está ordenado, posso parar o loop uma vez 
            # que o intervalo atual começa depois do início
            else: break

        # Se não houver intervalos que começam antes do início
        # retorna lista vazia indicando que não é possível 
        # cobrir o intervalo
        if len(Si) == 0: return []

        # S - Si
        for i in Si:
            S.remove(i)

        # Seleciona o intervalo com maior Ri
        # como está ordenado por Li, os intervalos com maior Ri
        # estão ordenados pelo Li. Dessa forma o max encontra o 
        # primeiro com maior Ri, que consequentemente é o menor Li
        aux = max(Si, key=lambda x: x[1])
        
        # Atualiza o início com o Ri do intervalo selecionado
        ini = aux[1]

        # Adiciona o intervalo selecionado à lista de saída
        out.append(aux)
        
        # Limpa a lista de intervalos que começam antes do início
        Si = []
    
    return out            


def main():
    V = int(input())
    n = int(input())
    S = []
    
    # Recebe as entradas
    for _ in range(n):
        aux = tuple(map(int, input().split()))
        S.append(aux)
        
    # Ordena os intervalos de acoro com o instante de início
    S.sort(key=lambda x: x[0])
    
    # Processamento dos intervalos
    out = intervalos(S, V)
    
    # Imprime tamanho e intervalos, um por linha
    print_saida(out)


if __name__ == '__main__':
    main()