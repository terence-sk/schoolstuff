precise = 0
not_precise = 0

for i in range(1,10000):
    not_precise += 1/i

for i in range(10000,0, -1):
    precise += 1/i

print("Presne: " + str(precise) + "\nNepresne: " + str(not_precise))
diff = abs(precise-not_precise)
print("Rozdiel: "  + str(diff))