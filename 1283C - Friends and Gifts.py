# https://codeforces.com/contest/1283/problem/C

n = int(input()); i = 0
f = list(map(int,input().strip().split()))[:n]
d = { x+1 for x in range(len(f)) if f[x] in f}
d_ = list(d)
c = [x+1 for x in range(len(f)) if f[x] == 0 ] #givers
h = list(d.difference(set(f))) #takers
for x in range(len(c)) :
  f[c[x]-1] = h[x]
for x in range(n):
 if d_[x]==f[x] :
  if f[c[i]-1] != f[x] : 
   s = f[c[i]-1]
   f[c[i]-1] =f[x]
   f[x] = s   
  else : 
   if i ==len(c) : i =0
   else :  i +=1
   s = f[c[i]-1]
   f[c[i]-1] =f[x]
   f[x] = s   
print(*f)
  
