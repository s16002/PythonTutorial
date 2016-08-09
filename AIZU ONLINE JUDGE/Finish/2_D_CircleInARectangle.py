W, H, x, y, r = [int(i) for i in input().split()]

if x + r <= W and y - r >= 0 and x - r >= 0 and y + r <= H:
    print("Yes")
else:
    print("No")