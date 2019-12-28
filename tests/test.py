n = input()

i = 0
for _ in n:
    print(n[:-i])
    i += 1

a = ""
for _ in n:
    a += _
    print(a)

n = int(input())
arr = list(map(str, input().rstrip().split()))
print(" ".join(arr[::-1]))