import tadPainel
import tadMatriz
import tadGol
import tkinter


#   Esta função pode ser utilizada para adicionar 
#	celulas em cordenadas especificas da matriz.
def criaCells(linhas,colunas):
    lst = []
    aux = True
    matriz = tadMatriz.cria(linhas,colunas)
    while aux:
        linha = input("Digite o numero da linha ou espaço para sair: ")
        coluna = input(("Digite o numero da coluna: "))
        if linha != '':
            lst.append((int(linha),int(coluna)))
        else:
            aux = False
    for elem in lst:
        mat = tadMatriz.setElem(matriz,elem[0],elem[1],1)
    return matriz


#	Função principal
def main():
	# Receita de bolo do tkinter
    janela = tkinter.Tk()
    janela.title("Game of life by Eduardo")
	
	# Altura da tela
    canvas_altura = 650
	# Largura da tela
    canvas_largura = 1300

    #Quantidade de quadrados
    quadrados_linha = 60
    quadrados_coluna = 130
	
    tela = tkinter.Canvas(janela, bg='white', width=canvas_largura, height=canvas_altura)
	# Monta os elementos da tela
    tela.pack()
	# Criação do tadPainel
    painel = tadPainel.cria(20,20,quadrados_linha,quadrados_coluna,8,8,1,'gray','black','white')

    # Criando uma Matriz
    mat = tadMatriz.cria(quadrados_linha,quadrados_coluna)

    """ Menu """
    print('###################\n#  Game of life no Tkinter  #\n#  By Eduardo     #\n###################')
    print("Padroes disponiveis: \narcon, beacon, blinker, glider,\ngosperglider, gosperglider2, pesado1, pulsar,\nrpentomino, toad.\n")


    rodar = 1
    while rodar:
        nomeArquivo = input("Digite o nome do padrao inicial: ")
        try:
            cells = tadMatriz.carrega(nomeArquivo+".txt")
            rodar = 0
        except:
            print("\n-> Erro ao abrir arquivo\n Verifique se o arquivo está na raiz do projeto.\n")
	
    comecox = int(input("Digite a cordenada X de inicio: ") )
    comecoy = int(input("Digite a cordenada Y de inicio: "))

    atualiza = []
	
    gol = tadGol.cria(mat,cells,comecox,comecoy)

    for i in range(1, tadMatriz.quantLinhas(gol) + 1):
        for j in range(1, tadMatriz.quantColunas(gol) + 1):
            status = tadMatriz.getElem(gol, i, j)
            if status == 1:
                tadPainel.onoff(i, j, painel, tela, True)
            else:
                tadPainel.onoff(i, j, painel, tela, False)
    interacoes = 1
	
    while True:
        
        if len(atualiza) != 0:
            for elem in atualiza:
                tadPainel.onoff(elem[0], elem[1], painel, tela, bool(elem[2]))

        tela.update()
        gol,atualiza = tadGol.proxGerecao2(gol)

    janela.mainloop()
    return 0
	
if __name__ == '__main__':
    main()
