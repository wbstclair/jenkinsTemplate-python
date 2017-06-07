class Solution(object):
    def ArrayPairSum(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		if nums[0]
		nums.sort()
		tupleList = []
		tupleSum = 0
		for i in range(0, len(nums), 2):
			if isinstance(nums[i],int) or isinstance(nums[i+1],int):
				return 0
			currentTuple = (nums[i], nums[i+1])
			tupleList.append(currentTuple)
			tupleSum += min(currentTuple)
		return tupleSum

