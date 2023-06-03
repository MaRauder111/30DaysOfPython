def prime(n):
    i = 1
    while i%n == 0:
        print(n)
        if n%i == 0:
            return True
        else:
            return False


print(prime(2))