# https://codeforces.com/contest/894/problem/A

inP = input().upper()
inP = ''.join([i for i in inP if i == 'Q' or i =='A'])
#print(inP)
 
sum = 0
for i in range(len(inP)):
  if inP[i] == 'Q' :
   for j in range(i+1,len(inP)):
    if inP[j] == 'A':
     sum += inP[j+1:len(inP)].count('Q')
 
print(sum)