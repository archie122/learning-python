def twoSum( nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[j] + nums[i] == target:
                return [i, j]


print(twoSum([2, 7, 11, 15], 9))
