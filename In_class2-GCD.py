"""
Find the greateest common divisor of 2 number
"""

# Naive Method time O(N)
def naive(num1, num2):
    for i in range(num1, num2):
        if num1 % i == 0 and num2 % i == 0:
            result = i
    
    return result

# Efficient Method 
# Euclid GCD, gcd(a, b) = gcd(b, a % b)
def eff(num1, num2):
    if num2 > num1:
        tmp = num2
        num2 = num1
        num1 = tmp

    if num2 == 0:
        return num1
    else:
        remainder = num1 % num2
        return eff(num2, remainder)
    
if __name__ == "__main__":
    num1, num2 = map(int, input().split())
    print(eff(num1, num2))