# Power Set

class Solution:
    def __init__(self):
        self.out = []
        self.curr = ""
    
    def subSeq(self, i, s):
        if i == len(s):
            if self.curr:
                self.out.append(self.curr)
            return
        
        self.curr += s[i]
        self.subSeq(i + 1, s)
        self.curr = self.curr[:-1]
        self.subSeq(i + 1, s)
    
    def AllPossibleStrings(self, s: str) -> List[str]:
        self.subSeq(0, s)
        self.out.sort()
        return self.out

# Example usage:
if __name__ == "__main__":
    sol = Solution()
    result = sol.AllPossibleStrings("abc")
    print(result)  # Output: ['', 'a', 'ab', 'abc', 'ac', 'b', 'bc', 'c']
