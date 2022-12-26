import io
import sys

_INPUT = """\
6
40004
1355506027
10888869450418352160768000001
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  S=input()
  ans=0
  now=0
  while now<len(S):
    if now<len(S)-1 and int(S[now])==0 and int(S[now+1])==0: now+=2
    else: now+=1
    ans+=1
  print(ans)