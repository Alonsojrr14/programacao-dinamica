# Exemplos Autorais: passo a passo

> Cenários originais criados para o projeto, ambientados em Pokémon e Demon
> Slayer. Nenhum reproduz literalmente os exemplos dos livros-texto.

---

## Exemplo 1: Fibonacci e o exército de demônios de Muzan

**Cenário.** Em Demon Slayer, Muzan transforma humanos em demônios. A regra
(adaptada para o exemplo): todo demônio já *fortalecido* transforma um humano por
noite; o recém-transformado precisa de **uma noite** para acumular sangue
suficiente e só então passa a transformar outros. Começamos com 1 demônio
fortalecido na noite 1.

**Entrada.** Número da noite `n = 7`.

**Processamento.** Seja `F(n)` o total de demônios fortalecidos na noite `n`. Os
fortalecidos de agora são os de antes (`F(n-1)`) mais os que amadureceram, que são
os fortalecidos de duas noites atrás (`F(n-2)`):

```
Noite:   0  1  2  3  4  5  6  7
F(n):    0  1  1  2  3  5  8  13
```

**Saída.** Na noite 7 o exército terá **13 demônios fortalecidos**.

**Explicação.** A recorrência `F(n)=F(n-1)+F(n-2)` aparece naturalmente. O código
recursivo recalcularia `F(5)` cinco vezes; com tabulation calculamos cada termo
uma vez e mantemos só os dois últimos (espaço O(1)).

---

## Exemplo 2: Mochila 0/1 e a mochila do treinador Pokémon

**Cenário.** Antes de enfrentar a Liga Pokémon, um treinador tem uma mochila com
**10 espaços** livres. Há cinco itens disponíveis; cada um ocupa um tamanho e tem
uma utilidade estratégica em batalha. Itens são indivisíveis: leva o item inteiro
ou não leva.

**Entrada.**

| Item | Tamanho | Utilidade |
|------|---------|-----------|
| Revive Máximo | 4 | 12 |
| Super Poção | 3 | 10 |
| Repelente | 2 | 7 |
| Ultra Ball | 5 | 16 |
| Restaurador Total | 6 | 18 |

**Processamento.** Preenchemos `M[i][c]`. Trecho final da tabela (capacidades
0..10) considerando os itens na ordem acima leva a `M[5][10] = 33`. A reconstrução
percorre a tabela de baixo para cima:

- Restaurador Total (i=5): incluir daria `18 + M[4][4]`; não compensa frente a `M[4][10]`. **Pula.**
- Ultra Ball (i=4): `16 + M[3][5]` supera `M[3][10]`. **Inclui** (restam 5 espaços).
- Repelente (i=3): `7 + M[2][3]` supera `M[2][5]`. **Inclui** (restam 3 espaços).
- Super Poção (i=2): `10 + M[1][0]` supera `M[1][3]`. **Inclui** (restam 0 espaços).
- Revive Máximo (i=1): sem espaço. **Pula.**

**Saída.** Levar **Super Poção + Repelente + Ultra Ball** → tamanho 3+2+5 = 10,
utilidade **33**.

**Explicação.** Um critério guloso por "maior utilidade" pegaria o Restaurador
Total (18) e depois ficaria preso; o guloso por densidade (utilidade/tamanho)
também falharia. Só a PD garante o ótimo global ao comparar incluir vs. pular em
cada estado.

---

## Exemplo 3: Caminho Mínimo na Fortaleza Infinita de Muzan

**Cenário.** Em Demon Slayer, a Fortaleza Infinita é um labirinto cujas salas se
ligam por passagens de mão única que nunca voltam (grafo acíclico). Um caçador de
demônios quer a rota mais rápida (em minutos) do `Portão` até o `Trono de Muzan`.

**Entrada.** Passagens `(origem → destino : minutos)`:

```
Portão → Corredor Suspenso (4),  Portão → Escada Invertida (2)
Corredor Suspenso → Câmara Central (5),  Corredor Suspenso → Salão dos Tatames (6)
Escada Invertida → Salão dos Tatames (3), Escada Invertida → Câmara Central (8)
Salão dos Tatames → Câmara Central (1),  Salão dos Tatames → Trono de Muzan (9)
Câmara Central → Trono de Muzan (3)
```

**Processamento.** Em ordem topológica, relaxamos as arestas:

| Sala | Custo mínimo desde o Portão | Veio de |
|------|----------------------------|---------|
| Portão | 0 | n/a |
| Escada Invertida | 2 | Portão |
| Corredor Suspenso | 4 | Portão |
| Salão dos Tatames | 5 | Escada Invertida |
| Câmara Central | 6 | Salão dos Tatames |
| Trono de Muzan | **9** | Câmara Central |

**Saída.** Rota ótima `Portão → Escada Invertida → Salão dos Tatames → Câmara
Central → Trono de Muzan`, **9 minutos**.

**Explicação.** Note que `Salão dos Tatames → Trono` direto custaria 5+9 = 14;
passar pela `Câmara Central` (5+1+3 = 9) é melhor. A ordem topológica garante que,
ao chegar ao `Trono`, todos os custos anteriores já são definitivos.

---

## Exemplo 4: Subsequência Comum Máxima (LCS) comparando times Pokémon

**Cenário.** Dois treinadores montam seus times de 6 Pokémon, cada um em uma
ordem. Queremos a maior "espinha dorsal" de Pokémon que ambos escalaram **na mesma
ordem relativa**, uma métrica de quanto as estratégias se parecem.

**Entrada.**

```
Time do Ash:  [Bulbasaur, Charmander, Squirtle, Pikachu, Snorlax, Gengar]
Time do Gary: [Charmander, Squirtle, Mewtwo, Pikachu, Gengar, Lugia]
```

**Processamento.** Matriz `L[i][j]` (linhas = time do Ash, colunas = time do
Gary). Quando os Pokémon coincidem, soma 1 à diagonal; senão, herda o máximo entre
cima e esquerda. A célula final `L[6][6] = 4`. A reconstrução, partindo do canto
inferior direito, recolhe as coincidências diagonais.

**Saída.** LCS = **[Charmander, Squirtle, Pikachu, Gengar]**, comprimento **4**.

**Explicação.** `Bulbasaur` e `Snorlax` só aparecem no time do Ash; `Mewtwo` e
`Lugia` só no do Gary; mas a ordem relativa Charmander→Squirtle→Pikachu→Gengar
sobreviveu em ambos. É o mesmo algoritmo que o `git diff` usa para alinhar linhas
de código.
