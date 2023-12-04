#%%
"""
Find Huge Fibonacci number mod m
Find nth Fibonacci number modulo m (int)
"""
class Solution():
    def find_pisano_len(self, m):
        first = 0
        sec = 1
        for i in range(m ** 2):
            mod = (first + sec) % m
            first = sec
            sec = mod
            if first == 0 and sec == 1:
                return i + 1
            
    def find_modulo(self, n, m):
       
        if n < 1:
            return n % m
        else:
            pisano_len = self.find_pisano_len(m)
            while n > pisano_len:
                n = n % pisano_len
            first = 0
            sec = 1
            for i in range(n):
                sum = first + sec
                first = sec
                sec = sum
            
            return first % m
            


#%%

if __name__ == "__main__":
    n, m = map(int, input().split())
    sol = Solution()
    print(sol.find_modulo(n, m))        