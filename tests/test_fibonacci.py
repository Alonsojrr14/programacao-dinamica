"""Testes da implementação de Fibonacci."""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.fibonacci import (  # noqa: E402
    fib_memo,
    fib_memo_lru,
    fib_recursivo,
    fib_sequencia,
    fib_tabulation,
)

ESPERADO = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]


@pytest.mark.parametrize("n,esperado", list(enumerate(ESPERADO)))
def test_todas_abordagens_concordam(n: int, esperado: int) -> None:
    assert fib_recursivo(n) == esperado
    assert fib_memo(n) == esperado
    assert fib_memo_lru(n) == esperado
    assert fib_tabulation(n) == esperado


def test_sequencia() -> None:
    assert fib_sequencia(10) == ESPERADO


def test_valor_grande_via_dp() -> None:
    # Tabulation aguenta n alto sem estouro de pilha.
    assert fib_tabulation(50) == 12586269025


def test_n_negativo_levanta_erro() -> None:
    for fn in (fib_recursivo, fib_memo, fib_tabulation, fib_sequencia):
        with pytest.raises(ValueError):
            fn(-1)
