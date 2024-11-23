t = int(input())
for case in range(t):
    n = int(input())
    count = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            count += 1
            if i != n // i:
                count += 1
    is_prime = True
    if count <= 1:
        is_prime = False
    for i in range(2, int(count**0.5) + 1):
        if count % i == 0:
            is_prime = False
            break
    print(is_prime)