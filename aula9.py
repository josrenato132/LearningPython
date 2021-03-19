import shutil

def escreverNovoArquivo (texto):
    arquivo = open("C:/Users/Jose Renato/Desktop/teste.txt", "w" )
    arquivo.write(texto)
    arquivo.close()

def atualizarArquivo (nomeArquivo, texto):
    arquivo = open(nomeArquivo, "a")
    arquivo.write(texto)
    arquivo.close()

def lerArquivo(nomeArquivo):
    arquivo = open(nomeArquivo, "r")
    textoArquivo = arquivo.read()
    print(textoArquivo)

def mediaNotas(nomeArquivo):
    arquivo = open(nomeArquivo, "r")
    alunoNota = arquivo.read()
    #print(alunoNota)
    alunoNota = alunoNota.split("\n")
    #print(alunoNota)
    listaMedia = []
    for x in alunoNota:
        listaNotas = x.split(",")
        aluno = listaNotas[0]
        listaNotas.pop(0)
        #print(listaNotas)
        media = lambda notas: sum([int(i) for i in notas]) / 4
        #print(media(listaNotas))
        listaMedia.append({aluno:media(listaNotas)})
    return listaMedia

def copiaArquivo(nomeArquivo):
    shutil.copy(nomeArquivo, "C:/Users/Jose Renato/Desktop/notas2.txt")

def moveArquivo(nomeArquivo):
    shutil.move(nomeArquivo, "C:/Users/Jose Renato/Desktop/notas3.txt")

if __name__ == '__main__':
    diretorio = "C:/Users/Jose Renato/Desktop/notas.txt"
    #escreverNovoArquivo("Primeira linha. \n")
    #atualizarArquivo(diretorio,"Rafael 5, 6, 7, 7 \n Lucas 7, 6, 5, 5 \n Maria 4, 4, 5, 5")
    listaMedia = mediaNotas(diretorio)
    print(listaMedia)
    lerArquivo(diretorio)

