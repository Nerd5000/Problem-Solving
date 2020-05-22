# built in function is faster it takes 1 time
# user made function takes n times


# built in function
# def split_and_join(line):
#     res = line.split(' ')
#     res = '-'.join(res)
    
#     return res

# user made function
def split_and_join(line):
    res=''
    for i in range(len(line)):
        if line[i]==' ':
            res+='-'
        else:
            res+=line[i]

    return res


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)