"""Mochila 0/1 (0/1 Knapsack), força bruta vs. Programação Dinâmica.

Problema: dado um conjunto de itens, cada um com um peso e um valor, e uma
capacidade máxima de peso, selecionar um subconjunto que maximize o valor
total sem ultrapassar a capacidade. Cada item é indivisível: ou entra
inteiro na mochila, ou não entra (daí o "0/1").

Cenário autoral do projeto (Pokémon): um treinador, antes de enfrentar a
Liga, tem uma mochila com espaço limitado e precisa escolher, entre os
itens disponíveis, a combinação que maximize a utilidade estratégica em
batalha sem estourar o espaço da mochila.

Recorrência (M[i][c] = melhor valor usando os i primeiros itens com
capacidade c):
    M[0][c] = 0
    M[i][c] = M[i-1][c],                              se peso[i] > c
    M[i][c] = max(M[i-1][c],
                  valor[i] + M[i-1][c - peso[i]]),    caso contrário

Compatível com Python 3.12+.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations


@dataclass(frozen=True)
class Item:
    """Item candidato à mochila."""

    nome: str
    peso: int
    valor: int


# ---------------------------------------------------------------------------
# Abordagem 1: força bruta                        tempo O(2^n)
# Testa TODAS as combinações de itens e fica com a de maior valor que ainda
# cabe na mochila. Sempre acha o ótimo, mas vira inviável com muitos itens
# (2^n combinações). Aqui ela serve de gabarito para validar a versão DP.
# ---------------------------------------------------------------------------


def mochila_forca_bruta(itens: list[Item], capacidade: int) -> tuple[int, list[Item]]:
    """Testa todos os subconjuntos possíveis dos itens.

    Avalia 2^n combinações, sendo n o número de itens. Inviável para
    entradas grandes, mas útil como referência de correção.

    Retorna (valor_total, itens_escolhidos).
    """
    melhor_valor = 0
    melhor_conjunto: list[Item] = []
    # gera todos os subconjuntos, de tamanho 0 até n, e guarda o melhor viável
    for tamanho in range(len(itens) + 1):
        for combinacao in combinations(itens, tamanho):
            peso_total = sum(item.peso for item in combinacao)
            valor_total = sum(item.valor for item in combinacao)
            if peso_total <= capacidade and valor_total > melhor_valor:
                melhor_valor = valor_total
                melhor_conjunto = list(combinacao)
    return melhor_valor, melhor_conjunto


# ---------------------------------------------------------------------------
# Abordagem 2: Programação Dinâmica               tempo O(n * W)
# Monta uma tabela onde a linha é o item e a coluna é a capacidade. Cada
# célula responde a uma pergunta: "com estes itens e este espaço, qual o
# maior valor possível?". A resposta de cada célula reaproveita as de cima.
# ---------------------------------------------------------------------------


def mochila_dp(itens: list[Item], capacidade: int) -> tuple[int, list[Item]]:
    """Resolve a mochila 0/1 com uma tabela DP e reconstrói a solução.

    Complexidade pseudo-polinomial: tempo O(n * W), espaço O(n * W), onde
    n é o número de itens e W a capacidade.

    Retorna (valor_total, itens_escolhidos).
    """
    n = len(itens)
    # tabela[i][c] = melhor valor com os i primeiros itens e capacidade c
    tabela = [[0] * (capacidade + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        item = itens[i - 1]
        for c in range(capacidade + 1):
            if item.peso > c:
                # o item não cabe na capacidade c: repete o valor sem ele
                tabela[i][c] = tabela[i - 1][c]
            else:
                # escolhe o melhor entre deixar o item de fora e incluí-lo
                sem_item = tabela[i - 1][c]
                com_item = item.valor + tabela[i - 1][c - item.peso]
                tabela[i][c] = max(sem_item, com_item)

    # Reconstrução: se o valor de uma linha difere da linha de cima, o item i
    # foi incluído; nesse caso, recua a capacidade pelo peso dele.
    escolhidos: list[Item] = []
    c = capacidade
    for i in range(n, 0, -1):
        if tabela[i][c] != tabela[i - 1][c]:
            item = itens[i - 1]
            escolhidos.append(item)
            c -= item.peso
    escolhidos.reverse()

    return tabela[n][capacidade], escolhidos


# ---------------------------------------------------------------------------
# Variante da abordagem 2: DP com espaço O(W)
# Como cada linha da tabela só depende da linha imediatamente acima, dá para
# guardar apenas UMA linha e atualizá-la no lugar. Mais econômica em memória,
# porém abre mão da reconstrução (devolve só o valor ótimo).
# ---------------------------------------------------------------------------


def mochila_dp_otimizada(itens: list[Item], capacidade: int) -> int:
    """Versão com espaço O(W) usando um único vetor (sem reconstrução).

    A iteração da capacidade é feita de trás para frente para garantir que
    cada item seja considerado no máximo uma vez (propriedade 0/1).
    """
    dp = [0] * (capacidade + 1)
    for item in itens:
        # percorre a capacidade em ordem decrescente para que dp[c - peso]
        # ainda represente o estado "sem este item" (evita reusá-lo)
        for c in range(capacidade, item.peso - 1, -1):
            dp[c] = max(dp[c], item.valor + dp[c - item.peso])
    return dp[capacidade]


if __name__ == "__main__":
    itens = [
        Item("Revive Máximo", peso=4, valor=12),
        Item("Super Poção", peso=3, valor=10),
        Item("Repelente", peso=2, valor=7),
        Item("Ultra Ball", peso=5, valor=16),
        Item("Restaurador Total", peso=6, valor=18),
    ]
    CAPACIDADE = 10  # espaços livres na mochila do treinador

    valor_bruto, escolha_bruta = mochila_forca_bruta(itens, CAPACIDADE)
    valor_dp, escolha_dp = mochila_dp(itens, CAPACIDADE)

    print(f"Espaço da mochila: {CAPACIDADE}")
    print(f"\nForça bruta -> utilidade {valor_bruto}: "
          f"{[i.nome for i in escolha_bruta]}")
    print(f"DP          -> utilidade {valor_dp}: "
          f"{[i.nome for i in escolha_dp]}")
    print(f"DP otimizada (só valor) -> {mochila_dp_otimizada(itens, CAPACIDADE)}")
