# Eduardo Couto

# Interface

def cria(linha,coluna):
    return [linha,coluna,{}]

def destroi():
    return None

def getElem(tadMatriz,linha,coluna):
    if linha <= quantLinhas(tadMatriz) and coluna <= quantColunas(tadMatriz):
        if (linha,coluna) in tadMatriz[2]:
            return tadMatriz[2][(linha,coluna)]
        else:
            return 0
    return print('Operação inválida.')

def setElem(tadMatriz,linha,coluna,valor):
    if linha <= quantLinhas(tadMatriz) and coluna <= quantColunas(tadMatriz):
        if valor == 0:
            if (linha,coluna)in tadMatriz[2]:
                del tadMatriz[2][(linha,coluna)]
        else:
            tadMatriz[2][(linha,coluna)] = valor
    return tadMatriz

def soma(tadMatriz1,tadMatriz2):
    newMat = cria(tadMatriz1[0],tadMatriz1[1])
    '''verificar se os tamanhos sao iguais'''
    if quantColunas(tadMatriz1) == quantColunas(tadMatriz2) and quantLinhas(tadMatriz1) == quantLinhas(tadMatriz2):
        for i in range(1,tadMatriz1[0]+1):
            for j in range(1,tadMatriz1[1]+1):
                newMat = setElem(newMat,i,j,getElem(tadMatriz1,i,j) + getElem(tadMatriz2,i,j))
    else:
        newMat = destroi()
    return newMat

def vezesK(tadMatriz, k):
    for i in range(1, tadMatriz[0] + 1):
        for j in range(1, tadMatriz[1] + 1):
            tadMatriz = setElem(tadMatriz,i,j,getElem(tadMatriz,i,j)*k)
    return tadMatriz

def multi(tadMatrizA,tadMatrizB):
    mat = cria(quantLinhas(tadMatrizA),quantColunas(tadMatrizB))
    if quantColunas(tadMatrizA) == quantLinhas(tadMatrizB):
        for i in range(1,quantLinhas(tadMatrizA)+1):
            for j in range(1,quantColunas(tadMatrizB)+1):
                for k in range(1,quantColunas(tadMatrizA)+1):
                    mat = setElem(mat,i,j,getElem(tadMatrizA,i,k)*getElem(tadMatrizB,k,j)+getElem(mat,i,j))
    return mat

def clona(tadMatriz):
    return list(tadMatriz)

def diagP(tadMatriz):
    lst = []
    if quantColunas(tadMatriz) != quantLinhas(tadMatriz):
        return None
    else:
        for i in range(1,quantLinhas(tadMatriz)+1):
           lst.append(getElem(tadMatriz,i,i))
        return lst

def diagS(tadMatriz):
    lst = []
    if quantColunas(tadMatriz) != quantLinhas(tadMatriz):
        return None
    else:
        coluna = quantColunas(tadMatriz)
        linha = 1
        while coluna >= 1 :
            lst.append(getElem(tadMatriz,linha,coluna))
            coluna -= 1
            linha += 1
        return lst

def quantLinhas(tadMatriz):
    return tadMatriz[0]

def quantColunas(tadMatriz):
    return tadMatriz[1]

def vizinhos(tadMatriz, lin, col):
    # Detectando o Esquerda Superior
    lstVizinhos = []
    if col-1 <= quantColunas(tadMatriz) and col-1 > 0 and lin-1 <= quantLinhas(tadMatriz) and lin-1 > 0:
        lstVizinhos.append(getElem(tadMatriz,lin-1,col-1))
    else:
        lstVizinhos.append(None)

    #Detectando vizinho superior
    if lin-1 <= quantLinhas(tadMatriz) and lin-1 > 0:
        lstVizinhos.append(getElem(tadMatriz,lin-1,col))
    else:
        lstVizinhos.append(None)

    #Detectando vizinho superior direito
    if lin-1 <= quantLinhas(tadMatriz) and lin-1 >0 and col+1 <= quantColunas(tadMatriz):
        lstVizinhos.append(getElem(tadMatriz,lin-1,col+1))
    else:
        lstVizinhos.append(None)

    #Detectando vizinho Direito
    if col+1 <= quantColunas(tadMatriz):
        lstVizinhos.append(getElem(tadMatriz,lin,col+1))
    else:
        lstVizinhos.append(None)

    #Detectando vizinho direito inferior
    if col+1 <= quantColunas(tadMatriz) and lin+1 <= quantLinhas(tadMatriz):
        lstVizinhos.append(getElem(tadMatriz,lin+1,col+1))
    else:
        lstVizinhos.append(None)

    #detectando vizinho inferior
    if lin+1 <= quantLinhas(tadMatriz):
        lstVizinhos.append(getElem(tadMatriz,lin+1,col))
    else:
        lstVizinhos.append(None)

    #Detectando o vizinho inferior esquerdo
    if lin+1 <= quantLinhas(tadMatriz) and col-1 > 0:
        lstVizinhos.append(getElem(tadMatriz,lin+1,col-1))
    else:
        lstVizinhos.append(None)

    #Detectando vizinho esquerdo
    if col-1 > 0:
        lstVizinhos.append(getElem(tadMatriz,lin,col-1))
    else:
        lstVizinhos.append(None)

    return lstVizinhos


def extrai(tadMatriz, lin, col, tamLin, tamCol):
    if lin+tamLin-1 <= quantLinhas(tadMatriz) and tamCol+col-1 <= quantColunas(tadMatriz):
        mat = cria(tamLin, tamCol)
        for i in range(1,tamLin+1):
            for j in range(1,tamCol+1):
                mat = setElem(mat,i,j,getElem(tadMatriz,i+lin-1,j+col-1))
        return mat
    else:
        return None

def insere(tadMatrizA, lin, col, tadMatrizB):
    if lin+quantLinhas(tadMatrizB)-1 <= quantLinhas(tadMatrizA) and quantColunas(tadMatrizB)+col-1 <= quantColunas(tadMatrizA):
        for i in range(1,quantLinhas(tadMatrizB)+1):
            for j in range(1,quantColunas(tadMatrizB)+1):
                tadMatrizA = setElem(tadMatrizA,i+lin-1,j+col-1,getElem(tadMatrizB,i,j))
        return tadMatrizA
    return None

def deslocaEsq(tadMatriz):
    mat = cria(quantLinhas(tadMatriz),quantColunas(tadMatriz))
    for i in range(1,quantLinhas(tadMatriz)+1):
        for j in range(1,quantColunas(tadMatriz)):
            mat = setElem(mat,i,j,getElem(tadMatriz,i,j+1))
    return mat

def deslocaDir(tadMatriz):
    mat = cria(quantLinhas(tadMatriz),quantColunas(tadMatriz))
    for i in range(1, quantLinhas(tadMatriz) + 1):
        for j in range(1, quantColunas(tadMatriz)):
            mat = setElem(mat,i,j+1,getElem(tadMatriz,i,j))
    return mat

def rotEsq(tadMatriz):
    mat = cria(quantLinhas(tadMatriz), quantColunas(tadMatriz))
    for i in range(1, quantLinhas(tadMatriz) + 1):
        for j in range(1, quantColunas(tadMatriz)):
            mat = setElem(mat, i, j, getElem(tadMatriz, i, j + 1))
    for i in range(1,quantLinhas(tadMatriz)+1):
        mat = setElem(mat,i,quantColunas(tadMatriz),getElem(tadMatriz,i,1))
    return mat

def rotDir(tadMatriz):
    mat = cria(quantLinhas(tadMatriz), quantColunas(tadMatriz))
    for i in range(1, quantLinhas(tadMatriz) + 1):
        for j in range(1, quantColunas(tadMatriz)):
            mat = setElem(mat, i, j + 1, getElem(tadMatriz, i, j))
    for i in range(1, quantLinhas(tadMatriz) + 1):
        mat = setElem(mat, i, 1, getElem(tadMatriz, i, quantColunas(tadMatriz)))
    return mat

def carrega(arquivo):
    arq = open(arquivo,'rt')
    linha = arq.readline()
    conteudo = []
    while linha != '':
        conteudo.append(linha.strip())
        linha = arq.readline()
    arq.close()
    matriz = []
    for linhaE in conteudo:
        numero = ''
        linha = []
        for elem in linhaE:
            if elem == ' ':
                if numero != '':
                    linha.append(int(numero))
                    numero = ''
            else:
                numero += elem
        if len(numero) != 0:
            linha.append(int(numero))
            numero = ''
        matriz.append(linha)
    mat = cria(len(matriz),len(matriz[0]))
    for i in range(1,quantLinhas(mat)+1):
        for j in range(1,quantColunas(mat)+1):
            mat = setElem(mat,i,j,matriz[i-1][j-1])
    return mat

def salva(tadMatriz,arquivo):
    mat = []
    try:
        for i in range(1,quantLinhas(tadMatriz)+1):
            linha = []
            for j in range(1,quantColunas(tadMatriz)+1):
                linha.append(getElem(tadMatriz,i,j))
            mat.append(linha)
        matNova = []
        for i in range(len(mat)):
            novaLinha = []
            for j in range(len(mat[1])):
                novaLinha.append(mat[i][j])

                if j < len(mat[1])-1:
                    novaLinha.append(' ')
            matNova.append(novaLinha)
        try:
            arqEscrita = open(arquivo, 'wt')
            for linha in matNova:
                for elem in linha:
                    arqEscrita.write(str(elem))
                arqEscrita.write('\n')
            arqEscrita.close()
            print("Arquivo",arquivo,"salvo com sucesso.")
        except:
            print("Não foi possivel salvar o arquivo.")
    except:
        print("Ocorreu um erro inesperado.")

def exibe(tadMatriz):
    for  i in range(1,quantLinhas(tadMatriz)+1):
        for j in range(1,quantColunas(tadMatriz)+1):
            print(getElem(tadMatriz,i,j),end=' ')
        print()

def main():
    print('###################\n#    TadMatriz    #\n###################')
    input("Aperte enter para sair.")

if __name__ == '__main__':
    main()