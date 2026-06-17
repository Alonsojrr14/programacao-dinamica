# Guia de Apresentação: Grupo 8

**Tempo total previsto:** 15 a 25 minutos
**Formato sugerido:** 5 integrantes, transição fluida, 1-2 slides de código ao vivo

> **Ferramentas de demonstração já prontas:**
> - `./apresentar.sh` roda os 4 algoritmos + os testes, com a explicação de cada
>   um na tela. Navegue pelas **setas** (`->` avança, `<-` volta, `q` sai); cada
>   tela substitui a anterior. Pode ser usado como demo guiada do início ao fim,
>   ou cada integrante roda só o seu trecho.
> - Os prints de cada tela estão em `assets/saida_*.png` (plano B caso o
>   terminal/projetor falhe). Detalhes em [`guia-slides.md`](guia-slides.md).

---

## Distribuição por integrante

### Integrante 1: Introdução + Fibonacci  *(≈ 4-5 min)*
- Abrir com o problema motivador: por que recursão ingênua "trava"?
- Definir PD: **subestrutura ótima** + **sobreposição de subproblemas**.
- Diferença Memoization (top-down) × Tabulation (bottom-up).
- Mostrar a árvore de recursão do Fibonacci (diagrama 2) e o ganho Θ(φⁿ)→Θ(n).
- **Demo:** rodar `src/fibonacci.py` (exército de demônios de Muzan).
- *Gancho para o próximo:* "Fibonacci tem 1 dimensão de estado; e se houver duas?"

> **Sugestão de fala:**
> "Boa tarde, professor e colegas. Nosso tema é Programação Dinâmica: uma
> técnica que resolve um problema grande quebrando-o em pedaços menores que se
> repetem e, em vez de recalcular esses pedaços toda hora, a gente guarda o
> resultado e reaproveita. Para ela funcionar, o problema precisa de duas
> coisas: subestrutura ótima, ou seja, a melhor solução do todo é feita das
> melhores soluções das partes; e sobreposição de subproblemas, que é quando os
> mesmos pedaços reaparecem várias vezes. O exemplo mais simples é Fibonacci.
> A gente imaginou o exército de demônios do Muzan: todo demônio já fortalecido
> transforma um humano por noite, e o recém-transformado leva uma noite para
> ganhar força — o total por noite segue exatamente Fibonacci. Olhem a árvore de
> recursão: F(3) é recalculado várias vezes, é trabalho jogado fora. Com
> memoization, calculamos cada termo uma única vez; com tabulation, montamos de
> baixo para cima e nem guardamos a tabela inteira. Fibonacci tem só uma
> dimensão de estado... e quando o problema tem duas? É o que a Mochila mostra."

### Integrante 2: Mochila 0/1  *(≈ 4 min)*
- Enunciar o problema e por que **guloso falha** (densidade não garante ótimo).
- Estado `(i, c)` e recorrência incluir vs. pular.
- Percorrer a tabela DP do exemplo da mochila do treinador Pokémon (diagrama 3).
- Destacar complexidade **pseudo-polinomial** O(n·W).
- **Demo:** `src/mochila.py` comparando força bruta × DP (mesmo resultado, custo distinto).

> **Sugestão de fala:**
> "Imaginem que vocês são um treinador de Pokémon e têm uma mochila com espaço
> limitado antes de encarar a Liga. Cada item ocupa um tamanho e tem uma
> utilidade em batalha. A pergunta é: qual combinação rende mais utilidade sem
> estourar o espaço? O '0/1' quer dizer que cada item entra inteiro ou não
> entra. E aqui tem uma pegadinha: ser guloso não funciona — se eu pego sempre o
> item mais valioso, o Restaurador Total, ele ocupa muito espaço sozinho e me
> faz perder a melhor combinação. A DP monta uma tabela: para cada item e cada
> espaço possível, ela decide o que vale mais, deixar o item de fora ou incluir.
> No fim, força bruta e DP chegam ao mesmo ótimo, utilidade 33; a diferença é
> que a força bruta testa 2 elevado a n combinações e a DP é muito mais barata.
> Até aqui os 'pedaços' eram itens. E se forem lugares num mapa?"

### Integrante 3: Caminho Mínimo  *(≈ 4 min)*
- Contextualizar DAG e por que aciclicidade importa.
- Recorrência `d[v] = min d[u] + w(u,v)` e ordem topológica.
- Caminhar pela tabela da Fortaleza Infinita de Muzan (diagrama 4).
- Comparar com Dijkstra: por que DP em DAG é Θ(V+E) e aceita pesos negativos.
- **Demo:** `src/caminho_minimo.py`.

> **Sugestão de fala:**
> "A gente ambientou na Fortaleza Infinita do Muzan: as salas se ligam por
> passagens de mão única que nunca voltam, ou seja, um grafo sem ciclos, o que
> chamamos de DAG. Queremos o caminho mais rápido do Portão até o Trono. A
> sacada da DP é a ordem topológica: organizamos as salas de modo que, ao chegar
> em uma sala, já sabemos o menor custo de tudo que leva até ela; aí é só somar.
> E reparem numa coisa interessante: o caminho mais curto não é o mais direto.
> Ir direto do Salão dos Tatames para o Trono custaria 14 minutos; desviar pela
> Câmara Central fecha em 9. A DP descobre isso sozinha, sem testar todos os
> caminhos. Comparando com o Dijkstra: como o grafo é acíclico, a nossa
> abordagem é até mais rápida, da ordem de V mais E, e ainda aceita pesos
> negativos."

### Integrante 4: Subsequência Comum Máxima (LCS)  *(≈ 4 min)*
- Definir subsequência (não contígua!) vs. substring.
- Recorrência igual/diferente; matriz e reconstrução por backtracking.
- Exemplo dos times Pokémon (diagrama 5).
- Conectar com aplicação real: `git diff` e bioinformática.
- **Demo:** `src/lcs.py`.

> **Sugestão de fala:**
> "Agora, dois treinadores montaram seus times de Pokémon, cada um numa ordem.
> Queremos a maior sequência de Pokémon que os dois escalaram na mesma ordem —
> mas não precisa ser seguida, pode ter buracos. Isso é a Subsequência Comum
> Máxima. Cuidado para não confundir com substring: substring é colada,
> subsequência pode pular elementos, desde que mantenha a ordem. A DP preenche
> uma matriz comparando os dois times: quando os Pokémon batem, ela aproveita a
> diagonal e soma 1; quando não batem, herda o maior vizinho. Depois ela
> 'caminha de volta' pela matriz para descobrir quais Pokémon formam a resposta.
> No nosso exemplo, mesmo com Pokémon trocados, sobram 4 na mesma ordem. E isso
> não é brincadeira: é exatamente o que o git diff faz para comparar versões de
> um arquivo, e o que a bioinformática usa para comparar DNA."

### Integrante 5: Comparação Geral + Testes + Conclusão  *(≈ 4-5 min)*
- Tabela comparativa dos 4 problemas (estado, recorrência, tempo, espaço).
- Mensagem central: **PD troca tempo por memória**.
- Receita de 4 passos para reconhecer e modelar um problema de PD.
- **Demo dos testes:** rodar `python3 -m pytest tests/ -v` e explicar a
  estratégia de **teste-gabarito** (DP comparada contra a força bruta/recursão).
  Resumir o que cada grupo valida:
  - Fibonacci: as 3 abordagens concordam; F(50) sem estouro; entrada inválida.
  - Mochila: DP == força bruta para toda capacidade de 0 a 20; casos-limite.
  - Caminho mínimo: custo/rota corretos; sem caminho → infinito; ciclo → erro.
  - LCS: recursivo == DP; subsequência realmente comum; casos-limite.
  - Fechar no **`26 passed`** como prova objetiva de qualidade.
- Aplicações reais (GPS, Git, bioinformática, logística, estoque, ML).
- Encerramento + abertura para perguntas.

> **Sugestão de fala:**
> "Juntando os quatro: o que muda de um para o outro é o estado e a recorrência,
> mas a ideia é sempre a mesma — guardar respostas de subproblemas para não
> repetir trabalho. A frase para levar para casa é: Programação Dinâmica troca
> tempo por memória. E como sabemos que está tudo certo, não só no papel? A gente
> testou: a estratégia foi comparar a versão por DP contra a força bruta, que
> testa todas as possibilidades — se as duas batem em dezenas de casos, a DP está
> correta. São 26 testes, e todos passam. Para fechar: sempre que um problema
> puder ser quebrado em subproblemas que se repetem, e a solução ótima vier das
> partes ótimas, pensem em DP. Ela aparece no GPS, no Git, na bioinformática, na
> logística, no controle de estoque e até em machine learning. Obrigado, e
> estamos abertos a perguntas."

---

## Checklist de ensaio

- [ ] Cada integrante cronometrou sua parte (margem de ±30 s).
- [ ] `./apresentar.sh` roda sem erro de ponta a ponta em Python 3.12+.
- [ ] Diagramas Mermaid renderizam no projetor/GitHub.
- [ ] Transições combinadas (cada um "passa a bola" ao próximo).
- [ ] Slide de backup com a tabela comparativa para perguntas.
- [ ] Prints de `assets/saida_*.png` exportados como plano B da demo.
- [ ] Revisar as 20 perguntas de `docs/perguntas.md`.

## Dicas de defesa
- Se perguntarem "por que não guloso?" → use o contraexemplo da mochila.
- Se perguntarem sobre memória → cite as otimizações O(1)/O(W)/O(min(m,n)).
- Sempre relacione a teoria ao exemplo autoral correspondente.
