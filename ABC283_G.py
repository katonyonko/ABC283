import io
import sys

_INPUT = """\
6
4 1 8
2 21 17 21
4 3 7
2 21 17 21
5 1 1
0 0 0 0 0
6 21 21
88 44 82 110 121 80
12 26 48
19629557415 14220078328 11340722069 30701452525 22333517481 720413777 11883028647 20926361028 24376768297 720413777 27999065315 13558621130
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N,L,R=map(int,input().split())
  A=list(map(int,input().split()))
  kitei=[]
  used=set() 
  for i in reversed(range(60)):
    find=0
    for j in range(N):
      if j in used: continue
      if find==0 and (A[j]>>i)&1==1:
        find=1
        kitei.append(A[j])
        used.add(j)
      elif find==1 and (A[j]>>i)&1==1:
        A[j]^=kitei[-1]
  kitei=kitei[::-1]
  for i in range(len(kitei)):
    for j in range(i+1,len(kitei)):
      if kitei[i]^kitei[j]<kitei[j]:
        kitei[j]^=kitei[i]
  ans=[]
  for i in range(L-1,R):
    tmp=0
    for j in range(len(kitei)):
      if (i>>j)&1==1:
        tmp^=kitei[j]
    ans.append(tmp)
  print(*ans)