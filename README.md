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
---
## Tips
* ```"".join(sorted(str))``` - String sort  
