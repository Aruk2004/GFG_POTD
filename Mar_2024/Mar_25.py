# Print N-bit binary numbers having more 1s than 0

class Solution:

	def NBitBinary(self, n):
        binary_numbers = []

        def generate(number, length, zero_count):
            # Base case
            if length == n:
                binary_numbers.append(number)
                return
            # Recursive case
            generate(number + "1", length + 1, zero_count)
            if zero_count * 2 < length:
                generate(number + "0", length + 1, zero_count+1)

        generate("", 0, 0)
        return binary_numbers

solution = Solution()
n = 3  # Generate N-bit binary numbers
result = solution.NBitBinary(n)
print("N-bit binary numbers with more 1s than 0s:", result)
