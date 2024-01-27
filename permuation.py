def permuation(n):
    if n == 1:
        return [[1]]
    else:
        result = []
        for i in range(1, n+1):
            for j in permuation(n-1):
                result.append([i] + j)
        return result
p=permuation(int(input()))
for itr in p:
  print(*itr)
