#linear search algorithm

# def linearSearch(arry: list, search_num: int,  length: int)->int:
#     if length == -1:
#         return "Not Found"
#     elif search_num == arry[length]:
#         return length
#     else: 
#         return linearSearch(arry, search_num, length-1)

    
def linearSearch(arry: list, searchNum: int)->int:
    for x in range(len(arry)):
        if searchNum == arry[x]:
            return x
    else: 
        return -1

if __name__ == '__main__':
    print(linearSearch([2,3,1,4,10], 10))
        
