class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """  
        for num in nums:
            if num == 0:
                index = nums.index(num)
                nums.pop(index)
                nums.append(0)