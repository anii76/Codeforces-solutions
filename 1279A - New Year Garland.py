#https://codeforces.com/contest/1279/problem/A

for _ in [0]*int(input()) :
 r,g,b = map(int,input().strip().split())
 p = [r,g,b];
 if  (sum(p)- max(p) == max(p)) or (sum(p)- max(p) >= max(p) - 1) :  
  print('Yes')
 else : print('No')