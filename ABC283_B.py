import io
import sys

_INPUT = """\
6
3
1 3 5
7
2 2
2 3
1 3 0
2 3
1 2 8
2 2
2 1
5
22 2 16 7 30
10
1 4 0
1 5 0
2 2
2 3
2 4
2 5
1 4 100
1 5 100
2 3
2 4
7
478 369 466 343 541 42 165
20
2 1
1 7 729
1 6 61
1 6 838
1 3 319
1 4 317
2 4
1 1 673
1 3 176
1 5 250
1 1 468
2 6
1 7 478
1 5 595
2 6
1 6 599
1 6 505
2 3
2 5
2 1
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N=int(input())
  A=list(map(int,input().split()))
  Q=int(input())
  for _ in range(Q):
    query=input().split()
    if query[0]=='1': A[int(query[1])-1]=int(query[2])
    else: print(A[int(query[1])-1])