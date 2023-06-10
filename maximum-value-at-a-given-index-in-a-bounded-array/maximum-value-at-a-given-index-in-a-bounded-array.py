class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:

        def test(mid):
            return get_sum(max(mid - left, 0), mid) + get_sum(max(mid - right, 0), mid - 1)

        def get_sum(start, end):
            return (start + end) * (end - start + 1) // 2

        left, right = index, n - index - 1
        maxSum -= n
        low, high = 0, maxSum
        while low < high:
            mid = (low + high + 1) // 2
            if test(mid) <= maxSum:
                low = mid
            else:
                high = mid - 1
        return low + 1

            




        
        