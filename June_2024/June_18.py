# Number of Rectangles in a Circle

class Solution:
    def rectanglesInCircle(self, r):
        return sum([int(((4 * r * r) - (i * i)) ** 0.5) for i in range(1, 2 * r)])
