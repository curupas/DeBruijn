"""
Projeto: DeBruijnGraph_Seminarios I.py

Direitos Autorais (C) 2024 : José Ricardo S Tavares (jose.ricardo.tavares@ufsc.grad.br)

  Data: 2024-10-31
Versão: 20241031.01
"""

import networkx as nx
import matplotlib.pyplot as plt
import time 
import sys

sys.setrecursionlimit(15500)

import platform
import psutil
import platform

# Mede alguns parâmetros de desempenho do sistema
def get_system_info():
    # Informação do processador
    cpu_info = {
        "Processor": platform.processor(),
        "Physical cores": psutil.cpu_count(logical=False),
        "Total cores": psutil.cpu_count(logical=True),
        "Max Frequency": f"{psutil.cpu_freq().max:.2f}Mhz",
        "Min Frequency": f"{psutil.cpu_freq().min:.2f}Mhz",
        "Current Frequency": f"{psutil.cpu_freq().current:.2f}Mhz",
    }

    # Consumo do processo atual
    process = psutil.Process()
    process_info = {
        "Process Name": process.name(),
        "Process ID": process.pid,
        "CPU Usage": f"{process.cpu_percent(interval=1.0)}%",
        "Memory Usage": f"{process.memory_info().rss / (1024 ** 2):.2f}MB"
    }

    return {
        "CPU Info": cpu_info,
        "Process Info": process_info
    }


class Node:
    def __init__(self, km1mer):
        self.km1mer = km1mer
        self.nin = 0
        self.nout = 0

    def __eq__(self, other):
        return isinstance(other, Node) and self.km1mer == other.km1mer

    def __ne__(self, other):
        return not (self == other)

    def __hash__(self):
        return hash(self.km1mer)

    def __str__(self):
        return self.km1mer

class DeBruijnGraph:
    @staticmethod
    def chop(st, k):
        for i in range(len(st) - (k - 1)):
            yield (st[i:i+k], st[i:i+k-1], st[i+1:i+k])

    def __init__(self, strIter, k):
        self.G = {}
        self.nodes = {}
        self.kmers = []  # Lista para armazenar os k-mers
        self.k = k  # Armazena o valor de k como um atributo da instancia
        for st in strIter:
            for kmer, km1L, km1R in self.chop(st, k):
                self.kmers.append(kmer)  # Adiciona o k-mer a lista
                if km1L not in self.nodes:
                    self.nodes[km1L] = Node(km1L)
                if km1R not in self.nodes:
                    self.nodes[km1R] = Node(km1R)
                self.nodes[km1L].nout += 1
                self.nodes[km1R].nin += 1
                self.G.setdefault(self.nodes[km1L], []).append(self.nodes[km1R])

    def print_kmers(self):
        """Imprime os k-mers utilizados para construir o grafo."""
        print("k-mers: ({0})".format(len(self.kmers)), end=" ")
        for kmer in self.kmers:
            print(kmer, end=" ")

    def get_kmers_str(self):
        """Retorna os k-mers utilizados para construir o grafo como uma string."""
        return ' '.join(self.kmers)

    def visualize(self):
        G = nx.DiGraph(directed=True)
        
        # Adiciona os nós ao grafo
        for node in self.nodes.values():
            G.add_node(str(node))

        # Adiciona as arestas ao grafo
        for src, dsts in self.G.items():
            for dst in dsts:
                G.add_edge(str(src), str(dst))

        pos = nx.circular_layout(G)

        fig = plt.figure(figsize=(12, 8))
        ax = plt.gca()
        fig.patch.set_facecolor('xkcd:mint green')
        ax.patch.set_facecolor('black')
        
        kmers_text = (self.get_kmers_str()).replace(' ', '\n')

        plt.text(1.0, 0.5, f"K-mers:\n\n{kmers_text}", transform=ax.transAxes, ha="left", va="center", fontsize=12,
                 bbox=dict(boxstyle="round,pad=0.5", facecolor="lightgrey", edgecolor="black", linewidth=1))

        plt.title("Grafo de De Bruijn")
        nx.draw(G, pos, with_labels=True, node_size=1800, node_color="lightblue", font_size=10, font_weight="bold", edge_color='black', arrows=True)
        plt.show()

    def eulerianWalkOrCycle(self):
        g = {node: adj[:] for node, adj in self.G.items()}  
        start_node = next((node for node in self.nodes.values() if node.nout > node.nin), None)
        if not start_node:
            start_node = next(iter(g))  # Comece de um vértice arbitrário

        path = []

        def visit(node):
            while g.get(node):
                next_node = g[node].pop(0)
                visit(next_node)
            path.append(node)

        visit(start_node)

        path = path[::-1]  

        # A reconstrução da sequência começa com o k-mer completo do primeiro nó
        sequence = str(path[0])
        # Então, para cada nó subsequente adiciona apenas o último caractere do k-mer
        for node in path[1:]:
            sequence += str(node)[-1]

        return sequence

def main():

    # Escolha uma das sequencias abaixo:

    #String="ATGGAAGTCGCGGAATC"
    #String="0000110010111101"
    #String="3.14159265358979323846"
    String="ATGGCTAGTTGGATCTGACGTGTGCA"

    # Escolha um comprimento para o kmer:
    kmer_Length=7

    start=time.time()
    G = DeBruijnGraph([String],kmer_Length)
    end=time.time()
    G.print_kmers()
    print("\nString Original ({0}): {1} {2} \n\nTempo de Execução: {3} millisegundos".format(len(String), len(G.eulerianWalkOrCycle()), G.eulerianWalkOrCycle(),(end-start)))
    print("\n\nComprimento da String Original ({0}) \n\nTempo de Execução: {1} millisegundos.\n\n".format(len(String),(end-start)*1000))
    G.visualize()

    system_info = get_system_info()
    for key, value in system_info.items():
        print(f"{key}:")
        for sub_key, sub_value in value.items():
            print(f"  {sub_key}: {sub_value}")

if __name__ == "__main__":
    main()

