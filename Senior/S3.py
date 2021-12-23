import sys
# sys.setrecursionlimit(1000000)
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
fill = lambda x: list(range(0, x + 1))
flat = lambda x, l: x.join(map(str, l))
mat, mit, MOD = sys.maxsize, -sys.maxsize, int(1e9 + 7)


def sieve(n):
    prime[1] = 1
    prime[0] = 1
    i = 2
    while pow(i, 2) < n + 1:
        if not prime[i]:
            for j in range(pow(i, 2), n + 1, i):
                prime[j] = 1
        i += 1
    r = 0
    for i in range(1, n + 1):
        if not prime[i]:
            r += i
        dp[i] = r


prime = emp(0, 200001)
dp = emp(0, 200001)
sieve(200000)
for i in range(readint()):
    a, b, = gi()
    printf(dp[b] - dp[a - 1])
