"""
Given a list of HTTP reponse code for a webserver 

[200, 200, 200, ... 200, 500, 500, 500]

return the first index that web server is down, i.e. returning 500 response code


Input: an array of numbers, a number to find

Output: the index of the array at which num first appears, or -1 if it does not

"""


def find_first(array, num):
    start = 0
    end = len(array) - 1
    index = -1
    while(start <= end):
        mid = (end+start)//2
        if array[mid] > num:
            # go left
            end = mid - 1
        elif array[mid] == num:
            end = mid - 1
            index = mid
        else:
            start = mid+1
    return index 
