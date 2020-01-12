# https://codeforces.com/contest/1283/problem/B

t = int(input())
for i in range(t):
    n , k = map(int , input().split())
    if (n % k) > (k//2) :
        r = k//2
    else :
        r = n % k
    print((n//k)*k + r)
      