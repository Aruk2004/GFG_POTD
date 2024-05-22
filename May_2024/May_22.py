# Minimize Max Distance to Gas Station

class Solution:
    def findSmallestMaxDist(self, stations, K):
        def is_feasible(d):
            required_stations = 0
            for i in range(len(stations) - 1):
                distance = stations[i+1] - stations[i]
                required_stations += int(distance / d)
            return required_stations <= K

        left, right = 0, max(stations[i+1] - stations[i] for i in range(len(stations) - 1))

        while right - left > 1e-7:  # Higher precision for binary search termination
            mid = (left + right) / 2
            if is_feasible(mid):
                right = mid
            else:
                left = mid

        return round(right, 2)

# Example usage:
solution = Solution()
stations = [1, 2, 3, 4, 5, 6, 7, 8, 9]
K = 3
print(solution.findSmallestMaxDist(stations, K))  # Output should be the smallest max distance after adding K stations
