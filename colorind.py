import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

#gerando cores e colocando no vetor "colors"

mapeamento_cores = {}
fourcolor = plt.cm.turbo(np.linspace(0.2, 1, 4, 6))
plt.cm.turbo

#Criando Grafo Aleatorio

G_1 = nx.fast_gnp_random_graph(8, 0.4)
nx.draw(G_1, with_labels = True )
plt.show()

#ARRUMAR(SALVAR GRAFO ACIMA EM UM ARQUIVO)
# Plotando grafo
nx.draw(G_1, with_labels=True)
plt.show()

# Salvando em arquivo
nx.write_gml(G_1, "graph.gml")

# Carregando grafo de arquivo
H = nx.read_gml("graph.gml")

# Plotando grafo depois de carregar de arquivo
nx.draw(H, with_labels=True)
plt.show()

#analisando o grau de cada verticie para usarmos posteriormente:

grauNo = G_1.degree
print (grauNo)

# transforma o grauNo em um dicionario, onde . values retorna os valores dos nos do dicionario, onde max retornara o maior valor
maior_grau= max(dict(grauNo).values())

#"dict" converte grauNo para dicionario, para facilitar a busca, "for v, grau in" incia as interações com o dicionario, na qual "if grau == maior_grau" verifica se o vertice buscado no dicionario tem o maior grau, assim os vertices cujo o grau é igual ao maior é salvo na lista
vertices_maior_grau=[v for v, grau in dict(grauNo).items()if grau==maior_grau]

def colorir_grafo(grafo):
    cores = {}  # Dicionário para armazenar as cores dos vértices
    for vertice in grafo.nodes:
        cores[vertice] = None  # Inicializa todas as cores como None

    cores_disponiveis = set(range(1, 5))

    for vertice in grafo.nodes:
        cores_adjacentes = set(cores[v] for v in grafo.neighbors(vertice))
        cor_disponivel = min(cores_disponiveis)
        while True:
            if cor_disponivel not in cores_adjacentes:
                cores[vertice] = cor_disponivel
                break
            cor_disponivel += 1

    return cores

cores = colorir_grafo(G_1)
pos = nx.spring_layout(G_1)  # Layout do grafo
nx.draw_networkx_nodes(G_1, pos, node_color=[cores[v] for v in G_1.nodes], cmap=plt.cm.rainbow)
nx.draw_networkx_edges(G_1, pos)
nx.draw_networkx_labels(G_1, pos)
plt.show(G_1)

vizinhos = list(nx.all_neighbors(G_1, 0))
vizinhos
