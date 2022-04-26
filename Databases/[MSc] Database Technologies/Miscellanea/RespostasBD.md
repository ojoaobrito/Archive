# Pergunta 1

- Armazenamento, devolução e atualização de dados;
- Catálogo acessível ao utilizador;
- Suporte a transações;
- Controlo de concorrência;
- Recuperação a falhas;
- Autorização;
- Comunicação de dados;
- Integridade.

# Pergunta 2

- A arquitetura 3 camadas é uma arquitetura derivada da arquitetura cliente-servidor, no entanto, enquanto que a arquitetura cliente-servidor tem a camada de negócio do lado do cliente, camada essa responsável pelo armazenamento das funções e regras de todo o negócio, a arquitetura de 3 camadas não tem essa mesma camada.

# Pergunta 3

- A operação de leitura faz a transferência de dados do disco para a RAM e a operação de escrita faz a transferência de dados da RAM para o disco. Ambas estas funções são relevantes para o desempenho da base de dados por serem operações de custo elevado em termos de tempo e espaço em memória, daí ser preciso planear essas operações cuidadosamente.

# Pergunta 4

- No caso de existir um ficheiro com dados ordenados, faz-se uma pesquisa binária para encontrar o primeiro valor que obedece à condição, percorrendo o ficheiro sequencialmente a partir desse ponto. Após isso, cria-se um ficheiro de indexação, estruturado em registos na forma <primeiro valor na pagina, apontador>. Após isso, a pesquisa binária vai ser feita no ficheiro de indexação. Procura o apontador e vai ao ficheiro principal, vê o registo para onde esse apontador aponta e começa a ler os registos sequencialmente, desde que eles satisfaçam as condições.

- Índices estruturados em árvore são ideais quando se pretende fazer uma pesquisa por gamas, no entanto, são também adequados para fazer pesquisas por igualdade.

# Pergunta 5

- Primeiro foi inserido o valor 'Ana Paula' na tabela através do comando INSERT;

- Depois é criado um "backup" da base de dados com o estado atual da mesma, com o nome "point1";

- De seguida é introduzido o valor 'Francisco Reis' usando o SELECT, seguido da criação de outro "backup" com o nome "point2";

- Seguidamente, é introduzido o valor 'Carlos Costa' usando o SELECT;

- Depois, recupera-se o "backup" de nome "point1", levando a que o base de dados volte ao estado presente na criação desse backup;

- Por último, é introduzido o valor 'Bruno Dias' usando o SELECT;

- Estado da tabela no final da execução:


|      Pessoa     |
|-----------------|
|    Ana Paula    |
|    Bruno Dias   |



# Pergunta 6

- A utilização de WAL em transações é benéfico porque reduz significativamente a quantidade de operações de escrita no disco, visto que quando se faz a transação só precisa de ser descarregado o arquivo de registo para o disco. Também é benéfico porque mantém a consistência das páginas de dados, guardando todos os dados no registo caso haja uma queda, levando a uma recuperação mais eficaz. Também faz uma cópia de segurança em linha e recuperação para um ponto no tempo.

# Pergunta 7

O nivel de isolamento "Read committed" é o nivel padrão, onde cada query só pode ver os dados submetidos antes da execução do query, levando a que dois resultados possam ser vistos caso haja uma dupla execução da query. O nivel de isolamento "Serializable" permite com que cada query veja os dados submetidos antes da execução da transação e todas as alterações feitas na transação, levando a que só haja um resultado.

# Pergunta 8

- A primeira pesquisa foi feita usando uma pesquisa sequencial, o que leva a que o filtro seja aplicado a todas as linhas que são alvo dessa pesquisa sequencial. Isso leva a que o número de linhas a ser analisadas seja elevado, aumentando o tempo de pesquisa para se obter todos os registos que satisfação o filtro implementado.

- A segunda pesquisa é feita através do scan dos índices. O filtro é aplicado na lista de índices e apenas os índices que satisfação o filtro são procurados, reduzindo drasticamente o número de linhas a ser analisadas. Depois, a essas linhas é aplicada a condição, de maneira a que apenas sejam devolvidos os registos q satisfação essa condição. Devido ao menor número de linhas analisadas, o tempo de execução do query vai ser muito menor que na primeira pesquisa, havendo uma diferença de quase 6000 ms.