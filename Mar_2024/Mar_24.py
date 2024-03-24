# Insert an Element at the Bottom of a Stack

class Solution:
    def insertAtBottom(self,st,x):
        st.insert(0, x)
        return st

solution = Solution()
stack = [1, 2, 3, 4]  # Example stack
element_to_insert = 5  # Element to insert at the bottom

result = solution.insertAtBottom(stack, element_to_insert)
print("Stack after inserting at the bottom:", result)
