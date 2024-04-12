# Sum of Products

class Solution:
    def pairAndSum(self, n, arr):
        #we initially take sum as 0
        sum=0
        #then we iterate through each bit position
        for i in range(32):
            #set bits refer to number of 1's in binary rep of integer
            #we are going to count the set bits at each position
            #inititally the count will be zero
            count=0
            #now we iterate through the array using j
            for j in arr:
                 # Check if the bit at position i is set (1) in the current element
                if j&(1<<i):
                    # Increment the count if the bit is set
                    count+=1
            #calculate the sum contributed by the bit position
            sum+=count*(count-1)//2*(1<<i)
        return sum

sol = Solution()
arr = [1, 2, 3, 4, 5]

result = sol.pairAndSum(len(arr), arr)
print(result)  # Output depends on the array elements and their binary representations
