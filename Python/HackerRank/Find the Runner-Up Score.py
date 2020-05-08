
def runnerUp(arr):
    maxNum=-1000
    runnerUpVal=-1000
    for i in arr:
        if maxNum < i:
            maxNum=i
    for i in arr:
        if i < maxNum and i>runnerUpVal:
            runnerUpVal=i
    
    return runnerUpVal



if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    print(runnerUp(list(arr)))