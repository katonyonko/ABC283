import io
import sys

_INPUT = """\
6
4 3
5 5
8 1
9 9
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  A,B=map(int,input().split())
  print(A**B)