# Find element occuring once when all other are present thrice

class Solution:
    def singleElement(self, arr, N):
        ones, twos = 0, 0

        for num in arr:
            # Add bits to twos if they are already present in ones
            twos |= (ones & num)

            # XOR the bits in ones with the bits in num
            ones ^= num

            # The common bits in ones and twos are set to 0
            common_bits = ones & twos
            ones &= ~common_bits
            twos &= ~common_bits

        return ones if ones < (1 << 31) else ones - (1 << 32)


# Example usage:
sol = Solution()
arr1 = [1, 10, 1, 1]
arr2 = [3, 2, 1, 34, 34, 1, 2, 34, 2, 1]

output1 = sol.singleElement(arr1, len(arr1))
output2 = sol.singleElement(arr2, len(arr2))

print(output1)  # Output: 10
print(output2)  # Output: 3
