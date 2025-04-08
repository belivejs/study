while True:
    try:
        n1, n2 = map(int, input().split(sep=' '))
        if n1 <= 1_000_000 and n2 <= 1_000_000:
            if n1 == 0 and n2 == 0:
                break
            elif n1 > n2:
                print('Yes')
            else:
                print('No')
        else:
            raise Exception('입력값 범위 초과')
    except EOFError:
        break