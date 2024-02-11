# Recamans sequence

class Solution:
    def recamanSequence(self, n):
        a = [0] * (n + 1)
        st = set()
        for i in range(1, n + 1):
            if a[i - 1] - i > 0 and (a[i - 1] - i) not in st:
                a[i] = a[i - 1] - i
            else:
                a[i] = a[i - 1] + i
            st.add(a[i])
        return a

# Example usage:
sol = Solution()
n = 10
print(sol.recamanSequence(n))  # Output: [0, 1, 3, 6, 2, 7, 13, 20, 12, 21, 11]
