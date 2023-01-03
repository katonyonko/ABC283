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

  class SegTree:
    X_unit = 10**6
    X_f = min

    def __init__(self, N):
      self.N = N
      self.X = [self.X_unit] * (N + N)

    def build(self, seq):
      for i, x in enumerate(seq, self.N):
        self.X[i] = x
      for i in range(self.N - 1, 0, -1):
        self.X[i] = self.X_f(self.X[i << 1], self.X[i << 1 | 1])

    def set_val(self, i, x):
      i += self.N
      self.X[i] = x
      while i > 1:
        i >>= 1
        self.X[i] = self.X_f(self.X[i << 1], self.X[i << 1 | 1])

    def fold(self, L, R):
      L += self.N
      R += self.N
      vL = self.X_unit
      vR = self.X_unit
      while L < R:
        if L & 1:
          vL = self.X_f(vL, self.X[L])
          L += 1
        if R & 1:
          R -= 1
          vR = self.X_f(self.X[R], vR)
        L >>= 1
        R >>= 1
      return self.X_f(vL, vR)

  N=int(input())
  P=list(map(lambda x: int(x)-1,input().split()))
  ans=[10**6]*N

  tmp=sorted([(P[i],i) for i in range(N)], reverse=True)
  st=SegTree(N)
  for i in range(N):
    y,x=tmp[i]
    st.set_val(x,x+y)
    ans[x]=min(ans[x],st.fold(x+1,N)-x-y)

  st=SegTree(N)
  for i in range(N):
    y,x=tmp[i]
    st.set_val(x,-x+y)
    ans[x]=min(ans[x],st.fold(0,x)+x-y)

  tmp=sorted([(P[i],i) for i in range(N)])
  st=SegTree(N)
  for i in range(N):
    y,x=tmp[i]
    st.set_val(x,-x-y)
    ans[x]=min(ans[x],st.fold(0,x)+x+y)

  st=SegTree(N)
  for i in range(N):
    y,x=tmp[i]
    st.set_val(x,x-y)
    ans[x]=min(ans[x],st.fold(x+1,N)-x+y)

  print(*ans)