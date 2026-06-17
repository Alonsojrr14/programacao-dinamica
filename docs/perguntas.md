# 20 Perguntas que o Professor Pode Fazer (com Respostas Ideais)

> Preparação para a arguição. Cada item traz a resposta ideal e o ponto-chave
> a enfatizar na defesa.

---

**1. Qual a diferença entre Programação Dinâmica e Dividir-e-Conquistar?**
Ambas decompõem o problema, mas em D&C os subproblemas são **disjuntos** (ex.: as
metades do Merge Sort), enquanto em PD eles **se sobrepõem**. A PD armazena
resultados para não recomputar; D&C não precisa de cache.
*Ponto-chave:* sobreposição de subproblemas.

**2. O que caracteriza a "subestrutura ótima"? Dê um contraexemplo de problema que não a tem.**
É a propriedade de que a solução ótima contém soluções ótimas dos subproblemas.
Contraexemplo: o **caminho mais longo simples** em um grafo geral, combinar
subcaminhos ótimos pode repetir vértices, violando a otimalidade.
*Ponto-chave:* nem todo problema de otimização tem subestrutura ótima.

**3. Memoization e Tabulation têm a mesma complexidade. Quando preferir cada uma?**
Mesmo tempo assintótico. Top-down (memoization) é preferível quando só uma
fração do espaço de estados é alcançada e o código deve seguir a recorrência;
bottom-up (tabulation) evita estouro de pilha e habilita otimização de espaço.
*Ponto-chave:* pilha vs. fração de estados vs. memória.

**4. Por que o Fibonacci recursivo é Θ(φⁿ) e não Θ(2ⁿ)?**
O número de chamadas obedece à própria recorrência de Fibonacci, cujo termo
dominante é `φⁿ/√5`, com φ ≈ 1,618 (razão áurea). É exponencial, mas com base
menor que 2 porque os dois ramos têm tamanhos diferentes (`n-1` e `n-2`).

**5. Como reduzir o espaço do Fibonacci para O(1)?**
Como `F(n)` depende só de `F(n-1)` e `F(n-2)`, mantemos apenas duas variáveis
e as atualizamos a cada passo, descartando a tabela completa.

**6. Por que a mochila 0/1 não pode ser resolvida por algoritmo guloso?**
Porque a escolha localmente melhor (maior valor ou maior densidade
valor/peso) pode impedir um conjunto global melhor. A indivisibilidade quebra a
troca contínua. A versão **fracionária**, sim, é gulosa.
*Ponto-chave:* exibir o contraexemplo da mochila do treinador Pokémon.

**7. O que significa a mochila 0/1 ser "pseudo-polinomial"? Isso contradiz ser NP-difícil?**
`O(n·W)` é polinomial no **valor** de `W`, mas `W` ocupa `log W` bits; no
**tamanho da entrada** ela é exponencial. Não há contradição: é eficiente só
quando `W` é numericamente pequeno.

**8. Como a tabela DP da mochila se reduz a um único vetor? Por que iterar a capacidade de trás para frente?**
Cada linha depende só da anterior, então um vetor 1D basta. Iteramos `c` de `W`
até `peso[i]` (decrescente) para garantir que `dp[c - peso]` ainda reflita a
linha **anterior**, assim cada item é usado no máximo uma vez (propriedade 0/1).
Iterar crescente daria a mochila **ilimitada**.

**9. Como recuperar quais itens entraram na mochila, e não só o valor ótimo?**
Backtracking: a partir de `M[n][W]`, se `M[i][c] ≠ M[i-1][c]` o item `i` foi
incluído; subtraímos seu peso de `c` e continuamos até `i = 0`.

**10. Por que usar PD em DAG em vez de Dijkstra para caminho mínimo?**
Em DAG, a ordem topológica torna o relaxamento linear Θ(V+E), sem fila de
prioridade, e **aceita pesos negativos** (Dijkstra não). Dijkstra é para grafos
gerais com pesos não-negativos.

**11. O que acontece com a abordagem se o grafo tiver ciclos?**
Não existe ordem topológica; a recorrência fica mal-definida (dependência
circular). Para pesos não-negativos usa-se Dijkstra; com pesos negativos sem
ciclo negativo, Bellman-Ford.

**12. Como a PD lida com arestas de peso negativo no DAG, e por que Dijkstra não consegue?**
Como a ordem topológica fixa a sequência de relaxamento independentemente do
sinal dos pesos, valores negativos são tratados normalmente. Dijkstra assume que
um nó "fechado" nunca melhora, premissa quebrada por pesos negativos.

**13. Qual a recorrência da LCS e o que cada caso representa?**
Se `X[i-1]==Y[j-1]`: `L[i][j]=L[i-1][j-1]+1` (estende a diagonal). Senão:
`L[i][j]=max(L[i-1][j], L[i][j-1])` (descarta o último de uma das sequências).
Base: linha/coluna 0 valem 0.

**14. Diferença entre subsequência e substring? Por que isso muda o algoritmo?**
Substring é **contígua**; subsequência preserva a ordem mas **pode ter buracos**.
LCS permite saltos, daí a recorrência 2D; "maior substring comum" usa outra
recorrência (zera quando os caracteres diferem).

**15. A LCS é única? O que o algoritmo retorna em caso de empate?**
Não necessariamente; pode haver várias LCS de mesmo comprimento. O comprimento é
único, mas a subsequência reconstruída depende da regra de desempate (no nosso
código, priorizamos `↑` quando `L[i-1][j] >= L[i][j-1]`).

**16. Como reduzir o espaço da LCS para O(min(m,n))?**
Mantendo apenas duas linhas (atual e anterior) da matriz, suficientes para o
**comprimento**. Reconstruir a subsequência com O(min) de espaço exige o
algoritmo de Hirschberg (divisão e conquista sobre a matriz).

**17. Como provar que uma solução de PD é correta?**
Por indução sobre o tamanho do subproblema: mostra-se que os casos base estão
corretos e que a recorrência preserva a otimalidade (a melhor decisão sobre
soluções ótimas dos subproblemas produz a solução ótima do estado atual).

**18. Como você define o "espaço de estados" e por que ele determina a complexidade?**
É o conjunto de subproblemas distintos (ex.: `(i,c)` na mochila). O custo total é
(nº de estados) × (custo por transição), pois cada estado é resolvido uma vez.

**19. PD sempre supera a solução recursiva? Há overhead escondido?**
Em tempo assintótico, sim, quando há sobreposição. Mas há custo de **memória**
(a tabela) e, na memoization, overhead de chamadas/hash. Para `n` minúsculo, a
recursão simples pode ser mais rápida na prática.

**20. Dê um problema do dia a dia para cada um dos quatro algoritmos.**
Fibonacci → modelagem de crescimento populacional/financeiro; Mochila 0/1 →
seleção de investimentos sob orçamento; Caminho mínimo em DAG → escalonamento de
tarefas/PERT-CPM; LCS → `git diff`, alinhamento de DNA e correção ortográfica.
