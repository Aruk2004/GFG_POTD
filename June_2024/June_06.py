# Max sum in the configuration

def max_sum(a,n):
    sum_A = sum(a)

    current_val = sum(i * a[i] for i in range(n))
    max_val = current_val

    for i in range(1, n):
        current_val = current_val + sum_A - n * a[n - i]
        max_val = max(max_val, current_val)

    return max_val
