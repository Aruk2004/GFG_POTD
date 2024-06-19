# Find maximum volume of a cuboid

class Solution:
    def maxVolume(self, p, a):
        x = (p - math.sqrt(p ** 2 - 24 * a)) / 12
        V = (p * x ** 2 - 8 * x ** 3) / 4
        return round(V, 2)
