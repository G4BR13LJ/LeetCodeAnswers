class Solution(object):
    @staticmethod
    def removeElement(nums, val):
        k = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        # while k < len(nums):
        #     nums[k] = '_'
        #     k += 1
        print(k)


def main():
    nums = [3, 2, 2, 3]
    val = 3

    solution = Solution()
    solution.removeElement(nums, val)

    print(nums)


if __name__ == "__main__":
    main()
