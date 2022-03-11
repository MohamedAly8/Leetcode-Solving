class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        list = []
        for i in range(len(nums)):
            if nums[i] in dic:
                list.append(i)
                list.append(dic[nums[i]])
            else:
                dic[target - nums[i]] = i
        return list