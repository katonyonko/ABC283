import io
import sys

_INPUT = """\
6
3 3
1 1 0
1 0 1
1 0 0
4 4
1 0 0 0
0 1 1 1
0 0 1 0
1 1 0 1
2 3
0 1 0
0 1 1
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  #必要な変数、関数の定義
  H,W=map(int,input().split())
  A=[list(map(int,input().split())) for _ in range(H)]
  dp=[10**6]*(H-1)*4
  def idx(i,j,k): return i*4+j*2+k
  def judge1(A,B,T):
    res=True
    for i in range(len(A)):
      if T[i]==1:
        tmp=False
        for j in [i-1,i+1]:
          if 0<=j<len(A) and A[i]==A[j]: tmp=True
        if A[i]==B[i]: tmp=True
        if tmp==False: res=False
    return res
  def judge2(A,B):
    res=[]
    for i in range(len(A)):
      tmp=1
      for j in [i-1,i+1]:
        if 0<=j<len(A) and B[i]==B[j]: tmp=0
      if A[i]==B[i]: tmp=0
      res.append(tmp)
    return res
  def rev(A): return [A[i]^1 for i in range(len(A))]

  #初期化
  if judge1(A[0],A[1],[1]*W)==True: dp[idx(0,0,0)]=0
  if judge1(A[0],rev(A[1]),[1]*W)==True: dp[idx(0,0,1)]=1
  if judge1(rev(A[0]),A[1],[1]*W)==True: dp[idx(0,1,0)]=1
  if judge1(rev(A[0]),rev(A[1]),[1]*W)==True: dp[idx(0,1,1)]=2

  #dp
  for i in range(H-2):
    if judge1(A[i+1],A[i+2],judge2(A[i],A[i+1]))==True: dp[idx(i+1,0,0)]=min(dp[idx(i+1,0,0)],dp[idx(i,0,0)])
    if judge1(A[i+1],A[i+2],judge2(rev(A[i]),A[i+1]))==True: dp[idx(i+1,0,0)]=min(dp[idx(i+1,0,0)],dp[idx(i,1,0)])
    if judge1(A[i+1],rev(A[i+2]),judge2(A[i],A[i+1]))==True: dp[idx(i+1,0,1)]=min(dp[idx(i+1,0,1)],dp[idx(i,0,0)]+1)
    if judge1(A[i+1],rev(A[i+2]),judge2(rev(A[i]),A[i+1]))==True: dp[idx(i+1,0,1)]=min(dp[idx(i+1,0,1)],dp[idx(i,1,0)]+1)
    if judge1(rev(A[i+1]),A[i+2],judge2(A[i],rev(A[i+1])))==True: dp[idx(i+1,1,0)]=min(dp[idx(i+1,1,0)],dp[idx(i,0,1)])
    if judge1(rev(A[i+1]),A[i+2],judge2(rev(A[i]),rev(A[i+1])))==True: dp[idx(i+1,1,0)]=min(dp[idx(i+1,1,0)],dp[idx(i,1,1)])
    if judge1(rev(A[i]),rev(A[i+1]),judge2(A[i],rev(A[i+1])))==True: dp[idx(i+1,1,1)]=min(dp[idx(i+1,1,1)],dp[idx(i,0,1)]+1)
    if judge1(rev(A[i]),rev(A[i+1]),judge2(rev(A[i]),rev(A[i+1])))==True: dp[idx(i+1,1,1)]=min(dp[idx(i+1,1,1)],dp[idx(i,1,1)]+1)
  ans=10**6
  if sum(judge2(A[-2],A[-1]))==0: ans=min(ans,dp[-4])
  if sum(judge2(A[-2],rev(A[-1])))==0: ans=min(ans,dp[-3])
  if sum(judge2(rev(A[-2]),A[-1]))==0: ans=min(ans,dp[-2])
  if sum(judge2(rev(A[-2]),rev(A[-1])))==0: ans=min(ans,dp[-1])
  if ans==10**6: print(-1)
  else: print(ans)