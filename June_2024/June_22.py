# Extract the Number from the String

class Solution:
    def ExtractNumber(self,sentence):
        words = sentence.split()
        ans =- 1
        for i in words:
            if i.isdigit():
                if '9' not in i:
                    ans = max(ans, int(i))
        return ans
