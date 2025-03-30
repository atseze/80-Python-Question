s1 = "listen"
s2 = "silenttt"

a1 = sorted(set(s1))
a2 = sorted(set(s2))

res = True if a1 == a2 else False
print(res)



print(True if sorted(s1) == sorted(s2) else False)