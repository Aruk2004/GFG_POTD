# Check if a string is repetition of its substring of k-length

class Solution:
    def kSubstrConcat(self, n, s, k):
        if n % k > 0:
            return 0

        mp = {}
        for i in range(0, n // k):
            substr = s[i * k : (i + 1) * k]
            mp[substr] = mp.get(substr, 0) + 1

        cnt = sum(val > 1 for val in mp.values())
        return len(mp) <= 2 and cnt <= 1

# Example usage:
solution_instance = Solution()
n_value = 10  # Replace with your n value
s_value = "abcabcabc"  # Replace with your s value
k_value = 3  # Replace with your k value
result = solution_instance.kSubstrConcat(n_value, s_value, k_value)
print(result)
