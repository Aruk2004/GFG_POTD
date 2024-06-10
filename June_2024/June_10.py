# Nuts and Bolts Problem

class Solution:

   def matchPairs(self, n, nuts, bolts):
        order = [ '!','#','$','%','&','*','?','@','^']
        n = []
        for i in order:
            if i in nuts and i in bolts:
                n.append(i)
        nuts[:] = n
        bolts[:] = n
