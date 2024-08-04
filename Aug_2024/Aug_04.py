# N meetings in one room

class Solution:
    def maximumMeetings(self, n, start, end):
        meetings = [[start[i], end[i]] for i in range(n)]
        meetings.sort(key=lambda x: x[1])

        count = 1
        last_end = meetings[0][1]

        for i in range(1, n):
            if meetings[i][0] > last_end:
                count += 1
                last_end = meetings[i][1]

        return count
