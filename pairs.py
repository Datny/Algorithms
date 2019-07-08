# Problem
# Given an integer array, output all the * *unique ** pairs that sum up to a specific value k.


def pair_sum(arr, k):
    pairs = []
    for indx, el1 in enumerate(arr):
        for indx2, el2 in enumerate(arr):
            if indx2 == indx:
                continue
            else:
                if arr[indx] + arr[indx2] == k:
                    if (arr[indx], arr[indx2]) not in pairs and (arr[indx2], arr[indx]) not in pairs:
                        pairs.append((arr[indx], arr[indx2]))
    return print(pairs)

pair_sum([1,3,2,2],4)
pair_sum([1,9,2,8,3,7,4,6,5,5,13,14,11,13,-1],10)
pair_sum([1,2,3,1],3)
pair_sum([1,3,2,2],4)