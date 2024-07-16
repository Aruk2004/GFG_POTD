# Remaining String

class Solution:
	def printString(self, s, ch, count):
		if ch not in s:
		    return ""

		temp = 0
		size = 0
		for i in s:
		    if i == ch:
		        temp+=1
            size += 1

		    if temp == count:
		        return s[size:]
	    return ""
