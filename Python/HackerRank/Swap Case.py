# using the built in function
def swap_case(s):
    res=s.swapcase()
    return res


# self made swap_case function
# the built in faster it takes 1 time 
# the self made takes n times
# def swap_case(s):
#     res=''
#     for i in s:
#         if i.lower()==i:
#             res+=i.upper()
#         else:
#             res+=i.lower()
    
#     return res

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)