def multiplier(factor):
    def multiply(x):
        return x * factor
    return multiply

double = multiplier(2)
triple = multiplier(3)


print(double(2))
print(double(7))
print(triple(6))

print(multiplier(10)(5))