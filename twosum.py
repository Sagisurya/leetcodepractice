class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        Dict = {}
        for i in range(len(nums)):
            if target - nums[i] in Dict:
                result.append(Dict[target - nums[i]])
                result.append(i)
                return result
            Dict[nums[i]] = i