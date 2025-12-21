def est_divisible(a, b):
    if a % b == 0 or b % a == 0:
        return True
    else:
        return False

# Exemples de test
print(est_divisible(2, 3))   # False
print(est_divisible(4, 8))   # True
print(est_divisible(8, 4))   # True
print(est_divisible(15, 3))  # True
print(est_divisible(7, 5))   # False