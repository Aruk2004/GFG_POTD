#Reverse String

class Solution:
    def reverseWord(s):
        i, j = 0, len(s) - 1
        s_list = list(s)
        
        while i < j:
            s_list[i], s_list[j] = s_list[j], s_list[i]
            i += 1
            j -= 1
        
        return ''.join(s_list)

# Example usage
input_string = "hello"
reversed_string = Solution.reverseWord(input_string)
print("Original:", input_string)
print("Reversed:", reversed_string)
