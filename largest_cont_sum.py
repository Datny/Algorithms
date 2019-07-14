from copy import deepcopy

# Largest Continuous Sum Problem
# Given an array of integers (positive and negative) find the largest continuous sum.
# With begginning and ending point.

def large_cont_sum(arr):
    left_max_sum = 0
    left_max_idx = 0
    for idx1, el2 in enumerate(arr):
        cont_sum_arr = deepcopy(arr)
        total_sum = 0
        for idx2, el2 in enumerate(cont_sum_arr[idx1:]):
            total_sum += el2
            cont_sum_arr[idx2] = total_sum
        if max(cont_sum_arr) > left_max_sum:
            left_max_sum = max(cont_sum_arr)
            left_max_idx = idx1
            right_max_idx = idx1 + idx2 - 2
    return (left_max_sum)


large_cont_sum([-30,1,2,-1,3,4,10,10,-10,-1])

from nose.tools import assert_equal


class LargeContTest(object):
    def test(self, sol):
        assert_equal(sol([1, 2, -1, 3, 4, -1]), 9)
        assert_equal(sol([1, 2, -1, 3, 4, 10, 10, -10, -1]), 29)
        assert_equal(sol([-1, 1]), 1)
        print('ALL TEST CASES PASSED')


# Run Test
t = LargeContTest()
t.test(large_cont_sum)