import io
import sys

_INPUT = """\
6
((a)ba)
(a(ba))
(((())))
abca
()(a)
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  S=input()
  ans='Yes'
  box=set()
  tmp=[[]]
  for i in range(len(S)):
    if S[i]=='(':
      tmp.append([])
    elif S[i]==')':
      tmp2=tmp.pop()
      for j in tmp2:
        if j in box: box.remove(j)
    else:
      if S[i] in box: ans='No'
      else: tmp[-1].append(S[i]); box.add(S[i])
  print(ans)  