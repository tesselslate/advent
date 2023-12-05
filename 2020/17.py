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

G = set()
_G = ul.grid(F)
for x, y in ul.gridpoints(_G):
    if _G[x][y] == "#":
        G.add((x,y,0,0))

def adjc(a,b,c,d):
    s = 0
    for p in ul.ndadj_all(4):
        x,y,z,w = p
        if (x+a,y+b,z+c,w+d) in G: s += 1
    return s

for _ in range(6):
    overlay = []

    V = set()
    for p in G:
        x,y,z,w = p
        adj = [(0,0,0,0)] + list(ul.ndadj_all(4))
        adj = [(x+p[0],y+p[1],z+p[2],w+p[3]) for p in adj]

        for p in adj:
            if p in V:
                continue
            V.add(p)
            x,y,z,w = p
            s = adjc(x,y,z,w)
            if p in G:
                if s != 2 and s != 3:
                    overlay.append((p,False))
            else:
                if s == 3:
                    overlay.append((p, True))

    for p in overlay:
        x,y,z,w = p[0]
        if p[1]:
            G.add(p[0])
        else:
            G.remove(p[0])
print(len(G))
