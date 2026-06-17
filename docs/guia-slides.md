# Guia para Montagem dos Slides

> Para quem vai construir a apresentação visual (Google Slides, PowerPoint, Canva
> ou similar). Este documento diz **o que entra em cada slide**, em que ordem e
> quem fala. O roteiro de fala detalhado está em [`apresentacao.md`](apresentacao.md).

**Meta de tempo:** 15 a 25 minutos · **Integrantes:** 5 · **Slides sugeridos:** 16 a 18

---

## Princípios visuais (valem para todos os slides)

- **Pouco texto por slide.** Tópicos curtos, não parágrafos. O detalhe é falado.
- **Um conceito por slide.** Se precisar de "e também...", crie outro slide.
- **Sempre o exemplo autoral junto da teoria** (demônios de Muzan, mochila do
  treinador Pokémon, Fortaleza Infinita, times Pokémon). É o que prova que o
  material é nosso. Use as artes/temas de Pokémon e Demon Slayer para deixar os
  slides mais lúdicos.
- **Diagramas no lugar de texto.** Reaproveite os diagramas Mermaid de
  [`diagramas.md`](diagramas.md) (exporte como imagem: print da renderização no
  GitHub ou cole o código em https://mermaid.live e baixe o PNG).
- **Código só em trechos curtos** (a recorrência ou o `for` principal), com fonte
  monoespaçada. O código completo fica para a demo ao vivo no final.
- Paleta sóbria, identidade da UFC, número do slide no rodapé.

---

## Roteiro slide a slide

> As linhas marcadas com 💬 *Fala:* são sugestões de texto para o apresentador
> falar — pode ler como está ou adaptar para o seu jeito. Falas mais completas
> (parágrafo inteiro por integrante) estão em [`apresentacao.md`](apresentacao.md).

### Bloco de abertura

**Slide 1 — Capa** *(Integrante 1)*
- Título: "Problemas Clássicos de Programação Dinâmica"
- Universidade Federal do Ceará · Projeto e Análise de Algoritmos · **Grupo 8**
- Nomes dos 5 integrantes
- Subtítulo: Fibonacci · Mochila 0/1 · Caminho Mínimo · Subsequência Comum Máxima (LCS)
- 💬 *Fala:* "Boa tarde, professor e colegas. Somos o Grupo 8 e vamos falar sobre os problemas clássicos de Programação Dinâmica."

**Slide 2 — Agenda**
- Lista dos 4 problemas + comparação final + demonstração de código
- Serve de "mapa" para a banca
- 💬 *Fala:* "A ideia é apresentar quatro problemas, comparar os quatro no fim e, por último, mostrar o código rodando de verdade."

**Slide 3 — O que é Programação Dinâmica** *(Integrante 1)*
- Definição em uma frase
- Os dois pilares: **sobreposição de subproblemas** + **subestrutura ótima**
- Diagrama 1 de [`diagramas.md`](diagramas.md) (fluxo "quando usar DP")
- Memoization (top-down) × Tabulation (bottom-up) em 2 colunas
- 💬 *Fala:* "DP é resolver um problema grande quebrando em pedaços que se repetem e guardando o resultado para não recalcular. Ela serve quando o problema tem subestrutura ótima e sobreposição de subproblemas. Dá para implementar de cima para baixo, com memoization, ou de baixo para cima, com tabulation."

### Bloco Fibonacci

**Slide 4 — Fibonacci: teoria** *(Integrante 1)*
- Recorrência `F(n) = F(n-1) + F(n-2)`
- **Exemplo autoral:** exército de demônios de Muzan / Demon Slayer (1 ilustração + a regra)
- Árvore de recursão (diagrama 2) destacando os nós repetidos
- 💬 *Fala:* "Pensem no exército do Muzan: cada demônio fortalecido transforma um humano por noite, e o novo leva uma noite para ganhar força. O total por noite segue Fibonacci. Olhem na árvore como F(3) é recalculado várias vezes — esse retrabalho é o que vamos eliminar."

**Slide 5 — Fibonacci: as 3 abordagens + complexidade** *(Integrante 1)*
- Tabela: Recursivo Θ(φⁿ) · Memoization Θ(n) · Tabulation Θ(n)/espaço Θ(1)
- Trecho curto de código (só o `for` do tabulation)
- 💬 *Fala:* "A recursão pura é exponencial. Com memoization guardamos cada termo e caímos para linear. Com tabulation, como só os dois últimos termos importam, dá para usar espaço constante. As três dão o mesmo resultado; muda o custo."

### Bloco Mochila 0/1

**Slide 6 — Mochila 0/1: o problema** *(Integrante 2)*
- Definição + formulação (maximizar valor sob restrição de capacidade)
- **Exemplo autoral:** mochila do treinador Pokémon antes da Liga (tabela dos 5 itens)
- 💬 *Fala:* "Um treinador tem uma mochila com espaço limitado antes da Liga. Cada item ocupa um tamanho e tem uma utilidade. Queremos a combinação de maior utilidade que ainda cabe — e cada item entra inteiro ou não entra, por isso '0/1'."

**Slide 7 — Mochila 0/1: a solução DP** *(Integrante 2)*
- Recorrência incluir × pular (diagrama 3)
- Resultado do exemplo: Super Poção + Repelente + Ultra Ball = utilidade 33
- Frase-chave: "por que o guloso falha aqui"
- Complexidade O(n·W) (pseudo-polinomial)
- 💬 *Fala:* "Para cada item e cada espaço, a DP decide o que vale mais: deixar de fora ou incluir. Ser guloso não resolve — pegar o item mais valioso, o Restaurador Total, prende a mochila e perde a melhor combinação. A força bruta e a DP chegam ao mesmo 33, mas a DP é muito mais barata."

### Bloco Caminho Mínimo

**Slide 8 — Caminho Mínimo em DAG: o problema** *(Integrante 3)*
- O que é um DAG e por que a aciclicidade permite ordem topológica
- **Exemplo autoral:** Fortaleza Infinita de Muzan / Demon Slayer (diagrama 4 do grafo)
- 💬 *Fala:* "A Fortaleza Infinita do Muzan tem salas ligadas por passagens de mão única que nunca voltam — isso é um grafo sem ciclos, um DAG. Queremos o caminho mais rápido do Portão até o Trono."

**Slide 9 — Caminho Mínimo: a solução DP** *(Integrante 3)*
- Recorrência `d[v] = min(d[u] + w(u,v))`
- Tabela de custos preenchida (rota ótima = 9 min, em destaque)
- Comparação rápida com Dijkstra (Θ(V+E), aceita pesos negativos)
- 💬 *Fala:* "Pela ordem topológica, ao chegar numa sala já sabemos o menor custo de tudo que leva até ela. Reparem: o caminho direto custaria 14 minutos, mas desviar pela Câmara Central fecha em 9. Como o grafo é acíclico, isso é até mais rápido que Dijkstra e aceita pesos negativos."

### Bloco Subsequência Comum Máxima (LCS)

**Slide 10 — LCS: o problema** *(Integrante 4)*
- Subsequência × substring (a diferença do "não contíguo")
- **Exemplo autoral:** times Pokémon de dois treinadores (as duas listas lado a lado)
- 💬 *Fala:* "Dois treinadores montaram times numa certa ordem. Queremos a maior sequência de Pokémon que os dois escalaram na mesma ordem, podendo pular alguns. Atenção: subsequência não é substring — substring é colada, subsequência pode ter buracos."

**Slide 11 — LCS: a solução DP** *(Integrante 4)*
- Recorrência (igual → diagonal+1; diferente → max) com diagrama 5
- Matriz preenchida com o caminho da reconstrução destacado
- Resultado: [Charmander, Squirtle, Pikachu, Gengar], comprimento 4
- Complexidade O(m·n)
- 💬 *Fala:* "A matriz compara os dois times: quando os Pokémon batem, soma 1 na diagonal; quando não batem, herda o maior vizinho. Depois caminhamos de volta para descobrir quais Pokémon formam a resposta. Sobram 4 na mesma ordem — é o mesmo princípio do git diff."

### Bloco de fechamento

**Slide 12 — Comparação Geral** *(Integrante 5)*
- A tabela comparativa do README (problema · estado · recorrência · tempo · espaço)
- Mensagem central: **DP troca tempo por memória**
- 💬 *Fala:* "Juntando os quatro, o que muda é o estado e a recorrência, mas a ideia é a mesma: guardar respostas de subproblemas para não repetir trabalho. Em uma frase: Programação Dinâmica troca tempo por memória."

**Slide 13 — Aplicações Reais** *(Integrante 5)*
- Ícones: GPS, Git (diff), bioinformática, logística, estoque, machine learning
- 💬 *Fala:* "Isso não fica só no papel: DP está no GPS, no git diff, na comparação de DNA, na logística, no controle de estoque e até em machine learning."

**Slide 14 — Conclusão** *(Integrante 5)*
- A receita de 4 passos para reconhecer um problema de DP
- Uma frase de encerramento
- 💬 *Fala:* "Resumindo a receita: defina o estado, escreva a recorrência, decida a ordem de cálculo e, se precisar, reconstrua a solução. Sempre que houver subproblemas que se repetem, pense em DP."

---

## Bloco final: DEMONSTRAÇÃO DE CÓDIGO AO VIVO *(Integrante 5 conduz; todos apoiam)*

> Este é o diferencial pedido: ao fim da apresentação, mostramos que o código
> **roda de verdade** e que cada demo usa o **cenário autoral** da respectiva
> seção. Não é código genérico de livro: a entrada de cada programa é o nosso
> exemplo.

**Slide 15 — "Vamos ver rodando"** (slide de transição)
- Título grande + bullet: "Cada algoritmo demonstrado com o nosso próprio exemplo"
- Tabela de rastreabilidade (mostra que é autoral):

| Algoritmo | Arquivo | Cenário autoral na demo |
|-----------|---------|--------------------------|
| Fibonacci | `src/fibonacci.py` | Exército de demônios de Muzan / Demon Slayer (noite 10) |
| Mochila 0/1 | `src/mochila.py` | Mochila do treinador Pokémon (5 itens, 10 espaços) |
| Caminho Mínimo | `src/caminho_minimo.py` | Fortaleza Infinita de Muzan (Portão → Trono de Muzan) |
| Subsequência Comum Máxima (LCS) | `src/lcs.py` | Times Pokémon de dois treinadores (estratégia comum) |

- 💬 *Fala:* "Para fechar, vamos rodar o código ao vivo. Repare que cada programa usa exatamente o exemplo que mostramos nos slides — não é código genérico de livro, a entrada é o nosso próprio cenário."

**Demo 1 — rodar tudo com um único comando** (terminal projetado, ao vivo):

```bash
./apresentar.sh
```

Esse script mostra uma tela por algoritmo e termina com os testes. A navegação é
pelas **setas do teclado**: `->` (ou Enter/espaço) avança, `<-` volta, `q` sai.
Cada tela substitui a anterior, então dá para ir e voltar à vontade durante a
arguição. Comente cada saída em uma frase, ligando ao slide correspondente
("aqui está o exército de demônios de Muzan que vimos no slide 4", etc.).

> Alternativa sem interação: `./apresentar.sh --auto` (roda tudo em sequência).
> Para rodar um algoritmo isolado: `python3 src/fibonacci.py` (ou `mochila`,
> `caminho_minimo`, `lcs`).

**Slide 16 — "E como sabemos que está correto?"**
- Explicar a estratégia de **teste-gabarito**: para a Mochila e a LCS, a versão
  DP é comparada contra a força bruta / recursão ingênua em vários casos — se
  batessem por acaso, não passariam em todos.
- Detalhar o que cada grupo de testes valida (o próprio `apresentar.sh` narra
  isso na etapa 5/5, em modo `-v`):
  - **Fibonacci**: as 3 abordagens concordam de F(0) a F(10); F(50) sem estouro
    de pilha; `n` negativo gera erro.
  - **Mochila 0/1**: DP == força bruta para toda capacidade de 0 a 20; a solução
    nunca estoura a mochila; casos-limite (capacidade zero, sem itens).
  - **Caminho mínimo**: custo/rota corretos; origem = destino → 0; sem caminho →
    infinito; grafo com ciclo gera erro (exige DAG).
  - **LCS**: recursivo == DP; a subsequência é de fato comum aos dois times;
    casos-limite (sem comuns, vazios).
- 💬 *Fala:* "Mas como sabemos que está mesmo correto? A gente comparou a versão por DP contra a força bruta, que testa todas as possibilidades. Se as duas batem em dezenas de casos, a DP está certa. São 26 testes e, como vocês vão ver, todos passam."

**Demo 2 — a suíte de testes** (já é a última etapa do `apresentar.sh`):

O próprio `apresentar.sh` encerra rodando `python3 -m pytest tests/ -q`. Se
quiser rodar isolado (ex.: responder a uma pergunta do professor):

```bash
python3 -m pytest tests/ -q
```

Saída esperada na tela: **`26 passed`**. Deixe esse resultado visível ao
encerrar — é a prova final de qualidade técnica.

> **Prints prontos para os slides.** Cada **tela completa** da demo (explicação
> + comando + saída, com as cores do terminal) está renderizada em `assets/`,
> pronta para arrastar para os slides — funciona como anexo e como plano B caso
> o terminal/projetor falhe:
>
> | Imagem | Conteúdo (tela da demo) |
> |--------|--------------------------|
> | `assets/saida_fibonacci.png` | Etapa 1/5: explicação + saída do Fibonacci |
> | `assets/saida_mochila.png` | Etapa 2/5: explicação + saída da Mochila 0/1 |
> | `assets/saida_caminho_minimo.png` | Etapa 3/5: explicação + rota (9 min) |
> | `assets/saida_lcs.png` | Etapa 4/5: explicação + LCS dos times (= 4) |
> | `assets/saida_testes.png` | Etapa 5/5: explicação dos testes + `26 passed` (`-v`) |
>
> As imagens são geradas a partir do próprio `apresentar.sh`, então refletem
> exatamente o que a banca vê. Para regerar: `python3 assets/gerar_prints.py`

**Slide 17 — Encerramento / Obrigado + Perguntas**
- Link do repositório no GitHub
- Abrir para perguntas (apoio: as 20 respostas de [`perguntas.md`](perguntas.md))
- 💬 *Fala:* "Esse é o nosso projeto, todo no repositório do link. Obrigado pela atenção — estamos abertos a perguntas."

---

## Por que as demos garantem autoria

- O **algoritmo** (a função de DP) é universal — não há como "inventar" Fibonacci.
  O que é **autoral** é a **modelagem do problema**: traduzimos cada algoritmo
  para um cenário original e usamos esse cenário como entrada real do programa.
- Nenhum exemplo reproduz os enunciados dos livros (coelhos de Fibonacci, itens
  genéricos de mochila, strings "ABCBDAB" de LCS). Trocamos por demônios de
  Muzan, a mochila de um treinador Pokémon, a Fortaleza Infinita e times Pokémon.
- Mostrar a demo rodando com esses dados, ao vivo, evidencia para a banca que o
  material foi construído pelo grupo, e não copiado.

## Checklist antes de apresentar

- [ ] Slides exportados e testados no projetor (fontes e diagramas legíveis ao fundo).
- [ ] Diagramas Mermaid convertidos em imagem (não dependa de internet na hora).
- [ ] Terminal com fonte aumentada e a pasta do projeto já aberta.
- [ ] `python3 --version` ≥ 3.12 e `pytest` instalado na máquina da apresentação.
- [ ] Ensaiar a demo uma vez (plano B já pronto: os prints em `assets/saida_*.png`
      podem virar um slide, caso a internet/projetor/terminal falhe).
- [ ] Cronometrar: blocos de fala ~13–18 min + demo ~3–5 min.
