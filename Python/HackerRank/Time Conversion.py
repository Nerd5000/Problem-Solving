#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    timeArray=s.split(':')
    timeString=""
    if timeArray[2][2]=='P':
        if timeArray[0][0]=='1' and timeArray[0][1]=='2':
            timeArray[2]=timeArray[2].replace('PM','')
        else:    
            timeArray[0]=str(int(timeArray[0])+12)
            timeArray[2]=timeArray[2].replace('PM','')    
    elif timeArray[2][2]=='A':
        if timeArray[0][0]=='1' and timeArray[0][1]=='2':
            timeArray[0]='00'
        timeArray[2]=timeArray[2].replace('AM','')

    for i in range(len(timeArray)):
        if i != 2:
            timeString+=timeArray[i]+':'
        else:
            timeString+=timeArray[i]
    return timeString


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
