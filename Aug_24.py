#Program to multiply strings

def multiplyStrings(s1, s2):
    s1 = s1[::-1]
    s2 = s2[::-1]
    
    isNeg1 = False
    isNeg2 = False
    
    if s1[-1] == '-':
        s1 = s1[:-1]
        isNeg1 = True
    if s2[-1] == '-':
        s2 = s2[:-1]
        isNeg2 = True
    
    s1 = s1.rstrip('0')
    s2 = s2.rstrip('0')
    
    len1 = len(s1)
    len2 = len(s2)
    
    out = ['0'] * (len1 + len2)
    
    for i in range(len2):
        carry = 0
        j = 0
        
        while j < len1:
            mul = (int(s2[i]) - int('0')) * (int(s1[j]) - int('0')) + (int(out[i + j]) - int('0')) + carry
            out[i + j] = str(mul % 10)
            carry = mul // 10
            j += 1
        
        while carry:
            mul = int(out[i + j]) - int('0') + carry
            out[i + j] = str(mul % 10)
            carry = mul // 10
            j += 1
    
    while out and out[-1] == '0':
        out.pop()
    
    if not out:
        return '0'
    
    if isNeg1 ^ isNeg2:
        out.append('-')
    
    out.reverse()
    
    return ''.join(out)

# Test the function
s1 = input("Enter the first number: ")
s2 = input("Enter the second number: ")
result = multiplyStrings(s1, s2)
print("Result:", result)
