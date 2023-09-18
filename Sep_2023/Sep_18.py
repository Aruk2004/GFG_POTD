# Power of 2

def isPowerofTwo(n):
    return n and (n & (n - 1)) == 0

# Example usage:
if __name__ == "__main__":
    num = int(input("Enter a number: "))
    result = isPowerofTwo(num)
    if result:
        print(f"{num} is a power of two.")
    else:
        print(f"{num} is not a power of two.")
