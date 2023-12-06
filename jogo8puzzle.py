import time as tempo

# Classe que representa as configurações do 8-puzzle
class EstadoPuzzle:
    def __init__(self, estado, pai, movimento, profundidade):
        self.estado = estado
        self.pai = pai
        self.movimento = movimento
        self.profundidade = profundidade
        if self.estado:
            self.avaliacao = heuristica(estado)
        if self.estado:
            self.custo = custo(estado)
        if self.estado:
            self.mapa = ''.join(str(e) for e in self.estado)

# Função avaliação (utilizou-se a distancia manhattan)
def heuristica(estado):
    distancia = 0
    for i in range(3):
        for j in range(3):
            valor = estado[i * 3 + j]
            if valor != 0:
                linhaF = (valor - 1)//3
                colunaF = (valor - 1)%3
                distancia += abs(i - linhaF) + abs(j - colunaF)
    return distancia

# Função custo
def custo(estado_atual):
    global EstadoMeta
    custo = 0
    for i in range(len(estado_atual)):
        valor = estado_atual.index(i)
        linha_atual = valor//3
        coluna_atual = valor%3
        valor = EstadoMeta.index(i)
        linha_meta = valor//3
        coluna_meta = valor%3
        custo += abs(linha_atual - linha_meta) + abs(coluna_atual - coluna_meta)
    return custo

# Variáveis globais 
EstadoMeta = [1, 2, 3, 8, 0, 4, 7, 6, 5]
NoMeta = None  
NosTotais = 0  
MaxProfundidade = 0  
MaxLargura = 0 

# 1) Busca em profundidade primeiro
def dfs(estadoInicial):
    global MaxLargura, NoMeta, MaxProfundidade,NosTotais
    
    # Armazena nos visitados
    tabuleiroVisitado = set()

    # Utiliza-se lógica FILO para realizar a busca    
    pilha = [EstadoPuzzle(estadoInicial, None, None, 0)]

    while pilha != []:
        no = pilha.pop()
        tabuleiroVisitado.add(no.mapa)
        NosTotais +=1
        if no.estado == EstadoMeta:
            NoMeta = no
            return pilha
        caminhosPossiveis = subEstados(no)
        caminhosPossiveis = caminhosPossiveis[::-1]

        for caminho in caminhosPossiveis:
            if caminho.mapa not in tabuleiroVisitado:
                pilha.append(caminho)
                tabuleiroVisitado.add(caminho.mapa)
                if caminho.profundidade > MaxProfundidade:
                    MaxProfundidade = 1 + MaxProfundidade

        if len(pilha) > MaxLargura:
            MaxLargura = len(pilha)

# 2) Busca em largura primeiro
def bfs(estadoInicial):
    global MaxLargura, NoMeta, MaxProfundidade, NosTotais

    # Armazena nos visitados
    tabuleiroVisitado = set()
    
    # Utiliza-se lógica FIFO para realizar a busca
    fila = [EstadoPuzzle(estadoInicial, None, None, 0)]

    # Utiliza-se lógica FIFO para realizar a busca
    while fila != []:
        no = fila.pop(0)
        tabuleiroVisitado.add(no.mapa)
        NosTotais +=1
        if no.estado == EstadoMeta:
            NoMeta = no
            return fila
        caminhosPossiveis = subEstados(no)

        for caminho in caminhosPossiveis:
            if caminho.mapa not in tabuleiroVisitado:
                fila.append(caminho)
                tabuleiroVisitado.add(caminho.mapa)
                if caminho.profundidade > MaxProfundidade:
                    MaxProfundidade = MaxProfundidade + 1

        if len(fila) > MaxLargura:
            tamanhoFila = len(fila)
            MaxLargura = tamanhoFila
  
# 3) Busca Hill-climbing
def hill_climbing(estadoInicial):
    global MaxLargura, NoMeta, MaxProfundidade, NosTotais

    # Armazena nos visitados
    tabuleiroVisitado = set()
    
    # Utiliza-se lógica FILO para realizar a busca
    pilha = [EstadoPuzzle(estadoInicial, None, None, 0)]

    while pilha != []:
        no = pilha.pop()
        tabuleiroVisitado.add(no.mapa)
        NosTotais +=1
        if no.estado == EstadoMeta:
            NoMeta = no
            return pilha
        caminhosPossiveis = subEstados(no)
        # Ordena a pilha a partir da função avaliação
        caminhosPossiveis.sort(key=lambda x: x.avaliacao)

        for caminho in caminhosPossiveis:
            if caminho.mapa not in tabuleiroVisitado:
                pilha.append(caminho)
                tabuleiroVisitado.add(caminho.mapa)

                if caminho.profundidade > MaxProfundidade:
                    MaxProfundidade = 1 + MaxProfundidade

        if len(pilha) > MaxLargura:
            MaxLargura = len(pilha)
            
# 4) Busca Best first
def best_first(estadoInicial):
    global MaxLargura, NoMeta, MaxProfundidade, NosTotais

    # Armazena nos visitados
    tabuleiroVisitado = set()
    
    # Utiliza-se lógica FIFO para realizar a busca
    fila = [EstadoPuzzle(estadoInicial, None, None, 0)]

    while fila != []:
        no = fila.pop(0)
        tabuleiroVisitado.add(no.mapa)
        NosTotais +=1
        if no.estado == EstadoMeta:
            NoMeta = no
            return fila
        caminhosPossiveis = subEstados(no)
        # Ordena a fila a partir da função avaliação
        caminhosPossiveis.sort(key=lambda x: x.avaliacao)

        for caminho in caminhosPossiveis:
            if caminho.mapa not in tabuleiroVisitado:
                fila.append(caminho)
                tabuleiroVisitado.add(caminho.mapa)
                if caminho.profundidade > MaxProfundidade:
                    MaxProfundidade = MaxProfundidade + 1

        if len(fila) > MaxLargura:
            tamanhoFila = len(fila)
            MaxLargura = tamanhoFila
            
# 5) Busca Best-cost
def best_cost(estadoInicial):
    global MaxLargura, NoMeta, MaxProfundidade, NosTotais

    # Armazena nos visitados
    tabuleiroVisitado = set()
    
    # Utiliza-se lógica FIFO para realizar a busca
    fila = [EstadoPuzzle(estadoInicial, None, None, 0)]

    while fila != []:
        no = fila.pop(0)
        tabuleiroVisitado.add(no.mapa)
        NosTotais +=1
        if no.estado == EstadoMeta:
            NoMeta = no
            return fila
        caminhosPossiveis = subEstados(no)
        # Ordena a fila a partir da função custo
        caminhosPossiveis.sort(key=lambda x: x.custo)

        for caminho in caminhosPossiveis:
            if caminho.mapa not in tabuleiroVisitado:
                fila.append(caminho)
                tabuleiroVisitado.add(caminho.mapa)
                if caminho.profundidade > MaxProfundidade:
                    MaxProfundidade = MaxProfundidade + 1

        if len(fila) > MaxLargura:
            tamanhoFila = len(fila)
            MaxLargura = tamanhoFila

# 6) Busca Best-path
def best_path(estadoInicial):
    global MaxLargura, NoMeta, MaxProfundidade, NosTotais

    # Armazena nos visitados
    tabuleiroVisitado = set()
    
    # Utiliza-se lógica FIFO para realizar a busca
    fila = [EstadoPuzzle(estadoInicial, None, None, 0)]

    while fila != []:
        no = fila.pop(0)
        tabuleiroVisitado.add(no.mapa)
        NosTotais +=1
        if no.estado == EstadoMeta:
            NoMeta = no
            return fila
        caminhosPossiveis = subEstados(no)
        # Ordena a fila a partir da função avaliação e custo
        caminhosPossiveis.sort(key=lambda x: (x.custo+x.avaliacao))

        for caminho in caminhosPossiveis:
            if caminho.mapa not in tabuleiroVisitado:
                fila.append(caminho)
                tabuleiroVisitado.add(caminho.mapa)
                if caminho.profundidade > MaxProfundidade:
                    MaxProfundidade = MaxProfundidade + 1

        if len(fila) > MaxLargura:
            tamanhoFila = len(fila)
            MaxLargura = tamanhoFila

# Obter Sub Nós
def subEstados(no):
    proximosCaminhos = []
    proximosCaminhos.append(EstadoPuzzle(mover(no.estado, 1), no, 1, no.profundidade + 1))
    proximosCaminhos.append(EstadoPuzzle(mover(no.estado, 2), no, 2, no.profundidade + 1))
    proximosCaminhos.append(EstadoPuzzle(mover(no.estado, 3), no, 3, no.profundidade + 1))
    proximosCaminhos.append(EstadoPuzzle(mover(no.estado, 4), no, 4, no.profundidade + 1))

    nos = []
    for caminhosProcessados in proximosCaminhos:
        if caminhosProcessados.estado != None:
            nos.append(caminhosProcessados)
    return nos

# Função que movimenta o espaço em branco (0)
def mover(estadoAtual, direction):
    # obter posição do zero
    i = estadoAtual.index(0)
    
    # gera copia do tabuleiro
    estadoNovo = [x for x in estadoAtual]

    # para zero em (0,0)
    if(i==0):
        if(direction==1):
            return None
        if(direction==2):
            temp=estadoNovo[0]
            estadoNovo[0]=estadoNovo[3]
            estadoNovo[3]=temp
        if(direction==3):
            return None
        if(direction==4):
            temp=estadoNovo[0]
            estadoNovo[0]=estadoNovo[1]
            estadoNovo[1]=temp
        return estadoNovo    
    # para zero em (0,1)  
    if(i==1):
        if(direction==1):
            return None
        if(direction==2):
            temp=estadoNovo[1]
            estadoNovo[1]=estadoNovo[4]
            estadoNovo[4]=temp
        if(direction==3):
            temp=estadoNovo[1]
            estadoNovo[1]=estadoNovo[0]
            estadoNovo[0]=temp
        if(direction==4):
            temp=estadoNovo[1]
            estadoNovo[1]=estadoNovo[2]
            estadoNovo[2]=temp
        return estadoNovo
    # para zero em (0,2)
    if(i==2):
        if(direction==1):
            return None
        if(direction==2):
            temp=estadoNovo[2]
            estadoNovo[2]=estadoNovo[5]
            estadoNovo[5]=temp
        if(direction==3):
            temp=estadoNovo[2]
            estadoNovo[2]=estadoNovo[1]
            estadoNovo[1]=temp
        if(direction==4):
            return None
        return estadoNovo
    # para zero em (1,0)
    if(i==3):
        if(direction==1):
            temp=estadoNovo[3]
            estadoNovo[3]=estadoNovo[0]
            estadoNovo[0]=temp
        if(direction==2):
            temp=estadoNovo[3]
            estadoNovo[3]=estadoNovo[6]
            estadoNovo[6]=temp
        if(direction==3):
            return None
        if(direction==4):
            temp=estadoNovo[3]
            estadoNovo[3]=estadoNovo[4]
            estadoNovo[4]=temp
        return estadoNovo
    # para zero em (1,1)
    if(i==4):
        if(direction==1):
            temp=estadoNovo[4]
            estadoNovo[4]=estadoNovo[1]
            estadoNovo[1]=temp
        if(direction==2):
            temp=estadoNovo[4]
            estadoNovo[4]=estadoNovo[7]
            estadoNovo[7]=temp
        if(direction==3):
            temp=estadoNovo[4]
            estadoNovo[4]=estadoNovo[3]
            estadoNovo[3]=temp
        if(direction==4):
            temp=estadoNovo[4]
            estadoNovo[4]=estadoNovo[5]
            estadoNovo[5]=temp
        return estadoNovo
    # para zero em (1,2)
    if(i==5):
        if(direction==1):
            temp=estadoNovo[5]
            estadoNovo[5]=estadoNovo[2]
            estadoNovo[2]=temp
        if(direction==2):
            temp=estadoNovo[5]
            estadoNovo[5]=estadoNovo[8]
            estadoNovo[8]=temp
        if(direction==3):
            temp=estadoNovo[5]
            estadoNovo[5]=estadoNovo[4]
            estadoNovo[4]=temp
        if(direction==4):
            return None
        return estadoNovo
    # para zero em (2,0)
    if(i==6):
        if(direction==1):
            temp=estadoNovo[6]
            estadoNovo[6]=estadoNovo[3]
            estadoNovo[3]=temp
        if(direction==2):
            return None
        if(direction==3):
            return None
        if(direction==4):
            temp=estadoNovo[6]
            estadoNovo[6]=estadoNovo[7]
            estadoNovo[7]=temp
        return estadoNovo
    # para zero em (2,1)
    if(i==7):
        if(direction==1):
            temp=estadoNovo[7]
            estadoNovo[7]=estadoNovo[4]
            estadoNovo[4]=temp
        if(direction==2):
            return None
        if(direction==3):
            temp=estadoNovo[7]
            estadoNovo[7]=estadoNovo[6]
            estadoNovo[6]=temp
        if(direction==4):
            temp=estadoNovo[7]
            estadoNovo[7]=estadoNovo[8]
            estadoNovo[8]=temp
        return estadoNovo
    # para zero em (2,2)
    if(i==8):
        if(direction==1):
            temp=estadoNovo[8]
            estadoNovo[8]=estadoNovo[5]
            estadoNovo[5]=temp
        if(direction==2):
            return None
        if(direction==3):
            temp=estadoNovo[8]
            estadoNovo[8]=estadoNovo[7]
            estadoNovo[7]=temp
        if(direction==4):
            return None
        return estadoNovo      

# Função principal
def main():
    global NoMeta

    # Construir estado inicial do tabuleiro
    print("INFORME O ESTADO INICIAL DO 8 PUZZLE:")
    estadoInicial = [int(x) for x in input().split()]

    # Iniciar cronometragem
    inicio = tempo.time()
    
    # Escolhe método a ser usado
    metodo = input("INFORME O MÉTODO DE BUSCA:\n1) Profundidade (Depth-first)\n2) Largura Primeiro (Breadth-first)\n3) Hill-Climbing (Depth-first + função de avaliação)\n4) Best-first (Breadth-first + função de avaliação)\n5) Best-cost (Breadth-first + função de custo)\n6) Best-path (Breadth-first + função de avaliação + função de custo)\n")
    if metodo == "1":
        dfs(estadoInicial)
    elif metodo == "2":
        bfs(estadoInicial)
    elif metodo == "3":
        hill_climbing(estadoInicial)
    elif metodo == "4":
        best_first(estadoInicial)
    elif metodo == "5":
        best_cost(estadoInicial)
    elif metodo == "6":
        best_path(estadoInicial)

    # Finalizar cronometragem
    fim = tempo.time()
    tempoTotal = (fim - inicio)

    # Salvar resultado do caminho total
    profundidade = NoMeta.profundidade
    custo = NoMeta.custo
    movimentos = []
    
    # Traduz movimentos
    while estadoInicial != NoMeta.estado:
        if NoMeta.movimento == 1:
            caminho = 'Cima'
        if NoMeta.movimento == 2:
            caminho = 'Baixo'
        if NoMeta.movimento == 3:
            caminho = 'Esquerda'
        if NoMeta.movimento == 4:
            caminho = 'Direita'
        movimentos.insert(0, caminho)
        NoMeta = NoMeta.pai

    # Impimir objetivo
    print("Estado inicial:\t\tEstado final:")
    print(estadoInicial[:3], end="\t\t")
    print("[1, 2, 3]")
    print(estadoInicial[3:6], end="\t\t")
    print("[8, 0, 4]")
    print(estadoInicial[6:9], end="\t\t")
    print("[7, 6, 5]")

    # Imprimir percurso
    print("--CAMINHO--")
    print("Estado inicial ->", end=" ")
    tam = len(movimentos)
    for i in range(tam):
        print(movimentos[i], end= " ")
        if i != tam-1:
            print("->", end = " ")
    print("= Estado final")
    
    # Imprimir info pertinente
    print("--INFORMAÇÃO--")
    print("Altura máxima da árvore: ", MaxProfundidade)
    print("Largura máxima da árvore: ", MaxLargura)
    print("Profundidade do estado final: ", profundidade)
    
    print("--GASTO--")
    print("Nós totais do percurso: ", NosTotais)
    print(f'Tempo de execução: {tempoTotal}')

# Chamada da função main(), com exeção para excesso de memória  
if __name__ == '__main__':
    try:
        main()
    except:
        print("NÃO FOI POSSÍVEL REALIZAR A AÇÃO")
