from sys import stdin

n = int(stdin.readline())

for i in range(1, n + 1):
    x = i
    if x % 3 == 0 or x % 10 == 3:
        print('', i, end='')
        continue

    x //= 10
    while x != 0:
        if x % 10 == 3:
            print('', i, end='')
            break

        x //= 10
print()