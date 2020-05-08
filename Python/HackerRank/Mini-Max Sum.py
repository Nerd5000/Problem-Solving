#!/bin/python3

import math
import os
import random
import re
import sys

#Order the array first
def orderedArray(arr):
    swapElement=0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i]>arr[j]:
                swapElement=arr[i]
                arr[i]=arr[j]
                arr[j]=swapElement
    return arr
                
    return 
# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    ar=orderedArray(arr)
    min=0
    max=0
    for i in range(len(ar)-1):
        max+=ar[i]
    for i in range(1,len(ar)):
        min+=ar[i]
    print(min,max,sep=" ")

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
