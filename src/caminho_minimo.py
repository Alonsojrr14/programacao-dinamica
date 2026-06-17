"""Caminho Mínimo em DAG, Programação Dinâmica sobre grafos acíclicos.

Quando o grafo é acíclico e direcionado (DAG), o caminho de custo mínimo
entre dois vértices pode ser resolvido por Programação Dinâmica: o menor
custo até um vértice depende apenas do menor custo até seus predecessores.
A ausência de ciclos garante uma ordem topológica em que cada subproblema
é resolvido antes de ser usado.

Cenário autoral do projeto (Demon Slayer): a Fortaleza Infinita de Muzan é
um labirinto cujas salas se conectam por passagens de mão única que nunca
voltam (estrutura acíclica). Um caçador de demônios quer a rota de menor
custo (tempo, em minutos) do Portão de entrada até o Trono de Muzan.

Recorrência (dist[v] = custo mínimo da origem s até v):
    dist[s] = 0
    dist[v] = min sobre (u, v) de  dist[u] + peso(u, v)

Complexidade: tempo O(V + E), espaço O(V + E).

Compatível com Python 3.12+.
"""

from __future__ import annotations

from collections import deque

# Grafo: dicionário de adjacência {origem: [(destino, peso), ...]}
Grafo = dict[str, list[tuple[str, int]]]


# ---------------------------------------------------------------------------
# Passo 1: ordenação topológica (algoritmo de Kahn)
# Antes de calcular custos, precisamos de uma ordem em que todo vértice
# apareça depois de quem aponta para ele. Essa ordem só existe se o grafo não
# tiver ciclos; é o que garante que, ao chegar num vértice, tudo de que ele
# depende já foi resolvido.
# ---------------------------------------------------------------------------


def ordem_topologica(grafo: Grafo) -> list[str]:
    """Retorna uma ordem topológica dos vértices (algoritmo de Kahn).

    Levanta ValueError se o grafo contiver ciclo (não é um DAG).
    """
    # conta quantas arestas chegam em cada vértice (grau de entrada)
    grau_entrada: dict[str, int] = {v: 0 for v in grafo}
    for vizinhos in grafo.values():
        for destino, _ in vizinhos:
            grau_entrada[destino] = grau_entrada.get(destino, 0) + 1
            # vértices que só aparecem como destino também viram chave do grafo
            grafo.setdefault(destino, grafo.get(destino, []))

    # processa primeiro os vértices sem dependências (grau de entrada zero)
    fila = deque(v for v, g in grau_entrada.items() if g == 0)
    ordem: list[str] = []
    while fila:
        u = fila.popleft()
        ordem.append(u)
        # ao "remover" u, libera seus vizinhos; os que zeram entram na fila
        for destino, _ in grafo.get(u, []):
            grau_entrada[destino] -= 1
            if grau_entrada[destino] == 0:
                fila.append(destino)

    if len(ordem) != len(grau_entrada):
        raise ValueError("O grafo possui ciclo; não é um DAG.")
    return ordem


# ---------------------------------------------------------------------------
# Passo 2: caminho mínimo por Programação Dinâmica       tempo O(V + E)
# Seguindo a ordem topológica, "relaxamos" cada aresta: se chegar a um vértice
# passando por outro sai mais barato, atualizamos seu custo. Como cada vértice
# é processado só depois de seus predecessores, o custo final já é o ótimo.
# ---------------------------------------------------------------------------


def caminho_minimo_dag(
    grafo: Grafo, origem: str, destino: str
) -> tuple[float, list[str]]:
    """Calcula o caminho de custo mínimo entre origem e destino em um DAG.

    Retorna (custo_total, rota). Se não houver caminho, custo é infinito e
    a rota é vazia.
    """
    ordem = ordem_topologica(grafo)

    dist: dict[str, float] = {v: float("inf") for v in grafo}
    anterior: dict[str, str | None] = {v: None for v in grafo}
    dist[origem] = 0

    # Relaxa as arestas seguindo a ordem topológica: ao processar u, seu
    # custo mínimo já é definitivo.
    for u in ordem:
        if dist[u] == float("inf"):
            continue
        for v, peso in grafo.get(u, []):
            if dist[u] + peso < dist[v]:
                dist[v] = dist[u] + peso
                anterior[v] = u

    # Reconstrói a rota do destino até a origem.
    if dist[destino] == float("inf"):
        return float("inf"), []

    rota: list[str] = []
    atual: str | None = destino
    while atual is not None:
        rota.append(atual)
        atual = anterior[atual]
    rota.reverse()

    return dist[destino], rota


if __name__ == "__main__":
    # Fortaleza Infinita: passagens de mão única entre salas e seus tempos.
    fortaleza: Grafo = {
        "Portão":            [("Corredor Suspenso", 4), ("Escada Invertida", 2)],
        "Corredor Suspenso": [("Câmara Central", 5), ("Salão dos Tatames", 6)],
        "Escada Invertida":  [("Salão dos Tatames", 3), ("Câmara Central", 8)],
        "Salão dos Tatames": [("Câmara Central", 1), ("Trono de Muzan", 9)],
        "Câmara Central":     [("Trono de Muzan", 3)],
        "Trono de Muzan":     [],
    }

    custo, rota = caminho_minimo_dag(fortaleza, "Portão", "Trono de Muzan")
    print(f"Rota de menor tempo (Portão -> Trono de Muzan): {custo} min")
    print(" -> ".join(rota))
