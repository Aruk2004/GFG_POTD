# Facing the sun

class Solution:
    # Returns count of buildings that can see sunlight
    def countBuildings(self, height):
        count = 0
        max_height = 0
        
        for h in height:
            if h > max_height:
                count += 1
                max_height = h
                
        return count
