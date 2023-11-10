# Number following a pattern

class Solution:
    def printMinNumberForPattern(self, S):
        col = []
        curr = S[0]
        c = 1 if S[0] == 'I' else 0

        for i in S:
            if i == curr:
                c += 1
            else:
                col.append((curr, c))
                c = 1
                curr = i

        if S[-1] == 'I':
            c += 1
        col.append((curr, c))

        out = ""
        c = 1

        for op, cnt in col:
            temp = ""
            for _ in range(cnt + (1 if op == 'D' else -1)):
                temp += str(c)
                c += 1
            if op == 'D':
                temp = temp[::-1]
            out += temp

        return out

# Test the class and function
sol = Solution()
result = sol.printMinNumberForPattern("IDID")
print(result)  # Output: "13254"
