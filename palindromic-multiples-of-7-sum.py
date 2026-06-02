#Among the integers from 1 to 50000: Find the sum of all numbers that:
#are divisible by 7,
#and are palindromes

def palindrome(m):
    M=str(m)
    return M==M[::-1]

def div(m):
    return m%7==0

def sum(n):
    s=0
    for i in range (1,n+1):
        if palindrome(i) and div(i):
            s+=i
    return s

print(sum(50000))