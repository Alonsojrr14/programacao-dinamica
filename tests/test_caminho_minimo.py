"""Testes do caminho mínimo em DAG."""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.caminho_minimo import caminho_minimo_dag, ordem_topologica  # noqa: E402

FORTALEZA = {
    "Portão":            [("Corredor Suspenso", 4), ("Escada Invertida", 2)],
    "Corredor Suspenso": [("Câmara Central", 5), ("Salão dos Tatames", 6)],
    "Escada Invertida":  [("Salão dos Tatames", 3), ("Câmara Central", 8)],
    "Salão dos Tatames": [("Câmara Central", 1), ("Trono de Muzan", 9)],
    "Câmara Central":     [("Trono de Muzan", 3)],
    "Trono de Muzan":     [],
}


def test_custo_e_rota_otimos() -> None:
    # Portão -> Escada Invertida(2) -> Salão dos Tatames(3) -> Câmara Central(1) -> Trono(3) = 9
    custo, rota = caminho_minimo_dag(FORTALEZA, "Portão", "Trono de Muzan")
    assert custo == 9
    assert rota == [
        "Portão",
        "Escada Invertida",
        "Salão dos Tatames",
        "Câmara Central",
        "Trono de Muzan",
    ]


def test_origem_igual_destino() -> None:
    custo, rota = caminho_minimo_dag(FORTALEZA, "Portão", "Portão")
    assert custo == 0
    assert rota == ["Portão"]


def test_sem_caminho() -> None:
    g = {"A": [("B", 1)], "B": [], "C": [("B", 1)]}
    custo, rota = caminho_minimo_dag(g, "A", "C")
    assert custo == float("inf")
    assert rota == []


def test_ciclo_levanta_erro() -> None:
    ciclico = {"A": [("B", 1)], "B": [("A", 1)]}
    with pytest.raises(ValueError):
        ordem_topologica(ciclico)
