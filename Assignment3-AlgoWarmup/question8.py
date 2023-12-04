#%%
# find GCD with Euclid algo
class Solution():
    def find_GCD(self, m, n):
        while m != 0:
            tmp = m
            m = n % m
            n = tmp
        return n
    
    def find_LCM(self, m, n):
        gcd = self.find_GCD(m, n)
        return (m * n) // gcd

if __name__ == "__main__":
    sol = Solution()
    m, n = map(int, input().split()) 
    if m > n:
        tmp = m
        m = n
        n = tmp
    print(sol.find_LCM(m, n))
# %%
