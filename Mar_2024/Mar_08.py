# Check if frequencies can be equal

from collections import Counter

class Solution:
    def sameFreq(self, s: str) -> bool:
        freq_map = Counter(s)
        count_map = Counter(freq_map.values())
        
        if len(count_map) == 1:
            return True
        
        if len(count_map) == 2:
            counts = list(count_map.keys())
            smaller_count = min(counts)
            larger_count = max(counts)
            
            if smaller_count == 1 and count_map[smaller_count] == 1:
                return True
            
            if count_map[larger_count] == 1 and larger_count - smaller_count == 1:
                return True
        
        return False

# Example usage:
if __name__ == "__main__":
    sol = Solution()
    s = "abbccc"
    result = sol.sameFreq(s)
    print(result)  # Output: True

