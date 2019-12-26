peple = ["gilbert", "david", "richard"]
peple.insert(0, "justin")
peple.insert(2, "rayan")
peple.append("joseph")
print("welcome to my parlor, " + peple[0])
print("welcome to my parlor, " + peple[1])
print("welcome to my parlor, " + peple[2])
print("welcome to my parlor, " + peple[3])
print("welcome to my parlor, " + peple[4])
print("welcome to my parlor, " + peple[5])
print("\nI can only invite two peple to my parlor")
peple.pop(0)
peple.pop(0)
peple.pop(0)
peple.pop(0)
print(peple)

del peple[0]
del peple[0]
print(peple)