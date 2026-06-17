"""Fibonacci, três abordagens didáticas de Programação Dinâmica.

Este módulo demonstra a evolução de uma recorrência exponencial ingênua
para soluções polinomiais usando memoization (top-down) e tabulation
(bottom-up).

A motivação autoral do projeto é o "exército de demônios de Muzan"
(Demon Slayer): a cada noite, todo demônio já fortalecido transforma um
humano em demônio; o recém-transformado leva uma noite para acumular
sangue suficiente e só então passa a transformar outros. O total de
demônios fortalecidos na noite n segue exatamente a recorrência de
Fibonacci.

Recorrência:
    F(0) = 0
    F(1) = 1
    F(n) = F(n-1) + F(n-2),  para n >= 2

Compatível com Python 3.12+.
"""

from __future__ import annotations

from functools import lru_cache


# ---------------------------------------------------------------------------
# Abordagem 1: recursão pura (ingênua)          tempo O(phi^n), espaço O(n)
# Traduz a fórmula direto em código. É a mais legível, mas F(n-1) e F(n-2)
# recalculam os mesmos valores sem parar, então o custo explode. Está aqui
# como ponto de partida: é o "jeito lento" que a DP vem melhorar.
# ---------------------------------------------------------------------------


def fib_recursivo(n: int) -> int:
    """Calcula F(n) pela definição recursiva pura.

    Reavalia os mesmos subproblemas inúmeras vezes (sobreposição de
    subproblemas). Serve apenas como linha de base para comparação.

    Complexidade: tempo O(phi^n), espaço O(n) (pilha de recursão).
    """
    if n < 0:
        raise ValueError("n deve ser não-negativo")
    if n < 2:
        return n
    return fib_recursivo(n - 1) + fib_recursivo(n - 2)


# ---------------------------------------------------------------------------
# Abordagem 2: memoization / top-down            tempo O(n), espaço O(n)
# É a mesma recursão de antes, mas guardando num cache cada F(k) já
# calculado. Assim cada subproblema é resolvido uma única vez: a árvore de
# chamadas deixa de ser exponencial e o custo cai para linear.
# ---------------------------------------------------------------------------


def fib_memo(n: int, memo: dict[int, int] | None = None) -> int:
    """Calcula F(n) com cache explícito dos subproblemas.

    Cada valor F(k) é computado uma única vez e reutilizado, reduzindo o
    tempo de exponencial para linear.

    Complexidade: tempo O(n), espaço O(n).
    """
    if n < 0:
        raise ValueError("n deve ser não-negativo")
    if memo is None:
        memo = {0: 0, 1: 1}
    if n in memo:  # subproblema já resolvido: devolve o valor guardado
        return memo[n]
    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]


@lru_cache(maxsize=None)
def fib_memo_lru(n: int) -> int:
    """Variante idiomática usando o cache embutido da biblioteca padrão."""
    if n < 0:
        raise ValueError("n deve ser não-negativo")
    if n < 2:
        return n
    return fib_memo_lru(n - 1) + fib_memo_lru(n - 2)


# ---------------------------------------------------------------------------
# Abordagem 3: tabulation / bottom-up            tempo O(n), espaço O(1)
# Em vez de descer recursivamente, monta a resposta do menor para o maior.
# Como só os dois últimos termos importam para o próximo, guardamos apenas
# eles e não a tabela inteira: isso reduz o espaço para constante.
# ---------------------------------------------------------------------------


def fib_tabulation(n: int) -> int:
    """Calcula F(n) preenchendo a tabela do menor para o maior subproblema.

    Mantém apenas os dois últimos valores, alcançando espaço constante.

    Complexidade: tempo O(n), espaço O(1).
    """
    if n < 0:
        raise ValueError("n deve ser não-negativo")
    if n < 2:
        return n
    # guarda apenas os dois termos anteriores e desliza a janela a cada passo
    anterior, atual = 0, 1
    for _ in range(2, n + 1):
        anterior, atual = atual, anterior + atual
    return atual


def fib_sequencia(n: int) -> list[int]:
    """Retorna a lista [F(0), F(1), ..., F(n)] usando tabulation."""
    if n < 0:
        raise ValueError("n deve ser não-negativo")
    # casos base; a fatia evita devolver [0, 1] quando n == 0
    tabela = [0, 1][: n + 1] if n < 2 else [0, 1]
    for i in range(2, n + 1):
        tabela.append(tabela[i - 1] + tabela[i - 2])
    return tabela


if __name__ == "__main__":
    N = 10
    print(f"Demônios fortalecidos a cada noite, até a noite {N}:")
    print(fib_sequencia(N))
    print(f"\nF({N}) recursivo   = {fib_recursivo(N)}")
    print(f"F({N}) memoization = {fib_memo(N)}")
    print(f"F({N}) tabulation  = {fib_tabulation(N)}")
