# Fibonacci series up to Nth term

class Solution:
    def series(self, n):

        fibonacci_series = [0, 1]  # Initialize the series with first two terms.

        # Generate the series up to the nth term.
        for _ in range(n - 1):
            next_term = (fibonacci_series[-1] + fibonacci_series[-2]) % (10**9 + 7)
            fibonacci_series.append(next_term)

        return fibonacci_series

solution = Solution()
n = 10  # Generate Fibonacci series up to the 10th term
result = solution.series(n)
print("Fibonacci series up to the {}th term:".format(n), result)
