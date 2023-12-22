# Maximum Meetings in One Room

class Solution:
    def maxMeetings(self, N, S, F):
        meet_list = []

        for i in range(N):
            meet_list.append((S[i], F[i], i + 1))

        meet_list.sort(key=lambda x: (x[1], x[0]))

        out = []
        last = 0
        for meet in meet_list:
            if last < meet[0]:
                last = meet[1]
                out.append(meet[2])

        return sorted(out)

# Example usage:
solution_instance = Solution()
N = 6
S = [1, 3, 0, 5, 8, 5]
F = [2, 4, 6, 7, 9, 9]
result = solution_instance.maxMeetings(N, S, F)
print(result)
