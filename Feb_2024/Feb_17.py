# Does array represent Heap

class Solution:
    def isMaxHeap(self, arr, n):
        t1 = (n - 1) // 2
        
        for i in range(t1 + 1):  # Include the last internal node
            left_child_idx = 2 * i + 1
            right_child_idx = 2 * i + 2
            
            if left_child_idx < n and arr[i] < arr[left_child_idx]:
                return False
            if right_child_idx < n and arr[i] < arr[right_child_idx]:
                return False
        
        return True

# Example usage
if __name__ == "__main__":
    # Instantiate the Solution class
    sol = Solution()

    # Example input array and its length
    arr = [9, 5, 3, 8]
    n = len(arr)

    # Check if the array represents a max-heap
    is_max_heap = sol.isMaxHeap(arr, n)

    # Print the result
    print("Is the array a max-heap?", "Yes" if is_max_heap else "No")
