
def counting_sort(arr, place):
    size = len(arr)
    output = [0] * size
    count = [0] * 10
    
    for j in arr:
        index = j // place
        count[index % 10] += 1
        
    for i in range(1, 10):
        count[i] += count[i - 1]
        
    i = size - 1
    while i >= 0:
        index = arr[i] // place
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(len(arr)):
        arr[i] = output[i]

def radix_sort(arr):
    place = 1
    valor_max = max(arr)
    while valor_max // place > 0:
        counting_sort(arr, place)

        place *= 10

if __name__ == "__main__":

    n = int(input())                        # primeira linha

    entradas = []

    for i in range(n):
        entradas.append(int(input().replace(" ", ''), 16))      # leitura das entradas como int
    radix_sort(entradas)            # ordena as entradas

    dict = {}
    for item in entradas:
        if item in dict:
            dict[item] += 1
        else:
            dict[item] = 1

    print(len(dict))                       # imprime número de únicos
    for i in dict:
        saida = str(hex(i).upper().replace("0X", ""))     # imprime os únicos em ordem
        while len(saida) < 26:
            saida = '0' + saida
        saida = f'{saida[:2]} {saida[2:10]} {saida[10:14]} {saida[14:18]} {saida[18:22]} {saida[22:]}'
        print(saida + ' ' + str(dict[i]))
