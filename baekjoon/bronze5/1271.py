n, m = map(int, input().split(sep=' '))
div, mod = divmod(n, m)

print(div)
print(mod)

"""
언패킹 연산자(*)를 사용하는 방법도 있다.
print(*divmod(*map(int,input().split())))
"""