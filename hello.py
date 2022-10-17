def isprime(x):
    for p in range(2, int(x**0.5)):
        if x % p == 0:
            return False
    return True

print('aboba')

for i in range(15):
    print(isprime(int(input())))
