_input = input().split(sep=' ')
sum = 0
for i in _input:
    sum += int(i)**2
print(sum%10)

"""
1. sum 내장 함수를 사용해도 된다.
2. list comprehesions을 사용해도 된다.
print(sum(i*i for i in map(int, input().split()))%10)
"""