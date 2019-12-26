# This tings calculate anything... almost
# opp means operation
#do nothing

print ("Make an equasion and I will resolve it.")
nb = input("Chose a first num: ")
#nb.to_f
op = input("Chose a opperation: ")
#opp.to_f
nbb = input("chose another num: ")
#nbb.to_f

print (nb + op + nbb + " = ")
if op == "+":
  print (nb + nbb)
elif op == "-":
  print (nb - nbb)
elif op == "*":
  print (nb * nbb)
elif op == "/":
  print (nb / nbb)
else:
  print ("Invalid operator")
