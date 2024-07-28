# Remove Duplicates

class Solution:
    def removeDups(self, str):

        unique_alpha = [0] * 26
        result = ''

        for i in range(len(str)): 
            if unique_alpha[ord(str[i]) - 97] == 0: 
                result += str[i]
                unique_alpha[ord(str[i]) - 97] += 1

        return result
