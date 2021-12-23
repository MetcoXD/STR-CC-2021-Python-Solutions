import sys
sys.setrecursionlimit(1000000)
readline = lambda: sys.stdin.readline().strip()
readint = lambda: int(sys.stdin.readline())
all_data = lambda: sys.stdin.read().split('\n')
printf = lambda x: sys.stdout.write("%d\n" % x)
prints = lambda x: sys.stdout.write(x)
printline = lambda x: list(map(print, x))
printeach = lambda x, y="": print(*x, sep=y)
gi = lambda: list(map(int, readline().split()))
gs = lambda: readline().strip().split()
emp = lambda x, y: [x] * y
fill = lambda x: list(range(1, x + 1))
flat = lambda x, l: x.join(map(str, l))
mat, mit, MOD = sys.maxsize, -sys.maxsize, int(1e9 + 7)
a, b, c = map(int, input().split())
if a * a + b * b == c * c:
    prints("True")
else:
    prints("False")
