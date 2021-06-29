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
- [collections.defaultdict](https://docs.python.org/ko/3/library/collections.html#collections.defaultdict)
```python
# d = {'a':[], 'b':[1, 2]}
d = collections.defaultdict(list)
# d = {'a':0, 'b':1}
d = collections.defaultdict(int)
```
### ```import itertools``` - [*link*](https://docs.python.org/ko/3/library/itertools.html)
- [itertools.product](https://docs.python.org/ko/3/library/itertools.html#itertools.product)
  - Cartesian product of **multiple** iterables
- [itertools.combinations](https://docs.python.org/ko/3/library/itertools.html#itertools.combinations)
```python
for c in itertools.combinations(range(5), 3):
    # type(c) - <class 'tuple'>
    # c - (0, 1, 2), (0, 1, 3), ...
```
### ```import bisect``` - [*link*](https://docs.python.org/ko/3/library/bisect.html)
- `bisect` basically points to leftmost index of `greater or equal` value compared to query number.
- With given **sorted** list `a` and `x = 4 `   
[1, 2, 3, <span style="color:red">4</span>, 4, 4, <span style="color:green">5</span>, 6, ...]
- `bisect.bisect_left(a, x)` = 3
  - points to leftmost index of `equal (if exist) or greater` value
- `bisect.bisect(a, x)` = 6
  - points to leftmost index of `greater` value
- bisect source code
    ```python
    def bisect_left(a, x):
        # [lo, hi)
        lo = 0       # lo:  inclusive
        hi = len(a)  # hi: *exclusive*
        
        while lo < hi:
            mid = (lo + hi) // 2

            # <= for bisect_right
            if a[mid] < x:
                lo = mid + 1
            else:
                hi = mid
            # add 'a[mid] == x:' for search

        return lo
    ```

- `Binary Search` using `bisect`
    - Finding first occurence of `num`
    ```python
    def BinarySearch(array, num):
        idx = bisect.bisect_left(array, num)
        # idx == len(array) means every element is smaller than num
        if idx != len(array) and array[idx] == num:
            return idx
        # num not found
        else:
            return -1
    ```
    - Finding greatest value smaller than `num`
    ```python
    def BinarySearch(array, num):
        idx = bisect.bisect_left(array, num)
        if idx > 0:
            return array[idx - 1]
        else:
            return None
    ```
### ```import heapq``` - [*link*](https://docs.python.org/ko/3/library/heapq.html)
- `heapq.heappop(heap)`
- `heapq.heappush(heap)`
### ```set``` - [*link*](https://wikidocs.net/16044)
- No duplicated values
- Iterable, but not ordered
- `s.add(elem)`
- `s.remove(elem)`
    - if elem does not exist, raise KeyError
    - `s.discard(elem)` won't raise error
- `a.union(b)`, `a.intersection(b)`, `a.difference(b)`
- `a.issubset(b)`, `a.issuperset(b)`, `a.isdisjoint(b)`
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
- ### Breadth First Search (BFS)
```python
import collections

adj = [set() for _ in range(node_num)]
for s, e in edges:
    adj[s].add(e)
    # if graph is undirected graph,
    # adj[e].add(s)

# You can use value of visit array as 0, 1, 2,
# which represents (weighted) length between certain node and start node
visit = [False for _ in range(node_num)]
auxilary_arr = [0 for _ in range(node_num)]

bfs_queue = collections.deque()
bfs_queue.append(start_node)
visit[start_node] = True
auxilary_arr[start_node] = init

# while not all(visit):
while bfs_queue:
    cur_node = bfs_queue.popleft()

    for next_node in adj[cur_node]:
    # any invalid state, already visited case will be skipped here
        # if it is about 2d grid,
        # if i or j in out of bound,
        #   continue
        if visit[next_node]:
            continue

        bfs_queue.append(next_node)
        visit[next_node] = True
        auxilary_arr[next_node] = some_val[cur_node] + foo
return auxilary_arr[end_node]
```

- ### Depth First Search (DFS)
You can either replace `queue` to `stack` of BFS or use recursive algorithm.
Recursive method can be considered as sort of `backtracking` or `dynamic programming`
```python
def distributeCoins(self, root: TreeNode) -> int:
    answer = 0
    
    # recursive function
    def dfs(node):
        nonlocal answer
        
        # leaf node
        if not node:
            return 0
        
        # retrieve sub-information
        l = dfs(node.left)
        r = dfs(node.right)
        
        # calculate for current node
        answer += abs(l) + abs(r)

        # return sub-information            
        return l + r + node.val - 1
    
    # Top-down
    dfs(root)
    return answer
```
If hierarchical structure of given tree is unsure, such as only adjacency relationship is given, specify `parent` in dfs function <br>
Plus, location of subsequent `dfs()` call determines whether this is `pre-fix`, `in-fix`, `post-fix`. Keep in mind!
``` python
def dfs(node, parent=None):
    for child in adj[node]:
        # ignore adjacent parent to ensure topological order
        if child != parent:
            child_stat = dfs(child, node)
            sub_stat[0] = child_stat[0] + 1
            sub_stat[1] = child_stat[0] + child_stat[1]
    stat[node] = sub_stat
    return sub_stat
```

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