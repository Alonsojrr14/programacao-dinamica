"""Testes da Mochila 0/1: força bruta e DP devem concordar no valor ótimo."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.mochila import (  # noqa: E402
    Item,
    mochila_dp,
    mochila_dp_otimizada,
    mochila_forca_bruta,
)

ITENS = [
    Item("Revive Máximo", 4, 12),
    Item("Super Poção", 3, 10),
    Item("Repelente", 2, 7),
    Item("Ultra Ball", 5, 16),
    Item("Restaurador Total", 6, 18),
]


def test_dp_iguala_forca_bruta() -> None:
    for capacidade in range(0, 21):
        valor_bruto, _ = mochila_forca_bruta(ITENS, capacidade)
        valor_dp, _ = mochila_dp(ITENS, capacidade)
        assert valor_dp == valor_bruto, f"falha em W={capacidade}"
        assert mochila_dp_otimizada(ITENS, capacidade) == valor_bruto


def test_solucao_respeita_capacidade() -> None:
    valor, escolhidos = mochila_dp(ITENS, 10)
    assert sum(i.peso for i in escolhidos) <= 10
    assert sum(i.valor for i in escolhidos) == valor


def test_capacidade_zero() -> None:
    valor, escolhidos = mochila_dp(ITENS, 0)
    assert valor == 0
    assert escolhidos == []


def test_lista_vazia() -> None:
    assert mochila_dp([], 10) == (0, [])
