# tiny-chess-01

A chess engine in 4 KB of Python, built for the make.fun tiny-chess-01 bounty.

`main.py` (3,832 bytes) is self-contained: 0x88 board, negamax with
alpha-beta, iterative deepening to a fixed 60,000-node budget, quiescence
search, transposition table, killer moves, and material + piece-square
evaluation. It speaks the make.fun trial HTTP protocol (`$MAKEFUN_ENV_URL`).

Local practice trial-0: 1 win, 3 draws, 2 losses (~1191 Elo vs the anchors).
