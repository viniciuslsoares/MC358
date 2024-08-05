def subArray(a,size): 

    soma_ant = 0
    soma_atual = 0
    start = 0
    end = 0
    s = 0

    for i in range(0,size): 

        soma_atual += a[i] 

        # Atualiza a nova maior soma
        if soma_ant < soma_atual: 
            soma_ant = soma_atual 
            start = s 
            end = i 

        # Encontra uma soma negativa
        if soma_atual < 0: 
            soma_atual = 0
            s = i+1
            
        # Comparação se soma igual
        if soma_atual == soma_ant:
            num = choose_index(start, end, s, i)
            if num == 2:
                start = s
                end = i

    if start == 0 and end == 0:
        
        # Se não existe soma positiva
        print(0, 0)
    else:
        
        # Corrige o índice
        print(start+1, end+1)
    
def choose_index(i1, j1, i2, j2):
    
    # Testa as condições quando a soma é igual
    if (j1 - i1 > j2 - i2):
        return 1
    elif (j1 - i1 < j2 - i2):
        return 2
    elif (i1 < i2):
        return 1
    elif (i1 > i2):
        return 2
    
a = input()
a = list(map(int, input().split()))
subArray(a,len(a))