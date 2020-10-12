
# 204. Count Primes


# Count the number of prime numbers less than a non-negative number, n.

# Example 1:
# Input: n = 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

# Example 2:
# Input: n = 0
# Output: 0

# Example 3:
# Input: n = 1
# Output: 0



class Solution():
    def countPrimes(self, n):
        # eliminate 0 & 1 
        if n <= 1:
            return 0
        # set an array with n size, elements of True
        isPrime = [True] * n 
        
        i = 2 
        # this is the key, if i is not prime, i^2 wont be prime 
        while i * i < n:
            if isPrime[i] == True:
                j = 2
                while i * j < n:
                    # if i is not a prime, multiple of i never ever gonna be prime
                    # change the multiple to false 
                    isPrime[i*j] = False
                    j += 1
            i += 1
        return isPrime.count(True) - 2
    
s = Solution()
print(s.countPrimes(10))
print(s.countPrimes(0))
print(s.countPrimes(1))
