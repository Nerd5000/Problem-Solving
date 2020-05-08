#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    spaces=n-1
    hashes=1
    for i in range(n):
        print(spaces*" "+hashes*"#")
        spaces-=1
        hashes+=1

if __name__ == '__main__':
    n = int(input())

    staircase(n)
