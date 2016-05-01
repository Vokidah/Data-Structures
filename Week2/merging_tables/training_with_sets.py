def MakeSet(i, parent):
    parent[i] = i

def Find(i, parent):
    while i != parent[i]:
        i = parent[i]
    return i

def Merge(i, j, parent, rank):
    i_id, j_id = Find(i, parent), Find(j, parent)
    if i_id == j_id:
        return
    if rank[i_id] > rank[j_id]:
        parent[j_id] = i_id
        rank[i_id] += rank[j_id]
    else:
        parent[i_id] = j_id
        rank[j_id] += rank[i_id]



n, m = map(int, input().split())
rank = list(map(int, input().split()))
array = [i for i in range(0, n)]
for i in range(0, n):
    MakeSet(i, array)
for _ in range(m):
    i, j = map(int, input().split())
    print(array)
    Merge(i - 1, j - 1, array, rank)
    #print(i, j)
    print(rank[Find(j, parent=array)])
    #print(rank)