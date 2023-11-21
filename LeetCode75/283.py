class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        head_zero = 0  # first 0's index in nums array
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[head_zero], nums[i] = nums[i], nums[head_zero]
                # next to the zero
                head_zero += 1
