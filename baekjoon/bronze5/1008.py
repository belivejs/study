def div(a,b):
    if a>0 and b<10:
        print(a/b)
    else:
        raise Exception('입력 값의 조건이 틀렸습니다.')

a, b = map(int,input().split(sep=' '))
div(a,b)