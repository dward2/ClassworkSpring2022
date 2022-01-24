weight = 20 / 2.205
dosage = weight * 30

weight =  round(weight, 1)
dosage =  round(dosage, 1)

print("CORRECT DOSAGE")
print("For a patient weighing {} kg,".format(weight))
print("  the correct dosage is {} mg the first day".format(dosage))

