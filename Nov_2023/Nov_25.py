# Shuffle integers

class Solution:
    def shuffleArray(self, arr, n):
        offset = 10**5
    
        for i in range(n // 2):
            arr[i * 2] += (arr[i] % offset) * offset
            arr[i * 2 + 1] += (arr[n // 2 + i] % offset) * offset
    
        for i in range(n):
            arr[i] = arr[i] // offset

# Example usage:
arr1 = [1, 2, 9, 15]
shuffleArray(arr1, len(arr1))
print(arr1)  # Output: [1, 9, 2, 15]

arr2 = [1, 2, 3, 4, 5, 6]
shuffleArray(arr2, len(arr2))
print(arr2)  # Output: [1, 4, 2, 5, 3, 6]
