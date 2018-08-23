k, n = map(int, input().split())
if k == 0:
    quit()

arr = []
for i in range(k):
    arr.append(0)

def combs(start):
    global token
    for i in range(start, n):
        arr[token - 1] = i
        if token == k:
            print (*arr, sep=' ')
        else:
            token += 1
            combs(i + 1)
    token -= 1

token = 1
combs(0)
