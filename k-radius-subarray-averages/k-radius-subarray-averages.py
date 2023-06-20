class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:

        if len(nums) == 1:
            return [-1] if k > 1 else nums

        res = []

        for i in range(min(k,len(nums))):
            res.append(-1)

        midIndex = k

        if(midIndex+k < len(nums)):
            curSum = sum(nums[:k*2+1])

        # while our middle index can span the array
        while(midIndex+k < len(nums)):

            curAvg = curSum // ((k*2)+1)
            res.append(curAvg)
            curSum -= nums[midIndex-k]

            if midIndex+k+1 < len(nums):
                curSum += nums[midIndex+k+1]
            else:
                break
            midIndex += 1



        
        while len(res) < len(nums):
            res.append(-1)



        return res