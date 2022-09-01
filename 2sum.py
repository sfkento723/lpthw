from array import*
def twoSum(nums, target):
    for i, num in enumerate(nums):
        for j in range(i + 1, len(nums)):
            if num + nums[j] == target:
                return [i, j]

numbers = array('i', [2, 7, 11, 15])
targetnumber = 9

print(twoSum(numbers, targetnumber))
