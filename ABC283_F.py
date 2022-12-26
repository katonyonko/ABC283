import io
import sys

_INPUT = """\
6
4
3 2 4 1
7
1 2 3 4 5 6 7
16
12 10 7 14 8 3 11 13 2 5 6 16 4 1 15 9
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  