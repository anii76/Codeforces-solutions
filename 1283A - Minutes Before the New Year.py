# https://codeforces.com/contest/1283/problem/A

for _ in[0]*int(input()):
  h , m = map(int, input().split())
  print((23-h)*60+(59-m)+1)
