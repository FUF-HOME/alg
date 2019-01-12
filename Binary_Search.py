def binary_search(nums, target):
    low = 0
    height = len(nums) - 1
    mid = int((low+height)/2)
    while low <= height:
        guess = nums[mid]
        if guess == target:
            return guess
        if guess > target:
            height = mid -1
        else:
            low  = mid +1
    return None