#https://codeforces.com/contest/1301/problem/A

for _ in [0]*int(input()) : 
 a = input(); b = input() ; c = input()
 u = [ c[i] for i in range(len(c)) if b[i] != c[i] and a[i] != c[i] ] 
 if u != [] :  print('NO')
 else : print('YES')