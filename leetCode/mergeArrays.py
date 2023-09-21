#nums1 = [1,2,3,0,0,0]
#nums2 = [2,5,6]
class Solution(object):
    @staticmethod
    def merge(nums1, m, nums2, n):
        # Initialize pointers for nums1 and nums2
        i = m - 1
        j = n - 1

        # Start merging from the end of nums1
        k = m + n - 1
        print(f" i = {i}, j = {j}, k = {k}\n")

        # While there are elements in both arrays
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                print(f"nums1[i] = {nums1[i]} :bigger than: nums2[j] = {nums2[j]}")
                nums1[k] = nums1[i]
                i -= 1
            else:
                print(f"nums2[j] = {nums2[j]} :bigger than: nums1[i] = {nums1[i]}")
                nums1[k] = nums2[j]
                j -= 1
            print(f"Final array: {nums1}\n")
            k -= 1

        # If there are remaining elements in nums2, copy them to nums1
        while j >= 0:
            print(f"remaining elements in 2nd arr\nnums1[i] = {nums1[i]} | nums2[j] = {nums2[j]}")
            nums1[k] = nums2[j]
            j -= 1
            k -= 1


def main():
    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 5, 6]
    m, n = 3, 3

    solution = Solution()
    solution.merge(nums1, m, nums2, n)

    print(nums1)  # Output: [1, 2, 2, 3, 5, 6]


if __name__ == "__main__":
    main()
