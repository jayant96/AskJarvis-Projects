# Given an unsorted integer array, find a pair with the given sum in it.


def findPair(arr, n, sum):
    for i in range(0, n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == sum:
                print(arr[i], arr[j])
                return True
    return False

arr = [8, 7, 2, 5, 3, 1]
sum = 10
n = len(arr)
if findPair(arr, n, sum):
    print("Array has two elements with the given sum")
else:
    print("Array doesn't have two elements with the given sum")



##################################################################

# Given two sorted arrays X[] and Y[] of size m and n each where m >= n and X[] has exactly n vacant cells, merge elements of Y[] in their correct position in array X[], i.e., merge (X, Y) by keeping the sorted order.


def merge(X, Y, m, n):
    i = m - 1
    j = n - 1
    k = m + n - 1
    while i >= 0 and j >= 0:
        if X[i] > Y[j]:
            X[k] = X[i]
            i -= 1
        else:
            X[k] = Y[j]
            j -= 1
        k -= 1
    while j >= 0:
        X[k] = Y[j]
        j -= 1
        k -= 1

X = [1, 2, 3, 0, 0, 0]
Y = [2, 5, 6]
m = 3
n = 3
merge(X, Y, m, n)
print(X)



##################################################################

#Given an integer array, find the maximum product of its elements among all its subsets.


def maxProduct(nums):
    nums.sort()
    return max(nums[-1]*nums[-2]*nums[-3], nums[0]*nums[1]*nums[-1])

print(maxProduct([-4,-3,-2,-1,60]))


##################################################################

# Given a binary array, sort it in linear time and constant space. The output should print all zeroes, followed by all ones.


def sort_binary_array(arr):
    zeros = ones = 0
    for i in range(len(arr)):
        if arr[i] == 0:
            zeros += 1
        else:
            ones += 1
    for i in range(zeros):
        arr[i] = 0
    for i in range(ones):
        arr[zeros + i] = 1
    return arr

arr = [0, 1, 0, 1, 0, 0, 1, 1, 1, 0]
print(sort_binary_array(arr))



##################################################################

# Given a limited range array of size n containing elements between 1 and n-1 with one element repeating, find the duplicate number in it without using any extra space.


def findDuplicate(arr):
    for i in range(len(arr)):
        if arr[abs(arr[i])] >= 0:
            arr[abs(arr[i])] = -arr[abs(arr[i])]
        else:
            return abs(arr[i])

arr = [1, 2, 3, 4, 4]
print(findDuplicate(arr))

##################################################################

# Given an integer array, find the maximum length subarray having a given sum.


def max_subarray_sum(arr, k):
    max_sum = 0
    for i in range(len(arr)):
        curr_sum = 0
        for j in range(i, len(arr)):
            curr_sum += arr[j]
            if curr_sum == k:
                max_sum = max(max_sum, j - i + 1)
    return max_sum

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
k = 15
print(max_subarray_sum(arr, k))


##################################################################

#Given a sorted integer array, find the floor and ceil of a given number in it. The floor and ceil map the given number to the largest previous or the smallest following integer in the array.


def floor_ceil(arr, n):
    if n < arr[0]:
        return arr[0], arr[0]
    if n > arr[-1]:
        return arr[-1], arr[-1]
    for i in range(1, len(arr)):
        if arr[i] > n:
            return arr[i - 1], arr[i]

arr = [1, 2, 8, 10, 10, 12, 19]
n = 5
print(floor_ceil(arr, n))



##################################################################

#Given an integer array, find the maximum product of two integers in it.


def max_product(nums):
    nums.sort()
    return max(nums[-1] * nums[-2], nums[0] * nums[1])

print(max_product([1,5,4,5]))


##################################################################

#Given an integer array, find the maximum sum of subsequence where the subsequence contains no element at adjacent positions.


def maxSum(arr):
    n = len(arr)
    max_so_far = 0
    max_ending_here = 0
    for i in range(0, n):
        max_ending_here = max_ending_here + arr[i]
        if max_ending_here < 0:
            max_ending_here = 0
        elif (max_so_far < max_ending_here):
            max_so_far = max_ending_here
    return max_so_far

arr = [-2, -3, 4, -1, -2, 1, 5, -3]
print(maxSum(arr))



##################################################################

#Given an array of positive and negative integers, segregate them in linear time and constant space. The output should print all negative numbers, followed by all positive numbers.


def segregate(arr):
    j = 0
    for i in range(len(arr)):
        if arr[i] < 0:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
    return arr

arr = [12, 11, -13, -5, 6, -7, 5, -3, -6]
print(segregate(arr))


##################################################################