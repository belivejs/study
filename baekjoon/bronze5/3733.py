while True:
    try:
        N, stock = map(int, input().split(sep=' '))
        print(stock // (N + 1))
    except:
        break

"""
1. 영어로 된 알고리즘 문제라 해석이 어려웠음
"""