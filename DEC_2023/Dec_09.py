# Smith Number

class Solution:
    def is_prime(self, n):
        if n == 1:
            return False

        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False

        return True

    def sum_of_digits(self, n):
        return sum(int(digit) for digit in str(n))

    def sum_of_prime_factor(self, n):
        f = 2
        total_sum = 0

        while n > 1:
            if not self.is_prime(f):
                f += 1
                continue

            while n % f == 0:
                total_sum += self.sum_of_digits(f)
                n //= f

            f += 1

        return total_sum

    def smith_num(self, n):
        if self.is_prime(n):
            return 0

        return self.sum_of_prime_factor(n) == self.sum_of_digits(n)

# Example usage:
solution = Solution()
result = solution.smith_num(4)
print(result)  # Output: 1
