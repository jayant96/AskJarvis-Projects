# Given a sorted array of n integers and a target value, determine if the target exists in the array in logarithmic time using the binary search algorithm. If target exists in the array, print the index of it.

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def main():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target = int(input())
    print(binary_search(arr, target))

if __name__ == '__main__':
    main()




