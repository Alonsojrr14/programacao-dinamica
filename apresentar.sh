#!/usr/bin/env bash
#
# Roteiro de demonstração ao vivo - Grupo 8 (Programação Dinâmica).
#
# Executa os quatro algoritmos + os testes, com explicação de cada um na tela.
# Navegação entre as telas pelas SETAS do teclado (ou Enter para avançar).
#
# Uso:
#   ./apresentar.sh          # modo apresentação (navega com as setas)
#   ./apresentar.sh --auto   # roda tudo de uma vez, sem interação
#
# Controles no modo apresentação:
#   ->  /  seta para baixo  /  Enter  /  espaço   avança
#   <-  /  seta para cima                         volta
#   q                                             sai
#
# Dica: rode com a fonte do terminal aumentada para a banca enxergar.

set -uo pipefail

# Vai para a pasta do projeto, independentemente de onde o script foi chamado.
cd "$(dirname "$0")"

# Escolhe o interpretador Python disponível.
PY="$(command -v python3 || command -v python)"

# Cores ANSI.
AZUL='\033[1;36m'; VERDE='\033[1;32m'; AMARELO='\033[1;33m'; CINZA='\033[0;90m'
BRANCO='\033[0;37m'; NEGRITO='\033[1m'; RESET='\033[0m'

# Limpa a tela via ANSI (independe do TERM) e também o scrollback (\033[3J),
# para que a tela anterior não fique acessível ao rolar para cima.
limpar() { printf '\033[3J\033[H\033[2J'; }

secao() { echo -e "${NEGRITO}$1${RESET}"; }   # rótulo de seção
txt()   { echo -e "${BRANCO}$1${RESET}"; }    # parágrafo explicativo
chave() { echo -e "${AMARELO}$1${RESET}"; }   # fórmula / ponto-chave

cabecalho() {
  limpar
  echo -e "${AZUL}============================================================${RESET}"
  echo -e "${AZUL}  $1${RESET}"
  echo -e "${AZUL}============================================================${RESET}"
  echo -e "${CINZA}  $2${RESET}"
  echo
}

rodar() {
  echo -e "${VERDE}\$ $1${RESET}"
  echo
  eval "$1"
}

# ===========================================================================
# Telas (cada função desenha uma tela inteira; a navegação cuida de limpar).
# ===========================================================================

tela_capa() {
  limpar
  echo -e "${NEGRITO}"
  echo "  ============================================================"
  echo "   PROBLEMAS CLÁSSICOS DE PROGRAMAÇÃO DINÂMICA - GRUPO 8"
  echo "   Universidade Federal do Ceará"
  echo "   Projeto e Análise de Algoritmos"
  echo "  ============================================================"
  echo -e "${RESET}"
  echo -e "${CINZA}  Demonstração ao vivo dos 4 algoritmos + testes."
  echo -e "  Cada exemplo usa um cenário autoral elaborado pelo grupo.${RESET}"
}

tela_fibonacci() {
  cabecalho "1/5  FIBONACCI  (recursão x memoization x tabulation)" \
            "Cenário: exército de demônios de Muzan que cresce a cada noite."
  secao "O QUE É:"
  txt "Cada número da sequência é a soma dos dois anteriores. No nosso cenário,"
  txt "os demônios fortalecidos de hoje são os de ontem mais os que amadureceram"
  txt "(os de duas noites atrás). Esse padrão é exatamente a recorrência abaixo."
  echo
  chave "Recorrência: F(n) = F(n-1) + F(n-2)   |   base: F(0)=0, F(1)=1"
  echo
  secao "AS 3 ABORDAGENS (mesma resposta, custos diferentes):"
  txt " 1) Recursiva  : escreve a fórmula direto. Simples, porém RECALCULA os"
  txt "                 mesmos termos várias vezes -> custo exponencial (lenta)."
  txt " 2) Memoization: a mesma recursão, mas guarda em cache cada termo já"
  txt "                 calculado. Cada um é resolvido 1 vez -> custo linear."
  txt " 3) Tabulation : monta de baixo para cima e guarda só os 2 últimos"
  txt "                 termos -> linear no tempo e espaço constante O(1)."
  echo
  secao "O QUE OBSERVAR NA SAÍDA:"
  txt "As 3 abordagens chegam ao MESMO F(10)=55. O que muda é COMO se calcula:"
  txt "a DP evita o retrabalho da recursão ingênua."
  echo
  rodar "$PY src/fibonacci.py"
}

tela_mochila() {
  cabecalho "2/5  MOCHILA 0/1  (força bruta x DP)" \
            "Cenário: a mochila do treinador Pokémon antes da Liga."
  secao "O QUE É:"
  txt "Cada item tem um tamanho (espaço) e uma utilidade (valor). A mochila tem"
  txt "espaço limitado. Queremos a combinação de MAIOR utilidade que ainda cabe."
  txt "O '0/1' quer dizer: cada item entra inteiro ou não entra (não dá pela metade)."
  echo
  chave "Decisão por item: max( deixar de fora , incluir o item + resto do espaço )"
  echo
  secao "AS 2 ABORDAGENS:"
  txt " 1) Força bruta: testa TODAS as combinações (2^n). Acha o ótimo, mas"
  txt "                 fica impraticável quando há muitos itens."
  txt " 2) DP         : preenche uma tabela [item x espaço]. Cada célula reusa"
  txt "                 as respostas já calculadas -> custo O(n*W), bem menor."
  echo
  secao "POR QUE NÃO SER 'GULOSO':"
  txt "Pegar sempre o item de maior utilidade (Restaurador Total, 18) prende a"
  txt "mochila e perde a melhor combinação. Só a DP garante o ótimo global."
  echo
  secao "O QUE OBSERVAR NA SAÍDA:"
  txt "Força bruta e DP chegam ao MESMO valor (utilidade 33), escolhendo"
  txt "Super Poção + Repelente + Ultra Ball, que somam exatamente 10 de espaço."
  echo
  rodar "$PY src/mochila.py"
}

tela_caminho() {
  cabecalho "3/5  CAMINHO MÍNIMO em DAG" \
            "Cenário: a Fortaleza Infinita de Muzan (passagens de mão única)."
  secao "O QUE É:"
  txt "As salas se ligam por passagens de mão única que nunca voltam (um grafo"
  txt "sem ciclos, o 'DAG'). Queremos o caminho de MENOR tempo do Portão até o"
  txt "Trono de Muzan, somando os minutos de cada passagem."
  echo
  chave "Recorrência: d[v] = min( d[u] + peso(u,v) )  para toda aresta u -> v"
  echo
  secao "COMO A DP RESOLVE:"
  txt " 1) Ordem topológica: organiza as salas de modo que toda sala venha"
  txt "                      depois das que apontam para ela."
  txt " 2) Relaxamento     : nessa ordem, ao chegar numa sala já sabemos o"
  txt "                      menor custo de tudo que leva até ela -> é definitivo."
  echo
  secao "O QUE OBSERVAR NA SAÍDA:"
  txt "A rota mais curta NÃO é a mais direta. Ir por Salão dos Tatames -> Trono"
  txt "custaria 14 min; desviar pela Câmara Central fecha em 9 min. A DP acha isso"
  txt "sozinha, sem testar todos os caminhos possíveis."
  echo
  rodar "$PY src/caminho_minimo.py"
}

tela_lcs() {
  cabecalho "4/5  SUBSEQUÊNCIA COMUM MÁXIMA (LCS)" \
            "Cenário: comparar a ordem dos times Pokémon de dois treinadores."
  secao "O QUE É:"
  txt "Uma subsequência mantém a ORDEM dos elementos, mas pode pular alguns"
  txt "(não precisa ser uma sequência contígua). A LCS é a maior delas que"
  txt "aparece nos dois times ao mesmo tempo."
  echo
  chave "Iguais -> aproveita a diagonal e soma 1 | Diferentes -> herda o maior vizinho"
  echo
  secao "COMO A DP RESOLVE:"
  txt " 1) Preenche uma matriz comparando os dois times posição a posição."
  txt " 2) Depois 'caminha de volta' pela matriz para descobrir QUAIS Pokémon"
  txt "    formam a subsequência, e não apenas o tamanho dela."
  echo
  secao "O QUE OBSERVAR NA SAÍDA:"
  txt "Mesmo com Pokémon trocados e fora de posição, a DP encontra 4 deles na"
  txt "mesma ordem nos dois times. É o mesmo princípio que o 'git diff' usa para"
  txt "comparar versões de um arquivo."
  echo
  rodar "$PY src/lcs.py"
}

tela_testes() {
  cabecalho "5/5  PROVA DE CORREÇÃO  (pytest)" \
            "Como sabemos que os algoritmos estão realmente certos?"
  secao "A IDEIA GERAL:"
  txt "Não basta 'achar' que está certo: provamos rodando. A estratégia central é"
  txt "o teste-gabarito: comparar a DP contra a força bruta / recursão, que olham"
  txt "TODAS as possibilidades. Se a DP empata com o gabarito em muitos casos, ela"
  txt "está correta. Também checamos os casos-limite (entradas vazias, inválidas)."
  echo
  secao "O QUE CADA GRUPO VALIDA:"
  txt " - Fibonacci : as 3 abordagens concordam; F(50) sem estouro; entrada inválida."
  txt " - Mochila   : DP == força bruta de 0 a 20 de capacidade; casos-limite."
  txt " - Caminho   : custo/rota corretos; sem caminho -> infinito; ciclo -> erro."
  txt " - LCS       : recursivo == DP; subsequência realmente comum; casos-limite."
  echo
  chave "São 26 testes no total. O esperado: 26 passed."
  echo
  rodar "$PY -m pytest tests/ -v"
}

# Sequência de telas exibidas.
TELAS=(tela_capa tela_fibonacci tela_mochila tela_caminho tela_lcs tela_testes)

fim() {
  echo
  echo -e "${VERDE}${NEGRITO}"
  echo "  ============================================================"
  echo "   FIM DA DEMONSTRAÇÃO - Obrigado!  Perguntas?"
  echo "  ============================================================"
  echo -e "${RESET}"
}

# ===========================================================================
# Modo automático: roda tudo em sequência, sem interação.
# ===========================================================================
if [[ "${1:-}" == "--auto" ]]; then
  for tela in "${TELAS[@]}"; do
    "$tela"
    sleep 2
  done
  fim
  exit 0
fi

# ===========================================================================
# Modo apresentação: navegação pelas setas.
# ===========================================================================

# Lê uma tecla. Setas chegam como ESC + '[' + letra; devolvemos a string toda.
ler_tecla() {
  local k rest=""
  IFS= read -rsn1 k || true
  if [[ "$k" == $'\e' ]]; then
    IFS= read -rsn2 -t 0.01 rest || true
    k+="$rest"
  fi
  printf '%s' "$k"
}

rodape() {
  echo
  echo -e "${CINZA}  [<- volta]   [-> / Enter avança]   [q sai]      tela $1/$2${RESET}"
}

i=0
total=${#TELAS[@]}
while (( i < total )); do
  "${TELAS[$i]}"
  rodape "$((i + 1))" "$total"
  case "$(ler_tecla)" in
    $'\e[C' | $'\e[B' | '' | ' ') i=$((i + 1)) ;;        # direita/baixo/Enter/espaço
    $'\e[D' | $'\e[A')            (( i > 0 )) && i=$((i - 1)) ;;  # esquerda/cima
    q | Q)                        limpar; exit 0 ;;
  esac
done

limpar
fim
