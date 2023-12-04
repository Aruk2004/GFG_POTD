# Sum-string

class Solution:
    def add(self, num1, num2):
        carry = 0
        i = len(num1) - 1
        j = len(num2) - 1
        res = []

        while i >= 0 and j >= 0:
            _sum = int(num1[i]) + int(num2[j]) + carry
            res.append(str(_sum % 10))
            carry = _sum // 10
            i -= 1
            j -= 1

        while i >= 0:
            _sum = int(num1[i]) + carry
            res.append(str(_sum % 10))
            carry = _sum // 10
            i -= 1

        while j >= 0:
            _sum = int(num2[j]) + carry
            res.append(str(_sum % 10))
            carry = _sum // 10
            j -= 1

        if carry:
            res.append(str(carry))

        return ''.join(res[::-1])

    def solve(self, s, i, j, k):
        num1 = s[i:j]
        num2 = s[j:k]
        _sum = self.add(num1, num2)

        n = len(_sum)
        length = k + n

        if length > len(s):
            return 0

        curr_sum = s[k:length]

        if curr_sum != _sum:
            return 0

        if length == len(s):
            return 1

        return self.solve(s, j, k, length)

    def isSumString(self, s):
        n = len(s)

        for j in range(1, n):
            for k in range(j + 1, n):
                if self.solve(s, 0, j, k):
                    return 1

        return 0

# Example usage:
solution = Solution()
result = solution.isSumString("12243660")
print(result)  # Output: 1
