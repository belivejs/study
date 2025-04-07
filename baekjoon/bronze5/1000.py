def sum(a, b):
    if a > 0 and b < 10:
        print(a + b)
    else:
        raise Exception('입력 조건을 만족하지 못했습니다.')

a, b = map(int, input().split(sep=' '))
sum(a, b)