n = int(input())
times = list(map(int, input().split()))
times.sort()

total = 0 
prefix = 0

for t in times:
    prefix += t
    total += prefix

print(total)