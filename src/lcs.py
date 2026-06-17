"""Subsequência Comum Máxima / LCS (Longest Common Subsequence).

Implementações recursiva e por Programação Dinâmica.

Uma subsequência é obtida removendo zero ou mais elementos de uma sequência,
mantendo a ordem relativa dos restantes (não precisa ser contígua). A LCS de
duas sequências é a subsequência comum de maior comprimento.

Cenário autoral do projeto (Pokémon): comparar a ordem dos times de dois
treinadores. Queremos a maior "espinha dorsal" de Pokémon que ambos
escalaram na mesma ordem relativa, útil para medir o quanto as estratégias
de equipe se parecem.

Recorrência (L[i][j] = LCS dos prefixos X[:i] e Y[:j]):
    L[0][j] = L[i][0] = 0
    L[i][j] = L[i-1][j-1] + 1,                      se X[i-1] == Y[j-1]
    L[i][j] = max(L[i-1][j], L[i][j-1]),            caso contrário

Complexidade da versão DP: tempo O(m * n), espaço O(m * n).

Compatível com Python 3.12+.
"""

from __future__ import annotations

from collections.abc import Sequence

# ---------------------------------------------------------------------------
# Abordagem 1: recursão ingênua                  tempo O(2^(m+n)) no pior caso
# Compara os últimos elementos: se forem iguais, fazem parte da LCS e segue-se
# com os dois prefixos menores; se não, testa-se descartar um de cada lado e
# pega-se o melhor. Sem cache, refaz os mesmos prefixos e fica exponencial.
# ---------------------------------------------------------------------------


def lcs_recursivo(x: Sequence[str], y: Sequence[str]) -> int:
    """Retorna apenas o comprimento da LCS pela definição recursiva.

    Reavalia os mesmos prefixos repetidamente; serve de linha de base.
    """

    def aux(i: int, j: int) -> int:
        if i == 0 or j == 0:  # prefixo vazio: não há subsequência comum
            return 0
        if x[i - 1] == y[j - 1]:
            # elementos coincidem: contam +1 e avançam nos dois prefixos
            return aux(i - 1, j - 1) + 1
        # não coincidem: tenta descartar o último de cada lado e fica no melhor
        return max(aux(i - 1, j), aux(i, j - 1))

    return aux(len(x), len(y))


# ---------------------------------------------------------------------------
# Abordagem 2: Programação Dinâmica (tabulation)   tempo O(m * n)
# Preenche uma matriz com a mesma lógica da recursão, mas só uma vez por
# célula. Depois "caminha de volta" pela matriz para recuperar quais
# elementos formam a subsequência, não apenas o seu tamanho.
# ---------------------------------------------------------------------------


def lcs_dp(x: Sequence[str], y: Sequence[str]) -> tuple[int, list[str]]:
    """Calcula o comprimento da LCS e reconstrói uma subsequência ótima.

    Retorna (comprimento, subsequencia). Quando há empate, prioriza o
    movimento diagonal/para cima de forma determinística.

    Complexidade: tempo O(m * n), espaço O(m * n).
    """
    m, n = len(x), len(y)
    # L[i][j] = comprimento da LCS de x[:i] e y[:j]
    L = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:
                # elementos iguais: aproveita a diagonal e soma 1
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                # diferentes: herda o maior valor vizinho (de cima ou da esquerda)
                L[i][j] = max(L[i - 1][j], L[i][j - 1])

    # Reconstrução: parte do canto final da matriz e refaz o caminho ao contrário.
    # Onde os elementos coincidiram, aquele elemento entra na subsequência.
    subsequencia: list[str] = []
    i, j = m, n
    while i > 0 and j > 0:
        if x[i - 1] == y[j - 1]:
            subsequencia.append(x[i - 1])
            i -= 1
            j -= 1
        elif L[i - 1][j] >= L[i][j - 1]:
            i -= 1  # empate/maior para cima: desempate determinístico
        else:
            j -= 1
    subsequencia.reverse()  # foi montada do fim para o começo

    return L[m][n], subsequencia


def matriz_lcs(x: Sequence[str], y: Sequence[str]) -> list[list[int]]:
    """Retorna a matriz completa L de programação dinâmica (para didática)."""
    m, n = len(x), len(y)
    L = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])
    return L


if __name__ == "__main__":
    time_ash = ["Bulbasaur", "Charmander", "Squirtle", "Pikachu", "Snorlax", "Gengar"]
    time_gary = ["Charmander", "Squirtle", "Mewtwo", "Pikachu", "Gengar", "Lugia"]

    comprimento, espinha = lcs_dp(time_ash, time_gary)
    print("Time do Ash: ", time_ash)
    print("Time do Gary:", time_gary)
    print(f"\nPokémon na mesma ordem em ambos (LCS = {comprimento}):")
    print(" -> ".join(espinha))
