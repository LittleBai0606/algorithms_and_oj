class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = []
        length = len(nums)
        if length < 1:
            return None
        for i in range(length):
            oneNum = nums[i]
            otherNum = target - oneNum;
            if otherNum in nums:
                j = nums.index(otherNum)
                if i != j:
                    result.append(i)
                    result.append(j)
                    return result




