# https://codeforces.com/contest/237/problem/A

n = int(input())
lis  = []; i = 0; k = [0]
for x in range(n) :
 lis.append(input())
 if x!=0 and lis[x-1]==lis[x] :
  if lis[x] == rep : k[i] += 1
  else : k.append(1); i +=1 ; rep = lis[x]
 elif x == 0 : rep = lis[x]; 
print(max(k)+1)