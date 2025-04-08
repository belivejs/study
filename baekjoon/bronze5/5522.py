sum = 0
for _ in range(5):
    n = int(input())
    if 0 <= n and n <= 100:
      sum += n
    else:
       raise Exception('입력값의 범위를 확인하세요.')
print(sum)

"""
1. 표준 입력으로부터 여러 줄의 입력을 한꺼번에 읽고, 문자열들의 리스트로 반환
import sys
inputs = sys.stdin.readlines()
print(sum(map(int,inputs)))
"""