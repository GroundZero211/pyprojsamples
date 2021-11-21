def findFactor(n):
    return [i for i in range(1, n+1) if n % i == 0]

print("Factors of {}: {}".format(36, findFactor(36)))
print("Factors of {}: {}".format(40, findFactor(40)))
print("Factors of {}: {}".format(25, findFactor(25)))
print("Factors of {}: {}".format(89, findFactor(89)))
print("Factors of {}: {}".format(21, findFactor(21)))
