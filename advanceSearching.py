# Binary Search
def binarySearch(nums, target):
    nums.sort() 
    left, right = 0, len(nums)-1


    while left <= right:
        mid  = (right - left) // 2 + left
        if nums[mid] == target: return mid
        elif nums[mid] < target: left = mid + 1
        else: right = mid - 1

    return -1 # if target is not in the list

