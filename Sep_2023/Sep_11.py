# Lucky Number

def is_lucky(n):
  cnt = 2
  while cnt <= n:
    if n % cnt == 0:
      return False
    n -= n // cnt
    cnt += 1
  return True

if __name__ == "__main__":
  number = int(input("Enter a number: "))
  if is_lucky(number):
    print(number, "is a lucky number.")
  else:
    print(number, "is not a lucky number.")
