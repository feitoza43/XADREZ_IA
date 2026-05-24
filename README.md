# ♟️ Xadrez

Jogo de xadrez em Python com pygame-ce e IA Minimax.

## Tecnologias

- Python 3.14+
- pygame-ce
- Minimax + Alpha-Beta Pruning

## Instalação

```bash
pip install pygame-ce
python main.py
```

## Como jogar

- Você joga com as **peças brancas**
- A **IA** controla as pretas automaticamente
- **Clique** na peça para selecionar
- **Clique** no destino para mover
- Casas em **amarelo** = peça selecionada
- Casas em **verde** = movimentos válidos

## Estrutura

```
xadrez/
├── main.py          # entrada do jogo
├── src/
│   ├── board.py     # tabuleiro e estado
│   ├── pieces.py    # lógica das peças
│   ├── game.py      # loop e eventos
│   ├── renderer.py  # interface pygame
│   └── ai.py        # IA Minimax + Alpha-Beta
└── README.md
```

## Roadmap

- [x] Movimentos básicos
- [x] Interface gráfica pygame
- [x] IA Minimax + Alpha-Beta (depth=2)
- [ ] Xeque e xeque-mate
- [ ] Roque
- [ ] En passant
- [ ] Promoção do peão
- [ ] IA com tabela de aberturas