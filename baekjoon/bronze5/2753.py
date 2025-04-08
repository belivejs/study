_input = int(input())

if _input % 4 == 0 and (_input % 100 != 0 or _input % 400 == 0):
    print(1)
else:
    print(0)
