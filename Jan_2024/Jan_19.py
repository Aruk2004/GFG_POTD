# Top k numbers in a stream


class Solution:
    def kTop(self, array, size, k):
        result = []
        current_top = [0 for _ in range(k + 1)]  # Array to store the current top K elements
        frequency = {i: 0 for i in range(k + 1)}  # Dictionary to store the frequency of elements in current_top

        for index in range(size):
            # Update the frequency of the current element in the array
            frequency[array[index]] = frequency.get(array[index], 0) + 1

            # Set the last element of current_top as the current element from the array
            current_top[k] = array[index]

            # Find the correct position for the current element in the current_top array
            i = current_top.index(array[index]) - 1
            while i >= 0:
                # Compare frequencies and values for sorting
                if (frequency[current_top[i]] < frequency[current_top[i + 1]]) or \
                        ((frequency[current_top[i]] == frequency[current_top[i + 1]]) and
                         (current_top[i] > current_top[i + 1])):
                    current_top[i], current_top[i + 1] = current_top[i + 1], current_top[i]
                else:
                    break
                i -= 1

            # Extract the top K elements and append them to the result list
            i = 0
            current_result = []
            while i < k and current_top[i] != 0:
                current_result.append(current_top[i])
                i += 1

            result.append(current_result)

        return result

  # Example usage:
sol = Solution()

# Test Case 1
arr1 = [5, 2, 1, 3, 2]
N1, K1 = len(arr1), 4
output1 = sol.kTop(arr1, N1, K1)
for line in output1:
    print(' '.join(map(str, line)))

# Test Case 2
arr2 = [2, 1, 2, 1, 2, 1]
N2, K2 = len(arr2), 3
output2 = sol.kTop(arr2, N2, K2)
for line in output2:
    print(' '.join(map(str, line)))
