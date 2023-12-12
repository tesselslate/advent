import functools, math, re, string, sys, itertools, ul
from dataclasses import dataclass
from collections import Counter, defaultdict, deque

if len(sys.argv) > 1:
    F = open(sys.argv[1])
else:
    F = sys.stdin.readlines()

F = [l.strip() for l in F]
while F[-1] == "":
    del F[-1]
G = ul.grid(F)

RR = {r for r in range(len(G)) if G[r].count(".") == len(G[r])}
CC = {c for c in range(len(G)) if set(G[r][c] for r in range(len(G))) == {"."}}

galaxies = [(r,c) for (r,c) in ul.gridpoints(G) if G[r][c] == "#"]

def find(mult):
    S = 0
    for (a, b) in itertools.product(galaxies, repeat=2):
        er = len(set(range(*ul.minmax(a[0], b[0]))) & RR)
        ec = len(set(range(*ul.minmax(a[1], b[1]))) & CC)
        S += abs(a[0]-b[0]) + abs(a[1]-b[1]) + (er + ec) * (mult - 1)
    return S // 2
print(find(2))
print(find(1000000))
