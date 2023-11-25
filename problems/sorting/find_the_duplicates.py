"""
Given 2 sorted array arr1 and arr2 return a sorted list that contains 
duplicate numbers

input:  arr1 = [1, 2, 3, 5, 6, 7], arr2 = [3, 6, 7, 8, 20]

output: [3, 6, 7] 

"""


def find_duplicates(arr1, arr2):
    n = len(arr1)
    m = len(arr2)
    idx1 = 0
    idx2 = 0
    result = []

    while(idx1 < n and idx2 < m):
        v1 = arr1[idx1]
        v2 = arr2[idx2]
        if v1 == v2:
            result.append(v1)
            idx1+=1
            idx2+=1
        elif v1<v2:
            idx1+=1
        else:
            idx2+=1
    return result



