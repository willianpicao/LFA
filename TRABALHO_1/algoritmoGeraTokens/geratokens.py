def main():
    tabela = open('tabela.txt', 'r')
    input = []  
    dados = [] 
    input = tabela.readlines()

    for i in range(len(input)):          
        dados.append(input[i].split(";"))  #percorre matriz de dados(a tabela em txt) pegando dados separados por ";"
    tabela.close() 

    entrada = open('arq_de_entrada.txt', 'r')
    input2 = []
    input2 = entrada.readline()
    aux2 = []

    aux2 = input2.split(" ")
    entrada.close()
    print("============================================================================")
    print("||                            ENTRADA:                                    ||")
    print("||                                                                        ||")
    print("||",aux2)
    print("||                                                                        ||")
    print("||                                                                        ||")
    print("============================================================================")
    print("|| TOKENS GERADOS: ||\n")
    aux = 1  
    for x in aux2:
        for cont in range(len(x)):
            aux = ondeToPondeVou( x[cont], dados, aux )     
        print(dados[50][aux])   #na linha 50 da matriz(tabela)de dados que se encontram os tokens
        aux = 1

def ondeToPondeVou( ch, dados, aqui ):
    for i in range(len(dados)):
        if ( ch == dados[i][0] ):
            aqui = int(dados[i][aqui])
            aqui = aqui +1
    return (aqui)
            

main()