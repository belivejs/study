N = int(input())

if 1 <= N and N <= 9:
    for i in range(1, 10):
        print(f'{N} * {i} = {N*i}')
else:
    raise Exception('입력값 조건 미충족')