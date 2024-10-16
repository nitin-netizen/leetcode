class Solution(object):
    # We use a dictionary num_dict to store the values we have seen and their corresponding indices.
    def twoSum(self, nums, target):
        num_dict = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_dict:
                return [num_dict[complement], i]
            num_dict[num] = i
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
