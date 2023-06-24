# #binarySearch with sorted arry
# from time import sleep
# #with recursion
# def binarySearch(arry: list, first: int, last:int, search:int = 100)->int:
#     middle = (first+last)//2
#     if middle <= len(arry):
#         if first <= last:
#             if search == arry[middle]:
#                 return middle
#             elif search > arry[middle]:
#                 print("Great")
#                 sleep(1)
#                 return binarySearch(arry, middle+1, last)
#             else:
#                 return binarySearch(arry, first, middle-1)
#         else:
#             return -1

# if __name__ == "__main__":
#     arry = [2, 6, 10, 11, 12, 90]
#     first = 0
#     last = 6
#     print(binarySearch(arry, first, last))
from time import sleep
original = [x for x in range(8)]
def binarySearch(arry, search):
    track = True
    while track:
        mid = (len(arry))//2
        if search == arry[mid]:
            return mid, arry
        elif len(arry) == 1:
            return "Not Found"
            # track = False
        elif search > arry[mid]:
            print("Greater")
            sleep(1)
            arry = arry[mid:]
            print(arry)
            continue
        else:
            print("lower")
            sleep(1)
            arry = arry[0: mid]
            print(arry)
            continue
    


print(binarySearch(original, 5))