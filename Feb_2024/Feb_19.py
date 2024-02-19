# Game with String

# Import necessary libraries
from collections import Counter
import heapq

class Solution:
    def minValue(self, s: str, k: int) -> int:
        # Count the frequency of characters
        freq_map = Counter(s)
        
        # Convert the frequency map to a list and heapify it
        heap = [-freq for freq in freq_map.values()]
        heapq.heapify(heap)
        
        # Reduce k largest frequencies by 1 each time
        while k > 0:
            freq = -heapq.heappop(heap)
            freq -= 1
            if freq:
                heapq.heappush(heap, -freq)
            k -= 1
        
        # Calculate the sum of squares of frequencies
        result = sum(freq * freq for freq in heap)
        
        return result

# Example usage
if __name__ == "__main__":
    # Instantiate the Solution class
    sol = Solution()

    # Example input string and k value
    s = "aabbbcc"
    k = 2

    # Calculate the minimum value
    min_val = sol.minValue(s, k)

    # Print the result
    print("Minimum value:", min_val)

