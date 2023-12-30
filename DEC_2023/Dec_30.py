# Winner of an election

from collections import defaultdict

class Solution:
    def winner(self, arr):
        mp = defaultdict(int)
        
        for item in arr:
            mp[item] += 1
        
        winner_str = ""
        cnt = 0

        for key, value in mp.items():
            if value > cnt or (value == cnt and key < winner_str):
                winner_str = key
                cnt = value
        
        return [winner_str, str(cnt)]

# Example usage:
solution_instance = Solution()
arr_values = ["John", "Jane", "John", "Doe", "Jane"]
result = solution_instance.winner(arr_values)
print(result)
