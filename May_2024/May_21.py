# K closest elements

from typing import List

class Solution:
    def findCrossOver(self, arr: List[int], low: int, high: int, x: int) -> int:
        # Base cases
        if arr[high] <= x:
            return high
        if arr[low] > x:
            return low

        mid = (low + high) // 2

        # Check if mid is the crossover point
        if arr[mid] <= x and arr[mid + 1] > x:
            return mid
        elif arr[mid] < x:
            return self.findCrossOver(arr, mid + 1, high, x)
        return self.findCrossOver(arr, low, mid - 1, x)

    def printKClosest(self, arr: List[int], n: int, k: int, x: int) -> List[int]:
        # Find the crossover point
        crossoverIndex = self.findCrossOver(arr, 0, n - 1, x)
        leftIndex = crossoverIndex
        rightIndex = crossoverIndex + 1

        # If the element is present, move left index back
        if leftIndex >= 0 and arr[leftIndex] == x:
            leftIndex -= 1

        closestElements = []
        for _ in range(k):
            # Both indices are valid
            if leftIndex >= 0 and rightIndex < n:
                leftDiff = x - arr[leftIndex]
                rightDiff = arr[rightIndex] - x
                # Choose the closer element
                if leftDiff <= rightDiff:
                    closestElements.append(arr[leftIndex])
                    leftIndex -= 1
                else:
                    closestElements.append(arr[rightIndex])
                    rightIndex += 1
            elif leftIndex >= 0:  # Only left index is valid
                closestElements.append(arr[leftIndex])
                leftIndex -= 1
            else:  # Only right index is valid
                closestElements.append(arr[rightIndex])
                rightIndex += 1

        return closestElements

# Example usage
if __name__ == "__main__":
    solution = Solution()
    
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    n = len(arr)
    k = 3
    x = 5
    print(f"The {k} closest elements to {x} are: {solution.printKClosest(arr, n, k, x)}")
