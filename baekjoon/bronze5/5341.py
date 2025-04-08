while True:
    n = int(input())

    if n == 0:
        break
    
    print(sum(range(n, 0, -1)))

"""
1. 아래와 같이 수학적으로 접근할 수도 있다.
while True:
  n=int(input())
  if n==0:
    break
  print((n*(n+1))//2)
"""