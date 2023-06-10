class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:

        l = 0
        r = len(letters)

        ordtarget = ord(target)
        
        while l < r:

            mid = (l + r ) // 2
            ordmid = ord(letters[mid])


            if ordmid > ordtarget:
                # look left since all to left are greater than target
                r = mid
            
            # all nums on left are less, need to look to right
            else:
                l = mid + 1
        
        return letters[r] if r < len(letters) else letters[0]
            







