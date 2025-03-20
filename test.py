
f = open('test.txt', 'w')
for i in range(10):
    f.write(f'{i}번째 줄입니다.\n')
f.close()