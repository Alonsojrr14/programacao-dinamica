"""Gera imagens PNG das telas da apresentação ao vivo (apresentar.sh).

Em vez de capturar apenas a saída crua de cada programa, este gerador roda o
próprio apresentar.sh em modo --auto, separa o resultado por tela (cada
"clear" do script vira uma tela) e renderiza cada uma como um cartão de
terminal, preservando as cores. Assim os prints mostram EXATAMENTE o que a
banca vê, com toda a narração explicativa.

Uso:
    python3 assets/gerar_prints.py

As imagens são salvas em assets/saida_*.png.
"""

from __future__ import annotations

import re
import subprocess
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

RAIZ = Path(__file__).resolve().parents[1]
SAIDA = RAIZ / "assets"

COR_FUNDO = "#0d1117"
COR_BARRA = "#161b22"
COR_TITULO = "#8b949e"

# Mapeia os códigos ANSI usados no apresentar.sh para cores de renderização.
COR_PADRAO = "#e6edf3"
MAPA_CORES = {
    "0": COR_PADRAO,
    "": COR_PADRAO,
    "1": "#ffffff",        # negrito (rótulos de seção)
    "1;36": "#79c0ff",     # azul (banners)
    "1;32": "#7ee787",     # verde (comando, FIM)
    "1;33": "#e3b341",     # amarelo (fórmulas, pontos-chave)
    "0;90": "#8b949e",     # cinza (cenário)
    "0;37": "#c9d1d9",     # branco esmaecido (parágrafos)
}

FONTES_CANDIDATAS = [
    "/System/Library/Fonts/Menlo.ttc",
    "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf",
    "/Library/Fonts/Courier New.ttf",
]
TAM_FONTE = 22
ESPACO_LINHA = 31
MARGEM = 32
TOPO_BARRA = 52

SGR = re.compile(r"\x1b\[([0-9;]*)m")           # códigos de cor
CONTROLE = re.compile(r"\x1b\[[0-9;]*[A-Za-z]")  # demais escapes (clear, cursor)
CAMINHO_PY = re.compile(r"/\S*/python3[0-9.]*")  # encurta o caminho do python


def carregar_fonte(tamanho: int) -> ImageFont.FreeTypeFont:
    for caminho in FONTES_CANDIDATAS:
        if Path(caminho).exists():
            return ImageFont.truetype(caminho, tamanho)
    raise FileNotFoundError("Nenhuma fonte monoespaçada encontrada.")


def capturar_telas() -> list[str]:
    """Roda apresentar.sh --auto e devolve uma lista de telas (texto cru com ANSI)."""
    resultado = subprocess.run(
        ["bash", "apresentar.sh", "--auto"],
        cwd=RAIZ,
        capture_output=True,
        text=True,
        check=True,
    )
    bruto = CAMINHO_PY.sub("python3", resultado.stdout)
    # Cada chamada a `clear` emite a sequência \x1b[2J: usamos como divisor.
    telas = bruto.split("\x1b[2J")
    return [t for t in telas if t.strip()]


def linha_para_spans(linha: str) -> list[tuple[str, str]]:
    """Quebra uma linha em trechos (texto, cor) interpretando os códigos ANSI."""
    linha = CONTROLE.sub("", linha)  # remove clear/cursor que sobraram
    spans: list[tuple[str, str]] = []
    pos = 0
    cor = COR_PADRAO
    for m in SGR.finditer(linha):
        if m.start() > pos:
            spans.append((linha[pos:m.start()], cor))
        cor = MAPA_CORES.get(m.group(1), COR_PADRAO)
        pos = m.end()
    if pos < len(linha):
        spans.append((linha[pos:], cor))
    return spans


def renderizar(nome_arquivo: str, titulo: str, tela: str) -> None:
    """Desenha uma tela inteira (com cores) como cartão de terminal."""
    fonte = carregar_fonte(TAM_FONTE)
    fonte_titulo = carregar_fonte(18)

    linhas = [linha_para_spans(l) for l in tela.split("\n")]
    # Remove linhas em branco no topo/rodapé.
    while linhas and not any(t.strip() for t, _ in linhas[0]):
        linhas.pop(0)
    while linhas and not any(t.strip() for t, _ in linhas[-1]):
        linhas.pop()

    img_temp = Image.new("RGB", (10, 10))
    draw_temp = ImageDraw.Draw(img_temp)

    def largura_linha(spans: list[tuple[str, str]]) -> float:
        return sum(draw_temp.textlength(t, font=fonte) for t, _ in spans)

    largura_max = max((largura_linha(spans) for spans in linhas), default=400)
    largura = int(largura_max) + 2 * MARGEM
    altura = TOPO_BARRA + 2 * MARGEM + len(linhas) * ESPACO_LINHA

    img = Image.new("RGB", (largura, altura), COR_FUNDO)
    draw = ImageDraw.Draw(img)

    draw.rectangle([0, 0, largura, TOPO_BARRA], fill=COR_BARRA)
    for i, cor in enumerate(["#ff5f56", "#ffbd2e", "#27c93f"]):
        cx = 26 + i * 26
        draw.ellipse([cx - 8, TOPO_BARRA // 2 - 8, cx + 8, TOPO_BARRA // 2 + 8], fill=cor)
    draw.text((largura / 2, TOPO_BARRA / 2), titulo,
              font=fonte_titulo, fill=COR_TITULO, anchor="mm")

    y = TOPO_BARRA + MARGEM
    for spans in linhas:
        x = MARGEM
        for texto, cor in spans:
            draw.text((x, y), texto, font=fonte, fill=cor)
            x += draw_temp.textlength(texto, font=fonte)
        y += ESPACO_LINHA

    destino = SAIDA / nome_arquivo
    img.save(destino)
    print(f"gerado: {destino.relative_to(RAIZ)}  ({largura}x{altura})")


# Marcador presente na tela  ->  (arquivo, título da barra)
TELAS = [
    ("1/5", "saida_fibonacci.png", "1/5  Fibonacci"),
    ("2/5", "saida_mochila.png", "2/5  Mochila 0/1"),
    ("3/5", "saida_caminho_minimo.png", "3/5  Caminho mínimo (DAG)"),
    ("4/5", "saida_lcs.png", "4/5  Subsequência Comum Máxima (LCS)"),
    ("5/5", "saida_testes.png", "5/5  Testes (pytest -v)"),
]


def main() -> None:
    telas = capturar_telas()

    def acha(marcador: str) -> str:
        for t in telas:
            if marcador in CONTROLE.sub("", SGR.sub("", t)):
                return t
        raise RuntimeError(f"Tela com marcador '{marcador}' não encontrada.")

    for marcador, arquivo, titulo in TELAS:
        renderizar(arquivo, titulo, acha(marcador))

    # Remove o print antigo que foi substituído pela tela 5/5 completa.
    antigo = SAIDA / "saida_testes_detalhado.png"
    if antigo.exists():
        antigo.unlink()
        print(f"removido (obsoleto): {antigo.relative_to(RAIZ)}")


if __name__ == "__main__":
    main()
