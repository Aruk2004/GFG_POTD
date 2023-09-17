# Print first n Fibonacci Numbers

class Solution:
    def printFibb(self, n):
        if n <= 2:
            return [1] * n

        out = [0] * n
        out[0] = out[1] = 1

        for i in range(2, n):
            out[i] = out[i - 1] + out[i - 2]

        return out

if __name__ == "__main__":
    solution = Solution()
    n = 10 
    result = solution.printFibb(n)
    print(result)
