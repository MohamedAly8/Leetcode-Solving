class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:


        
        diff_c = ord(coordinates[0]) - ord('a')
        n = int(coordinates[1]) - 1

        return not ((n % 2 == 0 and diff_c % 2 == 0) or (n % 2 != 0 and diff_c % 2 != 0))
        







