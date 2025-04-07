A = int(input())
B = int(input())

if 0 < A and B < 10:
    print(A+B)
else:
    raise Exception('입력값 조건 미충족')