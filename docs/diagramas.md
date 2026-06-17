# Diagramas (Mermaid)

> Todos os diagramas abaixo são renderizados nativamente pelo GitHub. Basta
> visualizar este arquivo no repositório.

---

## 1. O método da Programação Dinâmica

```mermaid
flowchart TD
    A[Problema de otimização] --> B{Tem subestrutura ótima?}
    B -- Não --> X[DP não se aplica diretamente]
    B -- Sim --> C{Os subproblemas se sobrepõem?}
    C -- Não --> D[Use Dividir e Conquistar]
    C -- Sim --> E[Programação Dinâmica]
    E --> F[Top-down: Memoization]
    E --> G[Bottom-up: Tabulation]
    F --> H[Resolve sob demanda e<br/>guarda em cache]
    G --> I[Preenche tabela da base<br/>até a solução final]
    H --> J[Solução ótima]
    I --> J
```

---

## 2. Árvore de recursão do Fibonacci (recorrência ingênua)

Observe como `F(2)` e `F(1)` reaparecem várias vezes, é a **sobreposição de
subproblemas** que a DP elimina.

```mermaid
graph TD
    F5["F(5)"] --> F4["F(4)"]
    F5 --> F3a["F(3)"]
    F4 --> F3b["F(3)"]
    F4 --> F2a["F(2)"]
    F3a --> F2b["F(2)"]
    F3a --> F1a["F(1)"]
    F3b --> F2c["F(2)"]
    F3b --> F1b["F(1)"]
    F2a --> F1c["F(1)"]
    F2a --> F0a["F(0)"]
    F2b --> F1d["F(1)"]
    F2b --> F0b["F(0)"]
    F2c --> F1e["F(1)"]
    F2c --> F0c["F(0)"]
```

---

## 3. Mochila 0/1: decisão por item

```mermaid
flowchart TD
    S["Estado M[i][c]: itens 1..i, capacidade c"] --> Q{"peso[i] &le; c ?"}
    Q -- Não --> N["Não cabe:<br/>M[i][c] = M[i-1][c]"]
    Q -- Sim --> D{"Vale a pena incluir?"}
    D -- "Incluir" --> I["valor[i] + M[i-1][c - peso[i]]"]
    D -- "Pular" --> P["M[i-1][c]"]
    I --> M["M[i][c] = max(incluir, pular)"]
    P --> M
```

---

## 4. Caminho mínimo em DAG: relaxamento em ordem topológica

```mermaid
flowchart LR
    P((Portão)) -- 4 --> CS((Corredor Suspenso))
    P -- 2 --> EI((Escada Invertida))
    CS -- 5 --> CC((Câmara Central))
    CS -- 6 --> ST((Salão dos Tatames))
    EI -- 3 --> ST
    EI -- 8 --> CC
    ST -- 1 --> CC
    ST -- 9 --> TM((Trono de Muzan))
    CC -- 3 --> TM

    classDef rota fill:#2e7d32,color:#fff,stroke:#1b5e20,stroke-width:2px;
    class P,EI,ST,CC,TM rota
```

> Em verde, a rota ótima `Portão → Escada Invertida → Salão dos Tatames → Câmara
> Central → Trono de Muzan` (custo total = 9 minutos).

---

## 5. Subsequência Comum Máxima (LCS): direção do preenchimento e da reconstrução

```mermaid
flowchart TD
    A["L[i][j]"] --> B{"X[i-1] == Y[j-1] ?"}
    B -- Sim --> C["L[i-1][j-1] + 1<br/>(diagonal)"]
    B -- Não --> D["max(L[i-1][j], L[i][j-1])<br/>(cima ou esquerda)"]
    C --> E["Caracter entra na LCS"]
    D --> F["Caracter descartado"]
```

---

## 6. Fluxo geral de execução do projeto

```mermaid
sequenceDiagram
    participant U as Usuário
    participant M as main / módulo
    participant DP as Tabela DP
    U->>M: entrada (n, itens, grafo, sequências)
    M->>DP: preenche subproblemas (base -> topo)
    DP-->>M: valor ótimo
    M->>DP: reconstrói solução (backtracking)
    DP-->>M: itens / rota / subsequência
    M-->>U: resultado + solução ótima
```

---

## 7. Comparação de crescimento assintótico

```mermaid
flowchart LR
    subgraph Ingênuo
      A1["Fibonacci: O(&phi;^n)"]
      A2["Mochila: O(2^n)"]
      A3["LCS: O(2^(m+n))"]
    end
    subgraph Programação Dinâmica
      B1["Fibonacci: O(n)"]
      B2["Mochila: O(n&middot;W)"]
      B3["LCS: O(m&middot;n)"]
    end
    A1 -.reduz para.-> B1
    A2 -.reduz para.-> B2
    A3 -.reduz para.-> B3
```
