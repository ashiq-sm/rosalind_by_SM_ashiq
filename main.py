# i = input()[::-1]
# print("OUTPUT:")
# d = {"A": "T", "T": "A", "G": "C", "C": "G"}
# for j in i:
#   print(d[j], end="")
a = input()
b = input()
def hammingDistance(a, b):
    count = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            count += 1
    return count
print(hammingDistance(a, b))
