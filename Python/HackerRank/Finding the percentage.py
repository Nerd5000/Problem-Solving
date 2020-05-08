if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    data=student_marks[query_name]
    percentage=str(float((data[0]+data[1]+data[2])/3))
    # print(percentage+'0')
    print('{0:.2f}'.format((data[0]+data[1]+data[2])/3))
    
