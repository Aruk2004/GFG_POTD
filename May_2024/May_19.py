# Find the closest number

from typing import List

class Solution:
    def findClosest(self, n: int, k: int, arr: List[int]) -> int:
        arr.append(int(1e9+7))
        l, r = 0, n - 1
        while l < r:
            m = l + (r - l + 1) // 2
            if arr[m] > k:
                r = m - 1
            else:
                l = m
        
        if abs(arr[l] - k) <= abs(arr[l + 1] - k):
            return arr[l]
        return arr[l + 1]

# Example usage
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    n = 6
    k = 7
    arr = [1, 3, 5, 6, 8, 9]
    print(solution.findClosest(n, k, arr))  # Output: 6
    
    # Test case 2
    n = 6
    k = 10
    arr = [1, 3, 5, 6, 8, 9]
    print(solution.findClosest(n, k, arr))  # Output: 9
    
    # Test case 3
    n = 6
    k = 4
    arr = [1, 3, 5, 6, 8, 9]
    print(solution.findClosest(n, k, arr))  # Output: 3
