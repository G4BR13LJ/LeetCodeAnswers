# removes duplicates in an ordered int list
def removeDuplicates(nums):
    position = 0
    while position + 1 < len(nums):
        if nums[position] == nums[position + 1]:
            nums.remove(nums[position])
            position -= 1
        position += 1
    print(nums)
    return len(nums)


removeDuplicates([0, 0, 0, 1, 1, 1, 1, 2, 2, 3, 3, 4, 4])
