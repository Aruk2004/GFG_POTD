# Buy Maximum Stocks if i stocks can be bought on i-th day

class Solution:
    def buyMaximumProducts(self, n, k, price):
        v = [(price[i], i + 1) for i in range(n)]
        v.sort()

        out = 0

        for i in v:
            max_buy = min(k // i[0], i[1])
            out += max_buy
            k -= i[0] * max_buy

        return out

# Example usage:
solution_instance = Solution()
n = 3
k = 17
price = [10, 7, 19]
result = solution_instance.buyMaximumProducts(n, k, price)
print(result)
