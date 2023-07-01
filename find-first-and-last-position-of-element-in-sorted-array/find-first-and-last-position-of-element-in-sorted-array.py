class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
    
        def findFirstOccurance(nums,target):
            l, r = 0, len(nums) - 1
            while l < r:
                mid = (l + r) // 2
                if nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid
            return l if nums[l] == target else -1
        
        def findLastOccurance(nums,target):
            l, r = 0, len(nums)-1

            while l < r:

                mid = (l+r) // 2 + 1

                if nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid
            return r if nums[r] == target else -1


        if not nums:
            return [-1,-1]
        
        first, last = findFirstOccurance(nums,target), findLastOccurance(nums,target)

        return [first,last]



