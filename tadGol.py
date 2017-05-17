#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  tadGol.py
#
#  Autor: Eduardo Couto Rodrigues <eduardocooouto@gmail.com>
#  Criado em: 25/05/16
#  Usuário: Eduardo Couto
#
#  Função do programa:
#  Versão inicial: 1.0
#  ----------------------------------------------------------------
import tadMatriz

def cria(tad_matriz,celulas,linha,coluna):

    for i in range(1,tadMatriz.quantLinhas(celulas)+1):
        for j in range(1,tadMatriz.quantColunas(celulas)+1):
            tad_matriz = tadMatriz.setElem(tad_matriz,(linha-1)+i,(coluna-1)+j,tadMatriz.getElem(celulas,i,j))
    return tad_matriz

def destroi():
    return None

def vizinhosVivos(lst):
    vivos = 0
    for elem in lst:
        if elem == 1:
            vivos +=1
    return vivos

def proxGerecao(tadGol):
    '''
    As regras são simples e elegantes:
    1. Qualquer célula viva com menos de dois vizinhos vivos morre de solidão.
    2. Qualquer célula viva com mais de três vizinhos vivos morre de superpopulação.
    3. Qualquer célula morta com exatamente três vizinhos vivos se torna uma célula viva.
    4. Qualquer célula viva com dois ou três vizinhos vivos continua no mesmo estado para a próxima geração.
    '''
    lstAtualiza = []
    for i in range(1,tadMatriz.quantLinhas(tadGol)+1):
        for j in range(1,tadMatriz.quantColunas(tadGol)+1):
            quantVizinhos = vizinhosVivos(tadMatriz.vizinhos(tadGol,i,j))

            # Se estiver viva
            if tadMatriz.getElem(tadGol,i,j) == 1:
                if quantVizinhos < 2:
                    '''Qualquer célula viva com menos de dois vizinhos vivos morre de solidão.'''
                    lstAtualiza.append((i,j,0))
                elif quantVizinhos > 3:
                    '''Qualquer célula viva com mais de três vizinhos vivos morre de superpopulação.'''
                    #Morre de super população
                    lstAtualiza.append((i,j,0))
                elif quantVizinhos == 2 or quantVizinhos == 3:
                    '''Qualquer célula viva com dois ou três vizinhos vivos continua no mesmo estado para a próxima geração.'''
                    lstAtualiza.append((i,j,tadMatriz.getElem(tadGol,i,j)))
            else:
                if quantVizinhos == 3:
                    '''Qualquer célula morta com exatamente três vizinhos vivos se torna uma célula viva.'''
                    lstAtualiza.append((i,j,1))
    for item in lstAtualiza:
        tadGol = tadMatriz.setElem(tadGol,item[0],item[1],item[2])



    return tadGol

def proxGerecao2(tadGol):
    '''
    As regras são simples e elegantes:
    1. Qualquer célula viva com menos de dois vizinhos vivos morre de solidão.
    2. Qualquer célula viva com mais de três vizinhos vivos morre de superpopulação.
    3. Qualquer célula morta com exatamente três vizinhos vivos se torna uma célula viva.
    4. Qualquer célula viva com dois ou três vizinhos vivos continua no mesmo estado para a próxima geração.
    '''
    lstAtualiza = []
    for i in range(1,tadMatriz.quantLinhas(tadGol)+1):
        for j in range(1,tadMatriz.quantColunas(tadGol)+1):
            quantVizinhos = vizinhosVivos(tadMatriz.vizinhos(tadGol,i,j))
            trocou = False
            # Se estiver viva
            if tadMatriz.getElem(tadGol,i,j) == 1:
                if quantVizinhos < 2:
                    '''Qualquer célula viva com menos de dois vizinhos vivos morre de solidão.'''
                    lstAtualiza.append((i,j,0))

                elif quantVizinhos > 3:
                    '''Qualquer célula viva com mais de três vizinhos vivos morre de superpopulação.'''
                    #Morre de super população
                    lstAtualiza.append((i,j,0))
                elif quantVizinhos == 2 or quantVizinhos == 3:
                    '''Qualquer célula viva com dois ou três vizinhos vivos continua no mesmo estado para a próxima geração.'''
                    lstAtualiza.append((i,j,tadMatriz.getElem(tadGol,i,j)))
            else:
                if quantVizinhos == 3:
                    '''Qualquer célula morta com exatamente três vizinhos vivos se torna uma célula viva.'''
                    lstAtualiza.append((i,j,1))
    for item in lstAtualiza:
        tadGol = tadMatriz.setElem(tadGol,item[0],item[1],item[2])



    return tadGol,lstAtualiza


def main():
    pass
if __name__ == '__main__':
    main()