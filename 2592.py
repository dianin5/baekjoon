N = [int(input()) for _ in range(10)]
print(sum(N)//len(N))
print(max(N, key=N.count))