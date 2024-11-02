# DeBruijn
De Bruijn para as massas!

Em Combinatória, uma Sequência de De Bruijn de ordem n em um alfabeto A de tamanho k é uma sequência cíclica em que cada string 
de comprimento n possível em A ocorre exatamente uma vez como uma substring (ou seja, como uma subsequência contígua). 
Esta sequência é geralmente denotada por B(k, n).

![image](https://github.com/user-attachments/assets/50b7aec9-9c75-4c57-978b-e4ec428e9c81)

Um grafo de Bruijn é uma estrutura matemática que representa sobreposições entre substrings (k-mers) de uma sequência. É construído 
de tal forma que captura todas as possíveis sobreposições de comprimento k−1 entre k-mers de uma sequência.

# Uso de Grafos de De Bruijn para Sequenciamento de DNA

## Passos para Criar um Grafo de De Bruijn

1. Divisão em k-mers: 
Divida a sequência de DNA em subsequências de comprimento k, chamadas k-mers. Por exemplo, para a sequência "ATGGAAGTCGCGGAATC" e k=7:

k-mers:	ATGGAAG, TGGAAGT, GGAAGTC, GAAGTCG, AAGTCGC, AGTCGCG,
			GTCGCGG, TCGCGGA, CGCGGAA, GCGGAAT, CGGAATC  

2. Construção dos Vértices: 
Cada k-mer gera dois vértices a partir dos k-1 primeiros e últimos caracteres. Por exemplo:

ATGGAAG gera os vértices ATGGAA e TGGAAG
TGGAAGT gera os vértices TGGAAG e GGAAGT

3. Criação das Arestas: 
As arestas do grafo são formadas pelos k-mers, conectando os vértices gerados.

4. Construção do Grafo: 
Conecte todos os vértices usando as arestas formadas.

5. Caminho Euleriano (Algoritmo de Hierholzer): 
Encontre um caminho Euleriano, que percorre todas as arestas do grafo exatamente uma vez.

6. Reconstrução da Sequência: 
Concatene os k-mers do caminho Euleriano para reconstruir a sequência original

![image](https://github.com/user-attachments/assets/a713304e-e2c1-45a7-8fff-80b182402f20)

## Algoritmo de Hierholzer

O algoritmo de Carl Hierholzer encontra um ciclo euleriano num grafo se todos os vértices têm o mesmo número de arestas 
entrando e saindo, que é o que esperamos que aconteça com nosso trecho de DNA. 
Complexidade O(E), onde E é o número de arestas.

1. Escolha um vértice inicial em um grafo com todas as arestas ainda não percorridas.

2. Siga um ciclo: Continue caminhando através de arestas não percorridas até retornar ao ponto de partida, formando um ciclo.

3. Procure arestas não visitadas: Se houver arestas não percorridas, escolha um vértice dentro do ciclo que já foi formado e inicie um novo ciclo a partir dele, percorrendo as arestas restantes.

4. Combine os ciclos: Cada novo ciclo é integrado ao ciclo anterior até que todas as arestas do grafo sejam percorridas.


# Referências

[1] Jacob Bower. 18.312: 2011. DOI: Algebraic Combinatorics- Lecture 21. http://pi.math.cornell.edu/~levine/18.312/ alg-comb-lecture-21.pdf. 

[2] Zerbino DR, Birney E. Velvet: algorithms for de novo short read assem bly using De Bruijn graphs. Genome Res. 2008 May;18(5):821-9. DOI: 10.1101/gr.074492.107. Epub 2008 Mar 18. PMID: 18349386; PMCID: PMC2336801. 

[3] Teoria dos Grafos. http://www.decom.ufop.br/marco/site_media/ uploads/bcc204/19_aula_19.pdf 

[4] Compeau PE, Pevzner PA, Tesler G. How to apply De Bruijn graphs to genome assembly. Nat Biotechnol. 2011 Nov 8;29(11):987-91. DOI: 10.1038/nbt.2023. PMID: 22068540; PMCID: PMC5531759. 

[5] Do DNA à Proteina. https://www.youtube.com/watch?v=gG7uCskUOrA 

[6] Síntese Proteica- Transcrição e Tradução do DNA. https://www. youtube.com/watch?v=JbzM3wtWOUU 

[7] DNA Animation by Drew Berry and Etsuko Uno. https://www. youtube.com/watch?v=7Hk9jct2ozY 

[8] A Survey on De Bruijn Sequences. https://kishen19.github.io/ assets/files/projects/A%20survey%20on%20De_Bruijn_Sequences. pdf 

[9] An Eulerian Path Approach to DNA fragment assembly. Pavel A. Pevz ner, Haixu Tang, and Michael S. Waterman. https://www.pnas.org/ doi/epdf/10.1073/pnas.171285098






