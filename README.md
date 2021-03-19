# BOJ
### My Solution to [Baekjoon Online Judge](https://www.acmicpc.net/) Problems

## Platinum Level
- <img src="https://static.solved.ac/tier_small/16.svg" width="12">  [Largest Rectangle in a Histogram](https://www.acmicpc.net/problem/6549) - *[solution](https://github.com/okhee/BOJ/blob/main/Level_19_DivAndConq/9_6549.py)*
  - Divide and Conquer
  - Segment Tree
- <img src="https://static.solved.ac/tier_small/16.svg" width="12"> [공장](https://www.acmicpc.net/problem/6549) - *[solution](https://github.com/okhee/BOJ/blob/main/level_segment_tree/7578.py)*
  - Segment Tree

## Gold Level
- <img src="https://static.solved.ac/tier_small/15.svg" width="12"> [구간 곱 구하기](https://www.acmicpc.net/problem/11505) - *[solution](https://github.com/okhee/BOJ/blob/main/level_segment_tree/11505.py)*
  - Segment Tree
- <img src="https://static.solved.ac/tier_small/14.svg" width="12"> [가장 긴 증가하는 부분 수열 2](https://www.acmicpc.net/problem/12015) - *[solution](https://github.com/okhee/BOJ/blob/main/level_14_DP1/extra_12015.py)*
  - Binary Search Tree
- <img src="https://static.solved.ac/tier_small/14.svg" width="12"> [확장 게임](https://www.acmicpc.net/problem/16920) - *[solution](https://github.com/okhee/BOJ/blob/main/level_23_DFS_BFS/extra_16920.py)*
  - BFS
---
## [Python Standard Library](https://docs.python.org/ko/3/library/index.html)
### ```import collections``` - [*link*](https://docs.python.org/ko/3/library/collections.html)
- [collections.Counter](https://docs.python.org/ko/3/library/collections.html#collections.Counter)
  - Use this instead of dict for counting number of occurrence
### ```import itertools``` - [*link*](https://docs.python.org/ko/3/library/itertools.html)
- [itertools.product](https://docs.python.org/ko/3/library/itertools.html#itertools.product)
  - Cartesian product of **multiple** iterables
- [itertools.combinations](https://docs.python.org/ko/3/library/itertools.html#itertools.combinations)
### ```import bisect``` - [*link*](https://docs.python.org/ko/3/library/bisect.html)
- With given **sorted** list ```a``` and ```x = 4 ```   
[1, 2, 3, <span style="color:red">4</span>, 4, 4, <span style="color:green">5</span>, 6, ...]
- ```bisect.bisect_left(a, x) = ```<span style="color:red">3</span>
- ```bisect.bisect(a, x) = ``` <span style="color:green">6</span>
### ```import heapq``` - [*link*](https://docs.python.org/ko/3/library/heapq.html)
- `heapq.heappop(heap)`
- `heapq.heappush(heap)`
---
## Data Structures
### Trie - [*link*](https://ko.wikipedia.org/wiki/트라이_(컴퓨팅))
```python
class Node:
    def __init__(self, char):
        self.char = char
        self.child = {}
    
class Trie:
    def __init__(self):
        self.head = Node(None)
    
    def insert(self, word):
        cur = self.head
        for char in word:
            if char not in cur.child:
                cur.child[char] = Node(char)
            cur = cur.child[char]
        cur.child['*'] = None
    
    def search(self, word):
        cur = self.head

        for char in word:
            if char not in cur.child:
                return False
            cur = cur.child[char]
        if '*' in cur.child:
            return True
```
---
## Algorithms
### Graph, Tree Search Algorithm
- ### Dijkstra's Algorithm
```python
def dijkstra(V, initNode, adj)
  dist = [math.inf for _ in range(V+1)]
  dist[initNode] = 0
  prev = [None for _ in range(V+1)]
  heap = [(0, initNode)]

  # This heap contains duplicate only when
  # new route is efficient at one point but
  # turns out to be inefficient later.
  # This duplicate will be easily removed by 'continue'
  while heap:
    curDist, curNode = heapq.heappop(heap)

    # heap might contain meaningless case
    # where curNode is already handled elsewhere
    if dist[curNode] < curDist:
      continue

    # for all of its adjacent nodes,
    for nextDist, nextNode in adj[curNode]:
      nextDist = curDist + nextDist
      # if this new route is efficient, update
      if nextDist < dist[nextNode]:
        dist[nextNode] = nextDist
        heapq.heappush(heap, (nextDist, nextNode))
  return dist
```

- ### Floyd-Warshall Algorithm - O(|V|^3)
```python
import math
# dist = |V| × |V| array of minimum distances initialized to ∞ (infinity)
dist = [[math.inf for j in range(V)] for i in range(V)]

for v in range(V):
    dist[v][v] = 0

for each edge (u, v) do
    dist[u][v] = w(u, v)  // The weight of the edge (u, v)
  # dist[v][u] = w(u, v)  // if it is undirected

for k from 1 to |V|
    for i from 1 to |V|
        for j from 1 to |V|
            if dist[i][j] > dist[i][k] + dist[k][j] 
                dist[i][j] ← dist[i][k] + dist[k][j]
            end if
```
- ### Topological sort
```python
inward = [0 for _ in range(V+1)]
outward = [set() for _ in range(V+1)]

for each edge (u, v) do
    inward[v] += 1
    outward[u].add(v)

queue = []
for i in range(1, V+1):
    if inward[i] == 0:
        queue.append(i)

answer = []
while queue:
    curNode = queue.popleft()
    answer.append(curNode)
    for nextNode in outward[curNode]:
        inward[nextNode] -= 1
        if inward[nextNode] == 0:
            queue.append(nextNode)
```
- ### Prim's Algorithm
```python
# N nodes, 'edges' list given
for start, end, cost in edges:
    adj[start].add((end, cost))
    adj[end].add((start,cost))

visit = [False for _ in range(N)]
heap = [(0, 0)] # (edge cost to endNode, endNode)
totalCost = 0
# Must visit every node to terminate
while not all(visit):
    cost, curNode = heapq.heappop(heap)
    # Already visited, included
    if visit[curNode]:
        continue
    visit[curNode] = True
    totalCost += cost

    for nextNode, cost in adj[curNode]:
        # We want to choose edge (u, v)
        # Where u is visited and v is not visited
        if visit[nextNode]:
            continue
        heapq.heappush(heap, (cost, nextNode))
```
- ### Kruskal's Algorithm
```python
# global list
# Some kind of linked list that leads to ancestor
parents = [i for _ in range(V)]
def ancestor(node):
    global parents
    # if node has other parent
    if parents[node] != node:
        # Update with recent information
        parents[node] = ancestor(parents[node])
        return parents[node]
    else:
        return node

# adj, edges given
# edges.sort(key=lambda k: (cost of k))
edges = []
heapq.heappush(edges, (cost, start, end))

totalCost = 0
edgeCount = 0
while edges:
    cost, start, end = heapq.heappop(edge)
    # Same ancestor, this will make 'cycle'!
    if ancestor(start) == ancestor(end):
        continue

    # start's new ancestor will be merged into end
    parents[ancestor(start)] = end
    totalCost += cost
    edgeCount += 1

    if edgeCount == n-1:
        break
```

---
## Tips
* String sort 
```python
"".join(sorted(str))
```  
* Remove python **recursion** limit (Default: 1000)
```python
import sys
sys.setrecursionlimit(10**6)
```
* Faster I/O
> It may contain "\n" at end. Use ```rstrip()```
```python
import sys
input = sys.stdin.readline
```