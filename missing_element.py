#A second array is formed by shuffling the elements of the first array and deleting a random element.
#find and return number that makes difference
# Input:
#

# Output:
#
# 5 is the missing number


## also possible to make hash map, add and substract elements and check whhich value of which key is 0

def finder1(arr1,arr2):
    num = 0
    for n in arr1:
        num += n
    for n in arr2:
        num -= n
    return num


def finder(arr1,arr2):
    arr1.sort()
    arr2.sort()

    for el1, el2 in zip(arr1,arr2):
        if el1 != el2:
            return el1

print(finder([1,2,3,4,5,6,7],[3,7,2,1,4,6]))