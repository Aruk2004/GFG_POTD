# Smallest window containing 0, 1 and 2

class Solution:
    def smallestSubstring(self, S):
        n = len(S)
        count_0 = count_1 = count_2 = 0
        left = 0
        min_length = float('inf')

        for right in range(n):
            if S[right] == '0':
                count_0 += 1
            elif S[right] == '1':
                count_1 += 1
            elif S[right] == '2':
                count_2 += 1

            while count_0 > 0 and count_1 > 0 and count_2 > 0:
                min_length = min(min_length, right - left + 1)

                if S[left] == '0':
                    count_0 -= 1
                elif S[left] == '1':
                    count_1 -= 1
                elif S[left] == '2':
                    count_2 -= 1
                left += 1

        if min_length == float('inf'):
            return -1
        else:
            return min_length

# Example usage:
solution_instance = Solution()
print(solution_instance.smallestSubstring("10212"))  # Output: 3

print(solution_instance.smallestSubstring("12121"))  # Output: -1
