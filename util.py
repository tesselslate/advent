import sys
sys.setrecursionlimit(1000000)

def grid(size, fill=None):
    """Returns a square grid with the given size and fill element."""
    return [[fill]*size for _ in range(size)]

def grid3d(size, fill=None):
    """Returns a 3D grid with the given size and fill element."""
    return [grid(size, fill) for _ in range(size)]

def irange(start, stop, step=1):
    """Returns a range including the stop index."""
    return range(start, stop + 1, step)

def halves(x):
    """Returns the two halves of x."""
    l = len(x) // 2
    return x[:l], x[l:]

def manhattan(a, b, x, y):
    """Returns the manhattan distance between (a, b) and (x, y)."""
    return abs(a-x) + abs(b-y)

def max_countdict(d):
    """Returns the maximum (k, v) pair in a dictionary of Counters."""
    return max_dict(d, lambda n : sum([v for _, v in n.items()]))

def max_dict(d, val=lambda n:n):
    """Returns the maximum (k, v) pair in a dictionary."""
    M = (None, 0)
    for k, v in d.items():
        a = val(v)
        if a > M[1]:
            M = (k, a)
    return M

def print_grid(grid):
    """Pretty prints the given grid."""
    for y in grid:
        s = ""
        for x in y:
            s += str(x)[0]
        print(s)

def scan(fmt, inp):
    """
    Basic sscanf copycat for quick input parsing.

    %d - Base 10 number
    %f - Float
    %s - String
    %x - Base 16 (hex) number
    """
    out = []
    idx = 0
    fmt_idx = 0
    while fmt_idx < len(fmt):
        fc = fmt[fmt_idx]

        # process non-format characters
        if fc != '%':
            if inp[idx] != fc:
                raise ValueError(f"mismatch at {idx} ({inp}): expected {fc}, got {inp[idx]}")
            fmt_idx += 1
            idx += 1
            continue

        # read text for this capture
        typ = fmt[fmt_idx + 1]
        content = ""
        if fmt_idx + 2 == len(fmt):
            fmt_idx = len(fmt)
            content = inp[idx:]
        else:
            delim = fmt[fmt_idx + 2]
            while inp[idx] != delim:
                content += inp[idx]
                idx += 1
        fmt_idx += 2

        # convert capture and continue
        if typ == 'd':
            out.append(int(content))
        if typ == 'f':
            out.append(float(content))
        if typ == 's':
            out.append(content)
        if typ == 'x':
            out.append(int(content, 16))
    return out

if __name__ == "__main__":
    print("testing scan")
    assert scan("123", "123") == []
    assert scan("123 %d", "123 456") == [456]
    assert scan("123,%d %d,abc", "123,23 45,abc") == [23, 45]
    assert scan("H%f-%f", "H0.12-3.45") == [0.12, 3.45]
    assert scan("Hello %s!", "Hello test!") == ["test"]
    assert scan("%s-%d-%x-%f %s %s", "Hi-23-45BFAD-0.15 Hello Hello2") == ["Hi", 23, 0x45BFAD, 0.15, "Hello", "Hello2"]
