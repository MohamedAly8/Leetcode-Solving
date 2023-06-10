class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:

        l = 0
        r = len(letters)

        ordtarget = ord(target)

        currcloset = [0, 100]
        
        while l < r:

            mid = (l + r ) // 2
            ordmid = ord(letters[mid])


            if ordmid > ordtarget:
                # look left since all to left are greater than target
                diff = ordmid - ordtarget
                if diff < currcloset[1]:
                    currcloset = [mid, diff]
                    print("Heeere forr ", letters[mid], "currclosest index is: ", currcloset[0])



                r = mid
            
            # all nums on left are less, need to look to right
            else:
                l = mid + 1
            
            
            

        return letters[currcloset[0]]
            







