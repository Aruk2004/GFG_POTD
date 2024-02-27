# Play With OR

def game_with_number(arr, n):
    for i in range(n - 1):
        arr[i] |= arr[i + 1]
    return arr

# Example usage:
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    n = len(arr)
    result = game_with_number(arr, n)
    print(result)  # Output: [3, 3, 7, 7, 5]
