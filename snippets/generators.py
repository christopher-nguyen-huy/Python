# Generator example
def genrange(max):
    k = 0
    while k < max:
        yield k
        k += 1

# Shove into object
funcvar = genrange(32)

# 1st way to call out
for j in funcvar:
	pass
for i in genrange(42):
	pass

# 2nd way
funcvar = genrange(32)
print(funcvar.next())
print(next(funcvar))

# Generator comprehension
even_generator = (k for k in range(20) if k % 2 == 0)
print(even_generator.next())

