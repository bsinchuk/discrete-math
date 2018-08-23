n, k = map(int, input().split())
if k == 0:
    quit()

arr = []
for i in range(k):
    arr.append(0)

def permutations():
    global token
    for i in range(0, n):
        arr[token - 1] = i
        if token == k:
            if len(arr) == len(set(arr)):
                print (*arr, sep=' ')
        else:
            token += 1
            permutations()
    token -= 1

token = 1
permutations()
