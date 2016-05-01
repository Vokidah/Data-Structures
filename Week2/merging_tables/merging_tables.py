# python3

import sys

n, m = map(int, sys.stdin.readline().split())
lines = list(map(int, sys.stdin.readline().split()))
rank = [1] * n
parent = list(range(0, n))
ans = max(lines)

def getParent(table):
    # find parent and compress path
    if table != parent[table]:
        parent[table] = getParent(parent[table])
    return parent[table]


def merge(destination, source):
    realDestination, realSource = getParent(destination), getParent(source)
    if realDestination == realSource:
        return -1
    if rank[realDestination] > rank[realSource]:
        lines[realDestination] += lines[realSource]
        lines[realSource] = 0
        parent[realSource] = realDestination
    else:
        lines[realSource] += lines[realDestination]
        lines[realDestination] = 0
        parent[realDestination] = realSource
        if rank[realDestination] == rank[realSource]:
            rank[realSource] += 1
    return max(lines[realDestination], lines[realSource])

for i in range(m):
    destination, source = map(int, sys.stdin.readline().split())
    answer = merge(destination - 1, source - 1)
    if answer > ans:
        ans = answer
    print(ans)
