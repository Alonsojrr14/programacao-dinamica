"""Testes da Subsequência Comum Máxima (LCS)."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.lcs import lcs_dp, lcs_recursivo  # noqa: E402


def test_comprimento_recursivo_igual_dp() -> None:
    x = list("ABCBDAB")
    y = list("BDCAB")
    comprimento_rec = lcs_recursivo(x, y)
    comprimento_dp, sub = lcs_dp(x, y)
    assert comprimento_rec == comprimento_dp == 4
    assert len(sub) == 4


def test_subsequencia_eh_valida() -> None:
    time_ash = ["Bulbasaur", "Charmander", "Squirtle", "Pikachu", "Snorlax", "Gengar"]
    time_gary = ["Charmander", "Squirtle", "Mewtwo", "Pikachu", "Gengar", "Lugia"]
    comprimento, sub = lcs_dp(time_ash, time_gary)
    assert comprimento == 4
    assert sub == ["Charmander", "Squirtle", "Pikachu", "Gengar"]
    # Confere que sub é subsequência de ambos os times.
    assert _eh_subsequencia(sub, time_ash)
    assert _eh_subsequencia(sub, time_gary)


def test_sem_elementos_comuns() -> None:
    comprimento, sub = lcs_dp(list("ABC"), list("XYZ"))
    assert comprimento == 0
    assert sub == []


def test_sequencias_vazias() -> None:
    assert lcs_dp([], []) == (0, [])
    assert lcs_dp(list("ABC"), []) == (0, [])


def _eh_subsequencia(sub: list[str], seq: list[str]) -> bool:
    it = iter(seq)
    return all(elem in it for elem in sub)
