# Find the Highest number

from typing import List

class Solution:
    def findPeakElement(self, a: List[int]) -> int:
        left, right = 0, len(a) - 1

        while left < right:
            mid = (left + right) // 2

            if a[mid] > a[mid + 1]:
                right = mid
            else:
                left = mid + 1

        return a[left]

# Example usage
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    n = 11
    a = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]
    print(solution.findPeakElement(a))  # Output: 6

    # Test case 2
    n = 5
    a = [1, 2, 3, 4, 5]
    print(solution.findPeakElement(a))  # Output: 5
