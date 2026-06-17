# Análise de Complexidade

> Comparação entre a abordagem ingênua e a abordagem por Programação Dinâmica
> de cada problema, com justificativa do ganho.

## 1. Fibonacci

| Abordagem | Tempo | Espaço | Observação |
|-----------|-------|--------|------------|
| Recursivo ingênuo | Θ(φⁿ) ≈ Θ(1,618ⁿ) | O(n) (pilha) | Nº de chamadas ≈ F(n); exponencial |
| Memoization | Θ(n) | Θ(n) | Cada `F(k)` calculado 1 vez |
| Tabulation | Θ(n) | **Θ(1)** | Mantém só 2 valores anteriores |

**Por que φⁿ?** A árvore de recursão tem ramificação dupla e altura `n`; o
número de folhas cresce conforme a própria sequência de Fibonacci, cujo termo
geral é dominado por `φⁿ/√5`. Memoization "poda" a árvore para um caminho linear.

**Ganho:** de exponencial para linear, para `n = 50`, passamos de ~2,5 bilhões
de chamadas para 49 iterações.

---

## 2. Mochila 0/1

| Abordagem | Tempo | Espaço | Observação |
|-----------|-------|--------|------------|
| Força bruta | Θ(2ⁿ) | O(n) | Testa todos os subconjuntos |
| DP (tabela) | Θ(n·W) | Θ(n·W) | `n` itens × `W` capacidades |
| DP (1 vetor) | Θ(n·W) | **Θ(W)** | Sem reconstrução da solução |

**Pseudo-polinomial:** `O(n·W)` depende do **valor** de `W`, não do seu número
de bits. Se `W` for codificado em binário, ele cresce exponencialmente no
tamanho da entrada, por isso a mochila 0/1 é NP-difícil, mas tratável quando
`W` é moderado.

**Ganho:** com `n = 40`, a força bruta enfrenta ~1,1 × 10¹² subconjuntos; a DP
com `W = 100` faz apenas 4.000 operações.

---

## 3. Caminho Mínimo em DAG

| Abordagem | Tempo | Espaço | Observação |
|-----------|-------|--------|------------|
| Enumerar todos os caminhos | O(caminhos) (até exponencial) | n/a | Inviável em grafos densos |
| Dijkstra | O((V+E) log V) | O(V) | Geral, mas exige pesos ≥ 0 |
| **DP em ordem topológica** | **Θ(V + E)** | Θ(V + E) | Aproveita a aciclicidade; aceita pesos negativos |

**Por que linear?** A ordenação topológica garante que, ao processar um vértice,
o custo mínimo até ele já é definitivo. Cada vértice e cada aresta é visitado
exatamente uma vez no relaxamento. É mais rápido que Dijkstra justamente por
não precisar de fila de prioridade.

---

## 4. Subsequência Comum Máxima (LCS)

| Abordagem | Tempo | Espaço | Observação |
|-----------|-------|--------|------------|
| Recursivo ingênuo | O(2^(m+n)) | O(m+n) | Reavalia prefixos |
| DP (matriz) | Θ(m·n) | Θ(m·n) | Permite reconstruir a subsequência |
| DP (2 linhas) | Θ(m·n) | **Θ(min(m,n))** | Só comprimento (sem reconstrução) |

**Ganho:** para duas sequências de 30 elementos, o recursivo pode chegar a
~10¹⁸ chamadas; a matriz DP faz 900 preenchimentos.

---

## 5. Panorama comparativo

| Problema | Ingênuo | DP | Tipo de ganho |
|----------|---------|-----|---------------|
| Fibonacci | Θ(φⁿ) | Θ(n) | Exponencial → Linear |
| Mochila 0/1 | Θ(2ⁿ) | Θ(n·W) | Exponencial → Pseudo-polinomial |
| Caminho (DAG) | até exponencial | Θ(V+E) | → Linear no tamanho do grafo |
| LCS | Θ(2^(m+n)) | Θ(m·n) | Exponencial → Quadrático |

**Lição central:** a Programação Dinâmica troca **tempo** por **memória**.
Armazenar O(estados) resultados transforma uma explosão combinatória em um
preenchimento de tabela cujo custo é (nº de estados) × (custo por transição).
