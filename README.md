# DeBruijn
De Bruijn para as massas!

Em Combinatória, uma Sequência de De Bruijn de ordem n em um alfabeto A de tamanho k é uma sequência cíclica em que cada string 
de comprimento n possível em A ocorre exatamente uma vez como uma substring (ou seja, como uma subsequência contígua). 
Esta sequência é geralmente denotada por B(k, n).

![image](https://github.com/user-attachments/assets/50b7aec9-9c75-4c57-978b-e4ec428e9c81)

Um grafo de Bruijn é uma estrutura matemática que representa sobreposições entre substrings (k-mers) de uma sequência. É construído 
de tal forma que captura todas as possíveis sobreposições de comprimento k−1 entre k-mers de uma sequência.

# Passos para Criar um Grafo de De Bruijn

1. Divisão em k-mers:
Divida a sequência de DNA em subsequências de comprimento k, chamadas k-mers. Por exemplo, para a sequência "ATGGAAGTCGCGGAATC" e k=7:

k-mers:	ATGGAAG, TGGAAGT, GGAAGTC, GAAGTCG, AAGTCGC, AGTCGCG,
			GTCGCGG, TCGCGGA, CGCGGAA, GCGGAAT, CGGAATC  

2. Construção dos Vértices:
Cada k-mer gera dois vértices a partir dos k-1 primeiros e últimos caracteres. Por exemplo:

ATGGAAG gera os vértices ATGGAA e TGGAAG
TGGAAGT gera os vértices TGGAAG e GGAAGT

3. Criação das Arestas
As arestas do grafo são formadas pelos k-mers, conectando os vértices gerados.

4. Construção do Grafo
Conecte todos os vértices usando as arestas formadas.

5. Caminho Euleriano (Algoritmo de Hierholzer)
Encontre um caminho Euleriano, que percorre todas as arestas do grafo exatamente uma vez.

6. Reconstrução da Sequência
Concatene os k-mers do caminho Euleriano para reconstruir a sequência original

![image](https://github.com/user-attachments/assets/a713304e-e2c1-45a7-8fff-80b182402f20)


