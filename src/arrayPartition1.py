class Solution(object):
    def ArrayPairSum(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		nums.sort()
		tupleList = []
		tupleSum = 0
		for i in range(0,len(nums),2):
			currentTuple = (nums[i], nums[i+1])
			tupleList.append(currentTuple)
			tupleSum += min(currentTuple)
		return tupleSum

