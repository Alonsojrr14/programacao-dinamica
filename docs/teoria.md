# Fundamentos Teóricos da Programação Dinâmica

> Material autoral produzido a partir do estudo das referências listadas no
> README (CLRS, Kleinberg & Tardos, Skiena, Dasgupta-Papadimitriou-Vazirani).
> Os exemplos são originais.

## 1. O que é Programação Dinâmica

Programação Dinâmica (PD) é uma técnica de projeto de algoritmos para problemas
de **otimização** (e de contagem) que podem ser decompostos em subproblemas
**que se repetem**. A ideia central é resolver cada subproblema **uma única
vez** e armazenar seu resultado, evitando recomputações. O termo "programação"
aqui é histórico (Richard Bellman, década de 1950) e significa "planejamento
por tabelas", não programação de computadores.

A PD se aplica quando um problema satisfaz **duas propriedades**:

### 1.1 Subestrutura ótima
A solução ótima do problema contém, em seu interior, soluções ótimas dos
subproblemas. Formalmente, se uma decisão divide o problema em partes, a
combinação das soluções ótimas das partes produz a solução ótima do todo.

*Intuição autoral:* montar o time Pokémon de maior poder com 6 vagas inclui,
necessariamente, a melhor escolha para as 5 primeiras vagas dado o que sobra de
"orçamento de poder".

### 1.2 Sobreposição de subproblemas
O espaço de subproblemas é **pequeno** (polinomial), mas um algoritmo recursivo
ingênuo os revisita exponencialmente. É exatamente isso que a árvore de recursão
do Fibonacci evidencia: `F(3)` é recalculado várias vezes.

> Contraste: o Merge Sort também divide o problema, mas seus subproblemas são
> **disjuntos** (metades distintas do vetor). Por isso ele é Dividir-e-Conquistar
> e **não** se beneficia de PD.

## 2. As duas implementações canônicas

| Abordagem | Direção | Como funciona | Vantagem |
|-----------|---------|---------------|----------|
| **Memoization** (top-down) | do problema → base | Recursão normal + cache de resultados | Calcula só os subproblemas alcançados; código próximo da recorrência |
| **Tabulation** (bottom-up) | da base → problema | Itera preenchendo uma tabela | Sem custo de pilha de recursão; permite otimização de espaço |

Ambas têm a **mesma complexidade de tempo**. A escolha depende de: risco de
estouro de pilha, fração do espaço de estados realmente necessária e
possibilidade de reduzir memória (ex.: Fibonacci em `O(1)`).

## 3. Receita de 4 passos para projetar uma solução PD

1. **Caracterizar o estado**: que parâmetros identificam um subproblema?
   (ex.: `(i, capacidade)` na mochila).
2. **Escrever a recorrência**: como o valor ótimo de um estado se compõe a
   partir de estados menores? Definir também os **casos base**.
3. **Definir a ordem de avaliação**: garantir que todo estado dependa apenas de
   estados já computados (topo-down resolve via recursão; bottom-up via ordem).
4. **Reconstruir a solução** (opcional): além do valor ótimo, recuperar *quais*
   escolhas o produziram, fazendo *backtracking* pela tabela.

## 4. Quando NÃO usar PD

- Não há sobreposição de subproblemas → Dividir-e-Conquistar.
- A escolha localmente ótima já leva ao ótimo global → algoritmo **Guloso**
  (mais simples e rápido). Ex.: a mochila **fracionária** é gulosa; a **0/1**
  exige PD.
- O espaço de estados é exponencial mesmo após a modelagem → considerar
  heurísticas, aproximação ou programação inteira.

## 5. Resumo dos quatro problemas do projeto

| Problema | Estado | Recorrência (núcleo) | Base |
|----------|--------|----------------------|------|
| Fibonacci | `n` | `F(n)=F(n-1)+F(n-2)` | `F(0)=0, F(1)=1` |
| Mochila 0/1 | `(i, c)` | `M[i][c]=max(M[i-1][c], v_i+M[i-1][c-w_i])` | `M[0][c]=0` |
| Caminho mín. (DAG) | `v` | `d[v]=min_{(u,v)} d[u]+w(u,v)` | `d[s]=0` |
| LCS | `(i, j)` | igual/diferente → diagonal+1 ou max(↑,←) | `L[0][*]=L[*][0]=0` |
